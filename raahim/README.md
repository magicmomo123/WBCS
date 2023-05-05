￼
Raahim Azeem Worklog
## February
2/5 
Objective: Work on Charging Subcirucit schematic
Got schematic design help regarding the charging of the PCB with Jason. Decided on using the MC3P chip to charge the battery itself. We decided that this would be a useful because it also included a stat pin that checked when the battery power is low. This pin could then be used to send a message to the microcontroller and we could have some kind of indiciation for when the battery is running low on the PCB.

2/10 
Objective: Consult with Olga regarding ECE related topics for our project
Talked with Professor Mironenko about possible solutions for AM radio reception. She is supplying us with some material from ECE 210 to assist us in our search. We learned that AM radio definitely is great for long distance communication which is definitely one of the things we wanted especially in espionage discrete communication scenarios.

2/15 
Objective: Determine what hardware to use for the project. More research on components, Looking through datasheets, etc.
Decided on using Wifi instead of bluetooth and AM radio. Couple of reasons for this decision. First AM antenna's must be half or fourth of the center frequency, even with a coiled antenna, it would be much too large for fitting into a mouth. Second, wifi allows for more precise control of audio communication. We also have found a microcontroller that it small enough to fit into the mouth while still having capability for communication. We have chosen to use the ESP32C# N4, which has a size of about 10 x 10 mm. Now, we wil start work on our schematic.
    
2/21
Objectives: Get first consultation for Design Review Ethics and Safety session
Talked to Dr. Shilpa for consultation regarding safe materials that can be used to design the PCB. Learned about PMMA, accrylic material, and mouth molds to demonstrate how the PCB would fit into the mouth. 

2/23
Objective: Create Schematic I was responsible for
Finished the schemtic for the device with inspiration from the ESP32 C3 devkit. Working on PCB.
Decided on using the MAX98 for our DAC as we decided to go with the ESP32Wroom for implementation. This chip is simple for integration for our subsystem as a whole and fits our size requirements as well.
The Transducer we are using is a basic model which just has two wires that need to be connected to the output pins of the MAX98 to complete the circuit and vibrate accordingly to the signal being played over the DAC.

2/25
Objective: complete Design Board Review
The team met together to work on the design review.

## March
3/17
Objectives: Learn about how we can create molds to implement our object in the mouth for the future
Visit to East Bay Dental. There we learn about creating mouth molds and software we can use to create invisalign like encasings that can be clipped on the teeth. After this meeting we used puddy to creates indentations of our upper jaw. After that we used a material called stone to fill up the indentation to create the mold. An image of this mold is attached to the notebook.

3/28
Received first order of the PCB to implement our project.

## April
4/1
Objective: Solder PCB for first set of tests. 
Upon completion of the PCB, we realized that there was a problem in the design for the pcb that prohibits us from flashing the esp 32 when the USB is connected. Because of the current protection to the PCB, we cannot boot the ESP when the USB is conencted.
We learned that the PMOS gate is turned off that allows the USB connection to the ESP32 when the PCB is plugged in to prevent 5V going directly to the PCB. We learn that because of this flashing onto the ESP is impossible. Have to go back to design and fix the error.

4/5
Objective: Redesign PCB regarding last error
Redesign for the PCB completed and files sent to Vishal for fabrication order. We created an addition wire route to allow for the chip to be enabled and turned on while the USB-C is plugged into the laptop.

4/15
Objective: Start working on PCB
After soldering we determined that there was still another error on the PCB regarding the charging subcircuit. In addition we decided to slighlty increase the size of the PCB to make sure we have more room to solder and reduce the chance of soldering error.

4/23
Objectives: Start soldering components for PCB and setup for tests.
Received third pcb. 
Due to many complication, our last PCB was delivered 3 days before the demo. Had to quickly solder on all the components of the PCB. Due to the very small size soldering components was a very meticulous and extensive job as there was not much room for error. We ran into issue that our USB-C was clipping the edge of the PCB due to a last minute design change for the third order. To solve this had to saw off the edge of the USB-C charger to plug into the PCB itself.
Next, we had an issue where the laptop was not recognizing that the PCB was plugged in. This meant that we could not get the laptop to download code to the chip. To get around this we decided to manually solder the TX RX pins and attach them to wires and plug it into the breadboard. On the other end we plugged in a USB-UART to the breadboard to boot up the PCB. After this we were able to recognize the PCB as a device, but we were still struggling to download the code onto the PCB. We got the PCB charging subcircuit to charge up the battery using the ELO to see current flow between the batteries.

4/24
Objectives: Continue Debuggin PCB
To debug this issue we had to determine what was wrong on the PCB. Initially, we thought there may have been an issue with the soldering on the device as it was very small and a component may simply not be soldered on correctly. After closely analyzing whether the components were active using an oscilloscope. (We basically tested if voltage was applied to each component) we determined that everything was soldered properly other than the buttons. The buttons were questionable because the contacts were not exactly matching the PCB grooves so we decided to manually solder a few more wires to the PCB and plug it into the breadboard. The PCB however, was still not booting up. We measured the pins on the oscilliscope to measure the voltage drop when buttons pressed to make sure it was matching the download sequence of the ESP-32. The buttons were reacting the way the pins should be for the download sequence. We then determined that another pin that is meant to be permanently pulled up (GPIO8) was actually pulled down on the PCB using the oscilliscope. We looked at the PCB design and realized that we had mistakenly made it a pull down pin instead of a pull up. To fix this issue we had to manually solder a resistor from the 3v3 source to the GPIO8 pin to keep it at high. This fixed our initial issue of having to download the code. The arduino IDE was no showing that we were flashing code onto the ESP.

4/25
Objectives: Continue Debugging PCB
After having flashing the code to the ESP, we were still having issued with the PCB working. We quickly realized that the ESP kept on looping its launch sequence and saw that it kept on enabling itself. This made it so that the device could not function as the microcontroller was in a perpetual loop of turning on and off. We quickly learned that one of the error messages we were receiving was called "browning out". After research and guidance from the Head TA, Jason, we learned that browning out is a relatively common error and is primarily caused by an influx of current drawn into the ESP. This causes the ESP to in turn turn itself off to prevent itself from corrupting its own data and burning out. After testing out a few software solutions found online. Main one being that we can just turn off the check on the ESP manually using a command to stop the rebooting sequence if the system starts to brown out. We decided that this would be fine as we are using a 3.3 volt battery and there should never be a dangerous amount of current being fed to the esp32. This got us to another resetting error. After more research we learned that it may be the Wifi Module drawing too much current. When we just decided to boot up the esp with no code we ended up turning on the chip. However, this is virtually useless as we cannot demonstrate that it works. After more research online we learned that all these brownout and reset issues were caused when people were using linear regulators. Our PCB also happened to use one to prevent any damage done to the PCB if something with higheer power was ever delivered to the PCB. We decided to remove the linear regulator, then proceeded to connect the PCB directly to one of the power sources in the lab at exactly 3.3 volts. This time the PCB both flashed the code onto the chip and booted up. After this we were able to send data over to the PCB and relay it to the transducer to play the same audio signal that was sent over WiFi. We determined that this was a success.


4/26 
Demo Day for out PCB

## May
5/1
Objective: Work on Presentation
Created presentation for class

5/2
Presented project to Vishal and Professor Fliflet
