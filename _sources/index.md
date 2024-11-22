# Getting started guide for wireless color sensor

## Overview 

This documentation provides a guide to assemble and test a color sensor package with a dual wireless charging port that could be implemented to the OT-2 liquid handling robot. 

   <div style="text-align: center; margin-top: 10px;">
      <img src="_static/images/Wireless-color-sensor-in-OT-2.png" width="500">
  </div>

<br>
Following is a video of liquid color matching demo run on OT-2 with this wireless color sensor:

(Video link to be added)

The estimated time of the hardware assembling is:

<br>

## Prerequisites

This documentation assumes that readers have completed [Course 1: Hello World](https://ac-microcourses.readthedocs.io/en/latest/courses/hello-world/index.html#) and possess basic knowledge of electronic soldering and wiring techniques.
<br>

## Bill of materials

### Electronic parts: 

  - **Sensor Package:**

    <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Electronic-parts-sensor.png" width="500">
    </div>

    - [<span class="color-red">① PicoW</span>](https://www.digikey.com/en/products/detail/raspberry-pi/SC0919/18713315)
    - [<span class="color-blue">② Pico LipoSHIM</span>](https://www.digikey.com/en/products/detail/pimoroni-ltd/PIM557/15851380)
    - [<span class="color-magenta">③ AS7341 color sensor</span>](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4698/13162109)
    - [<span class="color-orange">④ Picowbell P5905</span>](https://www.digikey.com/en/products/detail/adafruit-industries-llc/5905/22596390)
    - [<span class="color-purple">⑤ STEMMA QT Wire</span>](https://www.digikey.com/en/products/detail/sparkfun-electronics/PRT-17258/13629029)
    - [<span class="color-green">⑥ Wireless charger receiver</span>](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/317010008/5487684)

    - [<span class="color-yellow">⑦ Lipo battery with 2-pole JST connector wire</span>](https://www.amazon.ca/EEMB-Battery-Rechargeable-Lithium-Connector/dp/B08FD3V6TF/)

    - [<span class="color-cyan">⑧ 1 Pin male connector jumper wires (2x)</span>](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4482/11594500)

   <br style="clear: both;"> 

  - **Wireless charging port (Dual charging):**

    <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Electronic-parts-charging.png" width="500">
    </div>

    - [<span class="color-red">① Wireless charger transmitters (2x) </span>](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/113030020/5487569)
    - <span class="color-orange"> ② Mirco-USB to USB Type-A cables ([1 short](https://www.amazon.ca/gp/product/B073PQWY2B/) and [1 long](https://www.digikey.ca/en/products/detail/stewart-connector/SC-2AMK003F/8544577)) </span>
    - [<span class="color-blue">③ Power supply (5V 2A) </span>](https://www.digikey.ca/en/products/detail/xp-power/VEL05US050-US-BB/5023710)
   
    <br style="clear: both;"> 

:::{Note}
 **Qi wireless charging:**
 The wireless charging modules linked above comply with the [Qi standard](https://en.wikipedia.org/wiki/Qi_(standard)), providing a consistent power output of 5V/500mA within an effective distance of 2-8mm. However, they are relatively more expensive.
:::

:::{Note}
 **Alternative:**
 One lower-cost alternative is [this inductive charging set](https://www.adafruit.com/product/1459), which requires a 9V power supply. Note that its output is less efficient and inconsistent, varying based on the power input and charging distance. Additionally, it lacks electromagnetic shielding and USB ports, which may require more advanced electronic knowledge to configure.
:::


### 3D printed parts: 

  - **Sensor package:**

     <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Printed-parts-sensor.png" width="500">
     </div>

    - <span class="color-red">① Microcontroller backboard</span>
    - <span class="color-orange">② Sensor stand</span>
    - <span class="color-blue">③ Sensor package main enclosure</span>
    
    <br style="clear: both;"> 

  <br>

  - **Wireless charging port:** 

     <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Printed-parts-charging.png" width="500">
     </div>

    - <span class="color-red">① Enclosure A side</span>
    - <span class="color-orange">② Enclosure B side</span>
    - <span class="color-blue">③ Base board</span>
    - <span class="color-magenta">④ Transmitter supports (2x) </span>

    <br style="clear: both;"> 

  All the 3D printing files can be found in [this link](https://github.com/Neil-YL/wireless-color-sensor/tree/07829dd6418d59315a7711e57d3ba6ff898b8a76/CAD-File/STEP). If your 3D printer is Bambu Lab series, [project files](https://github.com/Neil-YL/wireless-color-sensor/tree/c080448a7fcbc0e26ace216282e9614ede66aa17/CAD-File/BamBu-File) are available for BambuStudio.

:::{Hint}
Print the sensor package and the charging port enclosure with light-color material so that the LED indicators could be visible from the outsides.
:::

### Mechanical components and tools: 

  - **Mechanical components:**

     <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Mechanical-Components.png" width="500">
     </div>

    - <span class="color-red">① M2.5-10mm screws (4x)</span>
    - <span class="color-orange">② M2.5 hex nuts (4x)</span>
    - <span class="color-blue">③ Painter's tape</span>

    <br style="clear: both;"> 

 <br>

  - **Tools required:**

     <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Tools-required.png" width="500">
     </div>

    - <span class="color-red">① Phillips-head #0 screwdriver</span>
    - <span class="color-blue">② Soldering set</span>
  
  
  <br style="clear: both;"> 

 <br>

  - **Tools nice to have:**

     <div style="float: right; margin-left: 10px; width: 500px;">
      <img src="_static/images/Tools-nice-to-have.png" width="500">
     </div>

    - <span class="color-red">① Tools to remove 3D printing supports and deburr surface</span>
    - <span class="color-blue">② Multimeter for electronic connection troubleshooting</span>

  <br style="clear: both;"> 
 
## Hardware assembly

  ### Preparation / Before you begin assembling: 

  #### 3D printed parts preparation:

   Remove all printing supports from the 3D-printed parts. Deburr all the supported surfaces and edges, especially following highlighted areas that will be used for assembly.

  :::{hint}
  <span style="padding-left: 10px;">Use wirecutters to remove most of the supports from the printed parts.</span>  
  <span style="padding-left: 10px;">Clean up remaining spikes with sharp utility knives or scissors.</span>
  :::

   - <span class="color-red">inner walls of the sensor package</span> and <span class="color-orange">those of the charging port enclosure A/B</span>

  <div style="text-align: center; margin-top: 10px;">
    <img src="_static/images/inner-wall.png" style="width: 500px;">
  </div>

  <br>

   - <span class="color-blue">sliding slots</span> on the sensor enclosure and <span class="color-blue">tips</span> on the controller backboard.

  <div style="text-align: center; margin-top: 10px;">
    <img src="_static/images/Sliding-slots.png" style="width: 500px;">
  </div>

 <br>

   You may also test the fit between the sensor enclosure and the pipette on the OT-2. Polish as needed until it achieves a similar fit shown in the photo.


  <div style="text-align: center; margin-top: 10px;">
    <img src="_static/images/Fitting-of-pipette.png" style="width: 400px;">
  </div>

 
   <br>

  #### Electronic parts soldering:
   
  1. **LipoSHIM:** 

     Place the LipoSHIM on the back of the PicoW, ensure <span class="color-red">the power button</span> of the LipoSHIM and <span class="color-blue">the micro-USB port</span> on the PicoW are on the same side.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/PicoShim-soldering-1.png" style="width: 500px;">
     </div>

     <br>
     
     Solder <span class="color-orange">8 pins on each row</span> on the PicoW.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/PicoShim-soldering-3.png" style="width: 500px;">
     </div>
     
     <br>

     You may connect the PicoW to a micro-USB power supply and use the power button to check the soldering connection; <span class="color-red">the white LED indicator</span> on the LipoSHIM should light up.
     
     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/PicoShim-power-check.png" style="width: 500px;">
     </div>
     
     
  <br>

  
  2. **Battery connnector:**
     
     If you are working with the battery from the link provided in BOM section or if <span class="color-blue">the polarity of your battery</span> 2-pin JST connector is opposite to <span class="color-red">that of the LipoSHIM</span>:

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Battery-soldering-1.png" style="width: 500px;">
     </div>

     :::{warning}
      Never connect your battery to PicoSHIM with wrong polarity!
     :::
      
     <a id="battery-connector"></a>
     You can correct it by cutting off the connector, swapping the wires, and then resoldering them to match the correct polarity.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Battery-soldering-2.png" style="width: 500px;">
     </div>

<br>

  3. **Wireless charging unit:** 

     Solder a jumper wire to <span class="color-red">the C1+ (or C2+) pad</span> and another to <span class="color-blue">the GND pad</span> on the receiver board.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Receiver-soldering-1.png" style="width: 500px;">
     </div>     

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Receiver-soldering-2.png" style="width: 500px;">
     </div>   

     <br>

     Connect the transmitter to a power supply via micro-USB port and place the receiver on top of the transmitter (coils faced with coils). Check if <span class="color-blue">the blue LED charging indicator</span> on the transmitter board lights up. You may use a multimeter to measure the voltage between the two jumper wires; the reading should be approximately 5V.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Receiver-soldering-3.png" style="width: 500px;">
     </div>      


  #### Dual charging connection check:

   You may also check the connection of the dual wireless charging setup before start assembling. Use the short micro-USB/USB Type-A cable to connect two transmitters and connect the transmitter that has a free micro-USB port to a power supply. Test the receiver with the same procedure above for the wireless charging unit, the receiver should give a voltage reading of approximately 5V on each transmitter.

   <div style="text-align: center; margin-top: 10px;">
      <img src="_static/images/Dual-charging-test.png" style="width: 500px;">
   </div>      
  
  <br>
      
  ### Assembling:

  #### Sensor Package assembling:

  1. **Connect battery to Picow and LipoSHIM assembly:**
  
      Ensure the polarity of the battery matches the +/- markings on the LipoSHIM, if you are using the battery from the link provided in BOM section, [reverse the polarity](battery-connector) before connecting it to the LipoSHIM. 
     
     :::{warning}
       Never connect your battery to PicoSHIM with wrong polarity!
     :::

      Connect the battery to the LipoSHIM with <span class="color-blue">the JST connector</span>. Adjust the wires of the battery to through <span class="color-red">a row of pins</span> on the PicoW. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Battery-Picow-1.png" style="width: 500px;">
     </div>   
    
     <br>

      Test connection: Press the button on the LipoSHIM to power on the PicoW; <span class="color-blue">the white LED indicator</span> on the LipoSHIM should light up. Connect the PicoW to a power supply via the micro-USB port; <span class="color-red">the red LED charging indicator</span> on the LipoSHIM should also light up. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Battery-Picow-2.png" style="width: 500px;">
     </div>   

     <br>

      Power off and disconnect the power supply before proceeding with following steps.

  2. **Mount PicoW on Picowbell:** 
  
      Place the PicoW on the top of the Picowbell sockets; <span class="color-red">the micro-USB port</span> on PicoW should be at the same side as <span class="color-blue">the STEMMA QT port</span> on Picowbell.  

      <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Picow-Picowbell-1.png" style="width: 500px;">
     </div>   

     <br>     

     Carefully align the pins and press down the PicoW to secure it onto the Picowbell.

   :::{hint}  
   Since the power button on the PicoSHIM will interfere with the STEMMA QT port on the Picowbell, you don’t need to push the PicoW all the way down.
   :::

  3. **Connect wireless charging receiver to Picowbell:**
  
      Connect the GND jumper wire from the receiver to <span class="color-red">the GND socket</span> (third on the right, No.38) on the Picowbell. 
      
      Connect the C1+(or C2+) jumper wire to <span class="color-blue">the VBUS socket</span> (first on the right, No.40) on the Picowbell. 
      
      <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Picow-Pin-1.png" style="width: 750px;">
     </div>  

     <br> 

      Place the receiver on the powered transmitter, <span class="color-red">the red LED indicator</span> on LipoSHIM and <span class="color-blue">the blue LED indicator</span> on the transmitter should light up.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Receiver-Picowbell-1.png" style="width: 500px;">
     </div>   

     <br> 
 
  4. **Connect AS7341 to Picowbell:**

      Connect <span class="color-red">AS7341</span> to <span class="color-blue">Picowbell's STEMMA QT port</span> with a STEMMA QT wire. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/AS7341-Picobell-1.png" style="width: 500px;">
     </div>   

     <br>       
      Turn on the Picow (using the button on LipoSHIM), <span class="color-green">the green LED indicator</span> on AS7341 should light on.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/AS7341-Picobell-2.png" style="width: 500px;">
     </div>   

     <br>   

      Test the color sensor (software testing section)


  5. **Assemble Picowbell to the backboard:** 

      Align the assemble holes on Picowbell to those on the backboard, ensuring that <span class="color-red">the micro-USB port</span> on Picow is positioned on the side of <span class="color-blue">the backboard's opening slot</span>, adjusting the sensor cable to <span class="color-orange">one side within the case</span>. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/ Picowbell-to-backboard-1.png" style="width: 600px;">
     </div>   

     <br>   
      
      Insert <span class="color-red">the screws</span> through the holes on the Picowbell, position the nuts from <span class="color-blue">the back of the backboard</span>, and secure them with a screwdriver.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/ Picowbell-to-backboard-2.png" style="width: 600px;">
     </div> 

      :::{Hint}
      The positions of the nuts and screws can be swapped, but this method is generally easier for assembly.
      :::


  6. **Secure sensor stand to the main enclosure end:**
  
      The sensor stand is a thin board with four spikes, designed with a thinner edge and a thicker edge. Position the sensor stand with <span class="color-red">the thinner edge</span> at the opening side of the main enclosure and the spikes on the top. 
      
      <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/sensor-stand-to-main-1.png" style="width: 500px;">
     </div>   

     <br>   
      
      Insert it into the sensor end of the main enclosure. If the sensor stand is properly assembled, the spikes will be slightly higher than the surrounding flat surface.

      <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/sensor-stand-to-main-2.png" style="width: 500px;">
     </div>   

     <br>   

  7. **Secure the color sensor to the stand:** 
  
      Face down the AS7341, with <span class="color-red">the yellow square</span> on AS7341 close to opening of the main enclosure, align the assemble holes with four spikes, secure AS7341 to the stand.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/sensor-to-stand-1.png" style="width: 500px;">
     </div>   

     <br>   
  
     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/sensor-to-stand-2.png" style="width: 500px;">
     </div>   

     <br>   

      The yellow square on AS7341 should be visible from the hole of the sensor enclosure if the sensor is assembled properly.
    
     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/sensor-to-stand-3.png" style="width: 500px;">
     </div>   

     <br>   

:::{Note}
 If you would like to disassemble the sensor or sensor stand after assembly, use a tweezer(or a similar tool) to gently pry up one side of the sensor, then the other side, gradually lifting it out from four spikes. For the sensor stand, use a thin tool to push it up from the bottom. Be careful not to touch the central electronic components of the sensor during this process.
:::


  8. **Secure the receiver:**

     Prepare two pieces of painter’s tape, approximately 40mm long each. Place the wireless charger receiver on the inner wall of the enclosure, with the coils facing against the wall and the receiver board on the right, and secure with the painter's tape. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/receiver-to-main-1.png" style="width: 500px;">
     </div>   

     <br>   


  9. **Final Assembly of the Backboard and Main Enclosure：**

     Aligning the sliding tips on both ends of the backboard to the sliding slots on the main enclosure, adjusting all the wires within the enclosure, carefully assemble the backboard to the main enclosure. 
    
     <div style="text-align: center; margin-top: 10px; display: flex; justify-content: center;">
      <img src="_static/images/backboard-to-main-1.png" style="width: 400px; margin-right: 10px;">
      <img src="_static/images/backboard-to-main-2.png" style="width: 400px;">
     </div>

     <br>   
 
     **🎉 Congrats, your wireless color sensor is ready to go!**
    
     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/backboard-to-main-3.png" style="width: 500px;">
     </div>   

     <br>  

  #### Dual Charging port assembling:

  1. Join the A and B sides of the charging port enclosure, aligning them properly, and secure both parts together.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Port-A-B-1.png" style="width: 500px;">
     </div>   

     <br>  
 

  2. Plug the short micro-USB cable into <span class="color-red">the micro-USB port</span> on one transmitter.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-A-support-1.png" style="width: 500px;">
     </div>   

     <br>  

     Place the transmitter onto the transmitter support with the coils facing outward. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-A-support-2.png" style="width: 500px;">
     </div>   

     <br>

     Route the coils wires down from <span class="color-blue">the thinner edge</span> of the support. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-A-support-3.png" style="width: 500px;">
     </div>   

     <br>
     
     Insert the transmitter support with transmitter board into the port enclosure assembly. Then, secure it in place, ensuring there is no gap between the transmitter coils and the wall of the sensor slot.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-A-support-4.png" style="width: 500px;">
     </div>   

     <br>

:::{Hint}
 If there is a gap between the coils and the inner wall, or if the transmitter support bends significantly, consider polishing the walls for assembling to achieve a better fit.
:::

  3. Thread the long micro-USB cable through the square hole into the charging port assembly with the micro-USB head.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Long-usb-cable-1.png" style="width: 500px;">
     </div>   

     <br>

  4. Place another transmitter on the transmitter support with the coils facing outward. 
  
     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-B-support-1.png" style="width: 500px;">
     </div>   

     <br>  

     Route the coils wires down from the thicker side of the support through <span class="color-blue">the routing slot</span>. 

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-B-support-2.png" style="width: 500px;">
     </div>   

     <br>  

     Insert the transmitter support into the port enclosure assembly, leaving the transmitter board on the top. Secure the transmitter support in place, ensuring there is no gap between the transmitter coils and the wall of the sensor slot.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Transmitter-B-support-3.png" style="width: 500px;">
     </div>   

     <br>  

  5. Connect the short USB cable to the USB type-A port on the second transmitter. Connect the long micro-USB cable to the micro-USB port of the second transmitter. If you find any difficulties with cable connections, try swapping two transmitters to rearrange cable.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Cables-connection-1.png" style="width: 500px;">
     </div>   

     <br>  
        
  6. Connect the long cable to a power supply. The LED indicators on both transmitters should flash in the following sequence: blue; red; blue and red, and all off. If either indcator does not flash, you may check the cable connections.

     <div style="text-align: center; margin-top: 10px;">
       <img src="_static/images/Cables-connection-2.png" style="width: 500px;">
     </div>   

     <br>  


  7. Arrange the cables inside the enclosure and assemble the base board to the port enclosure. Place the sensor package on the slot of the charging port, the red indicator on the sensor package should light up.

     <div style="text-align: center; margin-top: 10px; display: flex; justify-content: center;">
      <img src="_static/images/Sensor-charging-1.png" style="width: 400px; margin-right: 10px;">
      <img src="_static/images/Sensor-charging-2.png" style="width: 400px;">
     </div>

     <br>   
## Software part


        



        

      


    


