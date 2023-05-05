# Arya Worklog


## February 

2/10
Talked with Professor Mironenko about possible solutions for AM radio reception. She is supplying us with some material from ECE 210 to assist us in our search. 

2/15
Decided on using Wifi instead of bluetooth and AM radio. Couple of reasons for this decision. First AM antenna's must be half or fourth of the center frequency, even with a coiled antenna, it would be much too large for fitting into a mouth. Second, wifi allows for more precise control of audio communication. We also have found a microcontroller that it small enough to fit into the mouth while still having capability for communication. We have chosen to use the ESP32C# N4, which has a size of about 10 x 10 mm. Now, we wil start work on our schematic. 

![image](https://user-images.githubusercontent.com/80484261/236363802-96d56ef6-3177-4cab-acfa-b0ad756d3159.png)  
<br>

Updated Block Diagram  
<br>


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

![image](https://user-images.githubusercontent.com/80484261/236362622-5926ef11-b2cc-488a-a95a-f1c616b738b7.png)
  
  Going with a design like this- should be pretty close to our final iteration hopefully.  
  

![image](https://user-images.githubusercontent.com/80484261/236364208-6c5de33c-1e65-4b47-a13c-2fac6b5b1202.png)  

Made transducer circuit.   


### PCB Issues (across iterations)

Ran into DRC issues when making the PCB. Thought I had enough grounding holes scattered and everything was wired as expected, but turns out there were zones that were not grounded since they were isolated from the rest of the board by traces. The warning and errors were not helpful in figuring this out.

While soldering the PCB, we ran into several issues. In hindsight, it would have beeen most effective to send the board and components for machine soldering given the size of our PCB. We anticipated having a challenge soldering, but it was much tougher than expected, especially since the oven was not working in a predictable manner. Instead, I designed a stencil that could be used to cover the right components with paste, and then heat the board up with the components on. 

Appyling the paste turned out to be harder than expected, and some of the paste in the fridge was not good at melting and connecting the components as intended. It was also hard to verify whether certain connections were accurately being made. Since our board was so small, we also had to take care to not lose extremely tiny capacitors and resistors that were incredibly difficult to hand-solder. 

At this point, I am thinking it might be easier to completely pivot and make the design a proof of concept with larger components since there still might be time. This way, we could verify whether certain systems and components are working as anticipated. Also it would be nice to check if our software and PCB design is accurate. 

The USB C connector was also hard to solder because of the pin design. Found out from some other groups and students that it is possible to flash the ESP by simply connecting the wires to individual ports. Ordered a connector on amazon that could power and flash the ESP conveniently. 
![image](https://user-images.githubusercontent.com/80484261/236362445-ed2d5cab-4dfe-48f4-8a85-dbcad461101d.png)
Connector schematic

Definitely going to use a micro usb or just go with the direct wire connectors in future. 


4/5 

Redesign completed and sent to vishal 

4/21 

Second redesign completed, includes capability for power switching, and many broken out pins for debugging as well as LED for testing. 

4/29 

Received third pcb, working on completion. Soldering was easier here since it was possible to do by hand. Was able to verify ESP32 connections and boot correctly. 
Had issues when trying to boot and flash the ESP32 that likely stemmed from power circuit stuff. Without rosin, it would have been much more challenging to solder the small components onto the PCB, and I likely would have had to deal with cold solder joints or other issues.  

![image](https://user-images.githubusercontent.com/80484261/236362525-479eb3d8-2f20-47f7-96bc-f9e1c4871755.png)
  
  Standard ESP32 setup that allowed for easy booting.   


when I was trying to debug my ESP32 on the PCB after it received a brownout error. Checked the power circuit to ensure that they were providing the required voltage levels.Checked for any power loss issues such as bad solder joints, damaged traces, or faulty components. Ended up fixing it after some faulty wiring led to inconsistnet voltages. 

![image](https://user-images.githubusercontent.com/80484261/236360332-27598976-a623-4cba-bbee-0abf6f2f250f.png)
  
  Final PCB design that ended up working.   
  


## May

5/1

Finished PCB, with some components broken out on the the breadboard because of soldering issues, issues with incorrect footprint geometry, etc. Ready for demo. Raahim helped fix a lot of things in the end; it was super helpful. 

During demo shorted the voltage regulator to somehow get the ESP32 to boot. In the moment, let us finish whatever we needed to. Huge relief. 


### Testing images and verifications:
![image](https://user-images.githubusercontent.com/80484261/236363413-34777fd6-c3b4-4b14-9dab-c4b00b5f8a41.png)
  
  Sampled audio STFT  
  

![image](https://user-images.githubusercontent.com/80484261/236363561-4010b4a1-f9aa-448d-a5a3-830d6855eef9.png)
  
  Battery Current Verification  
  


