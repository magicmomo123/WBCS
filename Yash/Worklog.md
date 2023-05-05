# Yash Worklog

## February

### 2/10
Spoke with Professor Mironenko about solutions for AM radio reception. Did research on how to implement AM radio reciever.

Issues with the AM recieiver include the demodulator which will take up a significant amount of poweer as well as the large antenna required. Further research is required. Look into loop antennas possibly. 

## 2/12

Brainstormed various communication protocols from bluetooth low energy to fm radio. FM radio obviously seems unviable, but we want long range connectivity how can this be done if AM radio takes up such a large amount of power. Only solution is having an intermediatry device such as a cell phone which can connect to propietry long range communication network such as LTE.

## 2/15

Both WiFi and RF (radio frequency) are wireless communication protocols, but there are some key differences between them.

WiFi is a wireless networking technology that uses radio waves to provide high-speed wireless internet and network connections. WiFi operates on specific frequency bands (usually 2.4GHz or 5GHz) and can provide data rates ranging from a few megabits per second (Mbps) to several gigabits per second (Gbps). WiFi has several advantages over RF, including:

Higher data rates: WiFi can provide much higher data rates than RF, which is particularly important for applications that require high-speed data transmission, such as video streaming, online gaming, and file transfers.

Greater range: WiFi has a longer range than RF, which means that it can cover larger areas and provide connectivity to devices that are further away from the access point.

More secure: WiFi has built-in security features that help to protect against unauthorized access and eavesdropping, which is particularly important for applications that involve sensitive data or require high levels of security.

Greater reliability: WiFi uses error-correcting techniques to ensure that data is transmitted accurately, which can help to prevent data loss or corruption.

More flexibility: WiFi can support a wide range of devices, including smartphones, tablets, laptops, and IoT devices, and can be used to create large-scale networks that can support a wide range of applications and services.

## 2/20

After doing further research we settled on using esp 32 mainly because it is a  popular choice for edge devices that require wireless connectivity. Some advantages of using the ESP32 for WiFi communication in edge devices include:

Low cost: The ESP32 is relatively inexpensive compared to other microcontrollers with built-in WiFi, making it an affordable option for edge devices.

Low power consumption: The ESP32 is designed to operate at low power levels, making it suitable for battery-powered edge devices.

Dual-core processor: The ESP32 has a dual-core processor, which allows it to perform multiple tasks simultaneously, such as running a WiFi connection while also processing sensor data.

Built-in security features: The ESP32 includes a range of security features, including support for encryption, secure boot, and secure flash, which helps to protect against unauthorized access and data breaches.

Easy to program: The ESP32 can be programmed using the Arduino IDE or the ESP-IDF (ESP32 IoT Development Framework), making it easy to develop and deploy applications.
Aurdino IDE makes it the perfect choice for us due to ease of progarmming.

## 2/25
Consultation with dentist. We decided to settle on one material that has proven to be quite useful in electrical applications in the mouth which is PMMA, which stands for polymethyl methacrylate. PMMA is a type of plastic that has several advantages when it comes to dental and medical applications.

Firstly, PMMA is considered safe to use because it doesn't react with the tissues in the mouth or cause any negative effects. This means it can be used without posing any risk to the patient's health. Additionally, PMMA is transparent, which allows for easy visualization of the underlying tissues and components. This is especially helpful when working in the oral cavity, where visibility can be limited.

## 2/28
The first coefficient that needs to be calculated is the voltage gain coefficient. This determines how much the input voltage is amplified by the circuit. It is calculated by dividing the output voltage by the input voltage.

The second coefficient is the input impedance coefficient. This determines how much the circuit resists the flow of current from the input source. It is calculated by dividing the input voltage by the input current.

The third coefficient is the output impedance coefficient. This determines how much the circuit resists the flow of current to the output load. It is calculated by dividing the output voltage by the output current.

To calculate these coefficients, you need to use the relevant equations and plug in the values for the components in the circuit. Once you have calculated the coefficients, you can use them to determine the optimal values for the components to achieve the desired amplification gain.



