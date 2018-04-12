# Build Update April 11, 2018

Looks like part of the problem was a loose ground wire. Some fresh Alkaline AA batteries were purchased today and installed. Upon first attempt with the raspberry pi 3, a significant improvement was noticed. But after swapping to the pi zero, the motors started acting sluggish again. 

When each of the idividual data-in ports are tested with one the pi's 5v output pin, the motors seem to work fine. But if both motors are used at the same time, they become sluggish. It seems like the problem lies in the output of the pi zero.

# Build Update April 10, 2018: Power and integration challenges
![](https://github.com/166inter/raspberryPorsche/blob/master/power_troubleshoot.jpg?raw=true)
*Troubleshooting in attempt at getting both the L298N and Pi to run off of the original 5 x 1.5V AAs*

Because space is limited inside the plastic Porsche 918 shell, I would like to power the Raspberry Pi and the motor controller both with the original 5 1.5V AA batteries mounted underneath the car. At the top of the above image is an Elego 545043 power supply. Since knowledge of how to do this is limited and  it is not critical (besides saving the weight of two more batteries), this can be left to tackle later. 

Today, the main goal was to power the controller with the AAs and using the powerbank I have to power the Pi separately (see image below). Because there is not much space, the batteries were popped out of the original case. 
![](https://github.com/166inter/raspberryPorsche/blob/master/integration.jpg?raw=true)
*Deciding on the interior layout. To achieve better weight distribution, the rechargeable batteries could be separated and put on either side of the motor controller. However, It is not necessary at this stage*

Currently, the servo motors are not working at full power, which is what needs to be inspected next.

More to come soon :)


