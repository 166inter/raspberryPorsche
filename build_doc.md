To do: </br>
<s>fix threadding so that it stops when you press x (return preset state keeps triggering)</s> </br>
<s>fix file csv file log (currently creating file but not populating)</s>

# Build Update April 19, 2018
-got log working
-need to optimize code, eliminate while loops, etc
-get camera working simultaneously with AutonomousX.X.X

# Build Update April 16, 2018

After reading more of the picamera advanced recipes docs, it looks like it is possible do image processing without needing to store the images on the disk. This may prove very useful gived the micro sd card's limited storage capacity. 

The image capturing code will have to be combined with the AutonomousX.X.X.py code to control the car using the input images. Currently, the directional commands (left, forward-left, forward, reverse, etc) are printed in the terminal when the script is run. However, this input should be logged in a file to use as training data. Similarly, the camera stream images should also be logged in a folder. In order to match the images with the input commands, time stamps can possibly be used.

# Build Update April 15, 2018

I only had a few hours today to work on this project out of the whole weekend. There are several options when deciding on a camera streaming/capture setup. 'Motion' is one of them; RPi-Cam-Web is another. PiCamera also has some built-in tools for capturing a sequence of images, allowing the user to set the frame rate, start and end time, and more. The resources/ code found on the raspberry pi stack exchange looks like a good start. In order to get the camerea stream working at the lowest possible latency, there is some useful information to follow in the picamera docs in section 5 (advanced recipes). Also it is important to note that if motion is installed, it needs to be manually deactivated before using raspistill, and other built-in camera modules.

# Build Update Apil 13, 2018

The power arrangement is not perfect, but working well enough to start to develop other parts of the car. 

The order of today was to begin setting up the camera so that it can be used to gather driving data as well as be used when running on a trained model. It is critical that the camera is synchronized with the timing of the keyboard/control inputs, otherwise, the model might learn to drive according to the asynchronous input and stop working if the synchronization changes.

# Build Update April 11, 2018

Looks like part of the problem was a loose ground wire. Some fresh Alkaline AA batteries were purchased today and installed. Upon first attempt with the raspberry pi 3, a significant improvement was noticed. But after swapping to the pi zero, the motors started acting sluggish again. 

When each of the idividual data-in ports are tested with one the pi's 5v output pin, the motors seem to work fine. But if both motors are used at the same time, they become sluggish. It seems like the problem lies in the output of the pi zero.

# Build Update April 10, 2018: Power and integration challenges
![](https://github.com/166inter/raspberryPorsche/blob/master/images/power_troubleshoot.jpg?raw=true)
*Troubleshooting in attempt at getting both the L298N and Pi to run off of the original 5 x 1.5V AAs*

Because space is limited inside the plastic Porsche 918 shell, I would like to power the Raspberry Pi and the motor controller both with the original 5 1.5V AA batteries mounted underneath the car. At the top of the above image is an Elego 545043 power supply. Since knowledge of how to do this is limited and  it is not critical (besides saving the weight of two more batteries), this can be left to tackle later. 

Today, the main goal was to power the controller with the AAs and using the powerbank I have to power the Pi separately (see image below). Because there is not much space, the batteries were popped out of the original case. 
![](https://github.com/166inter/raspberryPorsche/blob/master/images/integration.jpg?raw=true)
*Deciding on the interior layout. To achieve better weight distribution, the rechargeable batteries could be separated and put on either side of the motor controller. However, It is not necessary at this stage*

Currently, the servo motors are not working at full power, which is what needs to be inspected next.

More to come soon :)


