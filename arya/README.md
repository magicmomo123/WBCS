# Arya Worklog


## February 

2/10
Talked with Professor Mironenko about possible solutions for AM radio reception. She is supplying us with some material from ECE 210 to assist us in our search. 

2/15
Decided on using Wifi instead of bluetooth and AM radio. Couple of reasons for this decision. First AM antenna's must be half or fourth of the center frequency, even with a coiled antenna, it would be much too large for fitting into a mouth. Second, wifi allows for more precise control of audio communication. We also have found a microcontroller that it small enough to fit into the mouth while still having capability for communication. We have chosen to use the ESP32C# N4, which has a size of about 10 x 10 mm. Now, we wil start work on our schematic. 

2/25

Finished the schemtic for the device with inspiration from the ESP32 C3 devkit. Working on PCB. 

## March 

3/7

PCB design finished and sent to vishal for development. 

3/28 

Received first PCB and all components. 


## April 


4/1 

Upon completion of the PCB, we realized that there was a problem in the design for the pcb that prohibits us from flashing the esp 32 when the USB is connected. Because of the current protection to the PCB, we cannot boot the ESP when the USB is conencted. We need to slightly redesign to fix this problem .

4/5 

Redesign completed and sent to vishal 

4/21 

Second redesign completed, includes capability for power switching, and many broken out pins for debugging as well as LED for testing. 

4/29 

Received third pcb, working on completion. 

## May

5/1

Finished PCB, with some components broken out on the the breadboard because of soldering issues, issues with incorrect footprint geometry, etc. Ready for demo. 