## 3/1
I realized that type A amplifiers are not actually so advantagoeous. 
One major disadvantage of a basic type A amplifier is its low efficiency, as it operates in Class A mode all the time, even when there is no signal to amplify. This means that it draws a constant amount of power from the power supply, which results in a significant amount of wasted power and heat dissipation. As a result, the amplifier can become quite hot, and may require additional cooling to prevent damage.

Another disadvantage of a basic type A amplifier is its limited output power capability, as it can only output as much power as the power supply can provide. This means that it may not be suitable for driving high-power loads or for applications that require high output power.

Additionally, a basic type A amplifier can be sensitive to temperature variations, as changes in temperature can cause changes in the biasing of the output transistor, which can affect the amplifier's performance. This can lead to distortion and other issues.

Overall, while a basic type A amplifier may be simple and easy to design, its low efficiency, limited output power, and sensitivity to temperature variations make it less suitable for many applications.

## 3/5
Noticed that type A amplifier has some severe disadntaves, One major disadvantage of a basic type A amplifier is its low efficiency, as it operates in Class A mode all the time, even when there is no signal to amplify. This means that it draws a constant amount of power from the power supply, which results in a significant amount of wasted power and heat dissipation. As a result, the amplifier can become quite hot, and may require additional cooling to prevent damage.

Another disadvantage of a basic type A amplifier is its limited output power capability, as it can only output as much power as the power supply can provide. This means that it may not be suitable for driving high-power loads or for applications that require high output power.

Additionally, a basic type A amplifier can be sensitive to temperature variations, as changes in temperature can cause changes in the biasing of the output transistor, which can affect the amplifier's performance. This can lead to distortion and other issues.


Another advantage of PMMA is that it is easy to work with. It can be shaped and molded into a variety of sizes and shapes, making it highly versatile for different dental and medical applications. This means it can be used to encase different types of electrical components, such as sensors, transducers, or even small motors.
Finally, PMMA is relatively inexpensive compared to other materials used for similar purposes, which makes it a cost-effective solution for dental and medical practitioners.

## 3/7 
Finished some of the circuit design.

## 3/11

I recently underwent a dental impression procedure to obtain a mold of my upper palate. The dentist began by providing me with an impression tray containing a viscous, water-based substance called alginate. Alginate is a hydrocolloid material that is commonly used to create dental impressions due to its ability to quickly form a stable mold.

The alginate was inserted into the impression tray, and I was instructed to place it into my mouth, making sure to bite down firmly on it. The alginate material flowed into the contours of my teeth and gums, forming a negative impression of my dental arches. The material was left to set for a few minutes until it had solidified, and the dentist carefully removed the tray from my mouth.

The negative impression was then used to create a positive plaster cast of my upper palate. The cast was filled with dental stone, which hardened and formed an exact replica of my dental arches. This replica was then used to create a custom dental appliance or restoration, tailored specifically to my oral anatomy.
This mold is then to be used to create a custom fit for the BCDC for each individauls mouth, all in all good progress.


## 3/28
Worked on the devkit to make sure the I could code the esp to connect to some local host to play some audio.
First, I made sure that all of the necessary libraries were installed on my system, including the ESP32-Arduino Core and the audio.h library. The ESP32-Arduino Core provides the basic functionality required to work with the ESP32, while the audio.h library provides the necessary tools for working with audio data.

Next, I started a new Arduino sketch and used the #include directive to include the required libraries. This directive tells the Arduino IDE to include the necessary files at the beginning of the sketch.

To connect to my local host, I set up a Wi-Fi connection by providing my network's SSID and password. This allowed my ESP32 to connect to my Wi-Fi network and access the Internet.

After that, I initialized the audio output by setting the sample rate, bit depth, and number of channels. The sample rate determines the number of samples per second that are played back, while the bit depth determines the resolution of the audio data. The number of channels determines whether the audio is mono or stereo. I also set up the buffer size for the audio data, which determines how much data is stored in memory before being played back.

Next, I created a client object to connect to my local host using its IP address and port number. The IP address is a unique identifier assigned to each device on a network, while the port number determines which specific service or application is being accessed.

