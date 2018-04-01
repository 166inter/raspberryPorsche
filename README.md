# raspberryPorsche

![](https://github.com/166inter/raspberryPorsche/blob/master/raspberryPorsche.jpg?raw=true)



## Version 1 build:

This current build is not using cameras yet. However, it will be possible to control the car with a laptop keyboard and collect input data. Once the system is up and running with a camera, the input key and camera data can be used together to train a neural network for the car to run autonomously (eg. behavioral cloning or line following). OpenCV can be used to have the camera detect traffic signs. That is easier said than done, but becoming simpler as machine learning packages like Tensorflow and Keras become more accessible.

Hardware used:

* Raspberry Pi Model 3
* [Porsche Spyder RC car](https://www.amazon.de/gp/product/B00TYV74Z0/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)*
* 6 male to female jumper wires
* USB C cable

Tools:
* Soldering iron
* Screw driver

Up and running:

1. Open up the RC controller that came with your car
1. Solder the 6 male ends of the wires onto the board (1 on VCC, 1 on GND, 2 for each set of pads for forward and reverse)
1. Connect the female ends to the appropriate pins on the Pi (see https://pinout.xyz/)
1. Install Raspbian Jessie (or your OS of preference) on the Pi
2. Set up WiFi on the Pi
3. Use VNC viewer to log into the Pi
4. Run the AutonomousX.X.X.py script

Dependencies:
* rpi GPIO
* pygame
* VNC viewer

Reference material:
https://pinout.xyz/



*The price has gone up on this car since I bought it, you probably could find a cheaper RC car that does the same trick

More to come soon! :) Next, I want to use openCV to do some object detection and mount the Pi directly to the car. Also, I could get a much cleaner system if I solder the cables directly to the car itself rather than go through the RC transmitter. It might work with a MOSFET power control kit. Also, This project could be adapted on a raspberry pi zero or another microcontroller with all the necessary functionality like an esp32.

If you have any questions, do not hesitate file an issue and I will be happy to help you get your own project working. Alternatively, I can be reached at nchlsschmidt@gmail.com.
