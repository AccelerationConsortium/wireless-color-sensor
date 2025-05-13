import time
from machine import I2C, Pin
from as7341_sensor import Sensor

# Initialize the AS7341 sensor
sensor = Sensor(i2c=I2C(0, scl=Pin(5), sda=Pin(4)))

try:
    while True:
        # Turn on the LED
        sensor.LED = True
        print("LED is ON.")
        time.sleep(3)  # Keep LED on for 3 seconds

        # Turn off the LED
        sensor.LED = False
        print("LED is OFF.")
        time.sleep(3)  # Keep LED off for 3 seconds

except KeyboardInterrupt:
    # Handle manual interruption gracefully
    print("\nProgram interrupted by user.")

finally:
    # Ensure LED is off before exiting
    if sensor.LED:
        print("Turning off the LED before exiting.")
        sensor.LED = False
    print("Program terminated.")