Finally, I used a while loop to continuously read audio data from my local host and play it through the ESP32's audio output. Within the while loop, I used the client object to read data from my local host and store it in a buffer. Once the buffer was full, I played back the audio data using the audio.h library. This process continued indefinitely until the connection was closed or the sketch was stopped.

## 4/4
Today i worked on sending the audio data from the local host connction with audio.h to my transducer. Sufferened one issue where for some reason I could not program the boared with my own computer so had to use my partners computer.
To go over the steps I did, 
First, I made sure that I had the necessary libraries installed, including the ESP32-Arduino Core and the i2s.h library.
Then, I started a new Arduino sketch and included the required libraries using the #include directive.
Next, I initialized the I2S interface by setting the sample rate, the number of bits per sample, and the number of channels. I also specified the GPIO pins that would be used for the I2S interface.
After that, I created a buffer to hold the audio data that would be sent to the I2S DAC.
Finally, I used a while loop to continuously read audio data from a file or a sensor and write it to the I2S buffer, which would in turn send the data to the I2S DAC through the specified GPIO pins.
By doing this, I was able to use the i2s.h library to connect the ESP32's GPIO pins to an I2S DAC and play audio through an external speaker or headphones.


## 4/15
Today I worked on the https post requests with Arya and sending data back from the esp32 to the computer. I used an ESP32 microcontroller to collect data from an analog sensor using the built-in ADC pins. I needed to send this data to a computer using an HTTP POST request.
First, I made sure that I had the necessary libraries installed, including the ESP32-Arduino Core, and the ADC.h library.
Next, I initialized the ADC by setting its resolution, sampling rate, and voltage range. Then, I configured the GPIO pins to be used as ADC input channels.
After that, I created an HTTP client object to connect to the computer and send the data. I specified the server address, port number, and URL to which the data should be sent.
Then, I started a loop to read the ADC value and send it using an HTTP POST request. I also included headers in the request to specify the content type and length of the data.
Finally, I closed the HTTP client connection and waited for a certain amount of time before starting the loop again to collect and send more data.
Unfortunately the data was noisey and useless because the adc on the esp32 is trash.

## 4/23
Worked on soldering the first breadboard as well as the ADC test but with very limited success unfortunately I was not able to bring either task to valdiity, the soldering was helped by kevin but even then soldiering wires to all of the chips outputs was simply too hard. It was a tough day but we will make progress I am 100% sure.

## 4/24
We kept finding more and more issues with the ESP unfortunately there were pins that were not soldered correctly but eventually we figured out there is a download sequence that must be followed. 
We eventually read the internet and did the following,The ESP32 is powered on or reset, and it enters the bootloader mode. The bootloader is a small piece of software that is built into the ESP32's flash memory.

The bootloader waits for a download request from the host computer, usually through a USB cable.

The host computer sends a download request to the ESP32 bootloader using a tool such as esptool.py or the Arduino IDE.

The ESP32 bootloader responds to the download request by sending an acknowledgement to the host computer.

The host computer sends the new firmware or code to the ESP32 bootloader in binary format over the USB connection.

The ESP32 bootloader receives the binary data and writes it to the ESP32's flash memory.

Once the download is complete, the ESP32 bootloader verifies the firmware or code and resets the ESP32.

The ESP32 starts running the new firmware or code from the beginning of the flash memory.
We were able to succesfuly program the breadboard version of the ESP.

## 4/25 Continue debugging
So, we were working with an ESP32 microcontroller and we needed to regulate the voltage coming from my power supply to a stable 3.3 volts. We had decided to use a linear regulator to do this.
At first, everything seemed to be working fine. But as we started to increase the load on the ESP32, we noticed that it was drawing more current than I had anticipated. This caused the voltage coming from the regulator to drop below 3.3 volts, which in turn caused the ESP32 to brown out.
We realized that the linear regulator was not able to handle the current demands of the ESP32. This was because a linear regulator works by dissipating excess voltage as heat, and as the load on the regulator increased, so did the amount of heat it was producing. Eventually, the regulator became too hot and was unable to maintain a stable voltage output.
What we did was short the regulator and we got succesful funtionality on the esp.

## Afterwards to finish,
Worked on the presentation, the demo and redied our tests for showing the viability of our product.
