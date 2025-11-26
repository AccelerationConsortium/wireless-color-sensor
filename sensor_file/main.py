
import sys
import json
import ssl
import ntptime
from uio import StringIO
from time import sleep, ticks_ms, ticks_diff

from machine import I2C, Pin

# WiFi
from netman import connectWiFi

# Hardware
import machine
from neopixel import NeoPixel
from as7341_sensor import Sensor

# MQTT
from umqtt.simple import MQTTClient

from my_secrets import (
    SSID,
    PASSWORD,
    HIVEMQ_HOST,
    HIVEMQ_PASSWORD,
    HIVEMQ_USERNAME,
    COURSE_ID,
    PICO_ID,
)


def get_onboard_led():
    try:
        onboard_led = Pin("LED", Pin.OUT)  # only works for Pico W
    except Exception as e:
        print(e)
        onboard_led = Pin(25, Pin.OUT)
    return onboard_led

onboard_led = get_onboard_led()


def sign_of_life(led, first, blink_interval_ms=5000):
    global last_blink
    if first:
        led.on()
        last_blink = ticks_ms()
    time_since = ticks_diff(ticks_ms(), last_blink)
    if led.value() == 0 and time_since >= blink_interval_ms:
        led.toggle()
        last_blink = ticks_ms()
    elif led.value() == 1 and time_since >= 500:
        led.toggle()
        last_blink = ticks_ms()


# Instantiate the Sensor class
sensor = Sensor(i2c = I2C(0, scl=Pin(5), sda=Pin(4)))


def read_sensor_data():
    """Read dictionary of sensor data"""
   # sensor.LED = True

    # Get all channel data from the sensor
    channel_data = sensor.all_channels
  #  sensor.LED = False

    CHANNEL_NAMES = [
        "ch410",
        "ch440",
        "ch470",
        "ch510",
        "ch550",
        "ch583",
        "ch620",
        "ch670",
    ]

    # Return a dictionary that maps channel names to sensor data
    return dict(zip(CHANNEL_NAMES, channel_data))


print("Testing sensor...")
sensor_data = read_sensor_data()
print(sensor_data)


# Description: Receive commands from HiveMQ and send dummy sensor data to HiveMQ

connectWiFi(SSID, PASSWORD, country="CA")

# To validate certificates, a valid time is required
ntptime.timeout = 5  # type: ignore
ntptime.host = "time.google.com"
try:
    ntptime.settime()
except Exception as e:
    print(f"{e} with {ntptime.host}. Trying again after 5 seconds")
    sleep(5)
    try:
        ntptime.settime()
    except Exception as e:
        print(f"{e} with {ntptime.host}. Trying again with pool.ntp.org")
        sleep(5)
        ntptime.host = "pool.ntp.org"
        ntptime.settime()

print("Obtaining CA Certificate from file")
with open("hivemq-com-chain.der", "rb") as f:
    cacert = f.read()
f.close()

# SSL parameters for secure MQTT connection
ssl_params = {
    "server_side": False,
    "key": None,
    "cert": None,
    "cert_reqs": ssl.CERT_REQUIRED,
    "cadata": cacert,
    "server_hostname": HIVEMQ_HOST,
}


# Dummy function for running a color experiment
def run_color_experiment(R, Y, B):

    # set_color(R, Y, B)
    sensor_data = read_sensor_data()
    print(sensor_data)
    # clear_color()

    return sensor_data


# MQTT Topics, not used in LCM
command_topic = f"{COURSE_ID}/request"

# my_id = hexlify(machine.unique_id()).decode()

# MQTT Topics
command_topic = f"command/picow/{PICO_ID}/as7341/read"
sensor_data_topic = f"color-mixing/picow/{PICO_ID}/as7341"

print(f"Command topic: {command_topic}")
print(f"Sensor data topic: {sensor_data_topic}")


def mqtt_callback(topic, msg):
    """Callback function to handle incoming MQTT messages"""
    try:
        topic = topic.decode()
        msg = msg.decode()
        print((topic, msg))

        if topic == command_topic:
            # Parse the incoming message as JSON
            incoming_dict = json.loads(msg)
            command = incoming_dict["command"]

            # Extract the RGB values from the command
            R = command["R"]
            Y = command["Y"]
            B = command["B"]

            # Run the color experiment with the specified RGB values
            sensor_data = run_color_experiment(R, Y, B)

            # Combine the sensor data with the original command
            payload_data = incoming_dict.copy()
            payload_data.update({"sensor_data": sensor_data})

            # Convert the payload data to a JSON string
            payload = json.dumps(payload_data)

            # Publish the payload to the sensor data topic
            client.publish(sensor_data_topic, payload)
            print("sensor results published")

    except Exception as e:
        with StringIO() as f:  # type: ignore
            sys.print_exception(e, f)  # type: ignore
            print(f.getvalue())  # type: ignore


# Create MQTT client
client = MQTTClient(
    PICO_ID,
    HIVEMQ_HOST,
    user=HIVEMQ_USERNAME,
    password=HIVEMQ_PASSWORD,
    keepalive=3600,
    ssl=True,
    port=8883,
    ssl_params=ssl_params,
)

# Set the callback and connect
client.set_callback(mqtt_callback)

try:
    client.connect()
    print("Connected to MQTT broker")
except OSError as e:
    print(f"MQTT connection failed: {e}. Retrying in 5 seconds...")
    sleep(5)
    try:
        client.connect()
        print("Connected to MQTT broker on retry")
    except OSError as e2:
        print(f"Second connection attempt failed: {e2}")
        raise

# Subscribe to command topic
client.subscribe(command_topic)
print(f"Subscribed to {command_topic}")

print("")
print("Waiting for experiment requests...")
print("")

sign_of_life(onboard_led, True)  # Initialize sign_of_life

# Main loop to check for messages
try:
    while True:
        try:
            client.check_msg()
            sign_of_life(onboard_led, False)
        except OSError as e:
            print(f"Error: {e}. Reconnecting...")
            try:
                connectWiFi(SSID, PASSWORD, country="CA")
                client.connect()
                client.set_callback(mqtt_callback)
                client.subscribe(command_topic)
            except Exception as reconnect_error:
                print(f"Reconnection failed: {reconnect_error}")
                sleep(5)
finally:
    client.disconnect()
