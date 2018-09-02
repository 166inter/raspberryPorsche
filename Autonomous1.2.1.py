#!/usr/bin/env python

#special thanks to kamalraghav81 for helping me out with classes and threading!

import RPi.GPIO as GPIO
import threading, queue, random
import sys, tty, termios
from pygame import *
from time import *


init()
screen = display.set_mode((640, 480))
display.set_caption('The amazing key presser!')


forward_pin = 5
reverse_pin = 6

left_pin = 24
right_pin = 23
light_pin = 21

headlight_toggle = "OFF"

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup([forward_pin, reverse_pin, left_pin, right_pin, light_pin], GPIO.OUT)

q = queue.Queue(maxsize=10)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



class RemoteControl:
    """
        Motion control interface for RC car
    """

    def __init__(self):

        """
         send preset commands to remote
        """
        print("Setup/Initialize.")
        global q

    def forward(self):
        """
        Move forward
         GPIO commands to move forward
        """

        print("Move Forward")
        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(reverse_pin,  GPIO.HIGH)

    def reverse(self):
        """
        Move forward
         GPIO commands to move forward
        """

        print("Go Back")
        GPIO.output(forward_pin, GPIO.HIGH)
        GPIO.output(reverse_pin, GPIO.LOW)

    def right(self):
        """
        Move forward
         GPIO commands to move forward
        """

        print("Turn Right")
        GPIO.output(left_pin, GPIO.HIGH)
        GPIO.output(right_pin, GPIO.LOW)

    def left(self):
        """
        Move forward
         GPIO commands to move forward
        """

        print("Turn Left")
        GPIO.output(left_pin, GPIO.LOW)
        GPIO.output(right_pin, GPIO.HIGH)

    def forward_left(self):
        print("Go Forward-Left")
        GPIO.output(left_pin, GPIO.LOW)
        GPIO.output(right_pin, GPIO.HIGH)       

        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(reverse_pin,  GPIO.HIGH)

    def forward_right(self):
        print("Go Forward-Right")
        GPIO.output(left_pin, GPIO.HIGH)
        GPIO.output(right_pin, GPIO.LOW)

        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(reverse_pin,  GPIO.HIGH)

    def reverse_left(self):
        print("Go Reverse-Left")
        GPIO.output(left_pin, GPIO.LOW)
        GPIO.output(right_pin, GPIO.HIGH)

        GPIO.output(forward_pin, GPIO.HIGH)
        GPIO.output(reverse_pin,  GPIO.LOW)

    def reverse_right(self):
        print("Go Reverse-Right")
        GPIO.output(forward_pin, GPIO.HIGH)
        GPIO.output(reverse_pin, GPIO.LOW)

        GPIO.output(left_pin, GPIO.HIGH)
        GPIO.output(right_pin, GPIO.LOW)

    def preset(self):
        """
            send preset data
        """
        GPIO.output(left_pin, GPIO.HIGH)
        GPIO.output(right_pin, GPIO.HIGH)
        GPIO.output(forward_pin, GPIO.HIGH)
        GPIO.output(reverse_pin, GPIO.HIGH)
        print("Sending default command")

    def run(self):
        """
            run parallel thread to send commands
        """
        thread = threading.Thread(target=worker)
        thread.start()

def worker():
    print("thread at work")
    remote = RemoteControl()
    while True:
        if q.empty():
            #sleep(.1)
            remote.preset()
        else:
            new_key = q.get()
            q.task_done()
            if new_key == 'a':
                remote.left()
                #sleep(.1)
            elif new_key == 'd':
                remote.right()
                #sleep(.1)
            elif new_key == 'w':
                remote.forward()
                #sleep(.1)
            elif new_key == 's':
                remote.reverse()
                #sleep(.1)
            elif new_key == 'aw':
                remote.forward_left()
            elif new_key == 'dw':
                remote.forward_right()
            elif new_key == 'as':
                remote.reverse_left()
            elif new_key == 'sd':
                remote.reverse_right

if __name__ == "__main__":
    remote = RemoteControl()
    remote.run()

    while True:
        #rand = random.uniform(0, 5)
        keys = ([key.get_pressed()[K_a],key.get_pressed()[K_d],  
        key.get_pressed()[K_w], key.get_pressed()[K_s]])
        
    
    if key.get_pressed()[K_l] == 1:
        if headlight_toggle == "ON":
            print("headlights off")
            headlight_toggle = "OFF"
            GPIO.output(headlight_pin, GPIO.LOW)
            
        else:
            print("headlights on")
            headlight_toggle = "ON"
            GPIO.output(headlight_pin, GPIO.HIGH)
            
    
        print(keys)     

        if keys == [1,0,0,0]:
            q.put('a')
        elif keys == [0,1,0,0]:
            q.put('d')
        elif keys == [1,0,1,0]:
            q.put('aw')
        elif keys == [0,1,1,0]:
            q.put('dw')
        elif keys == [0,0,0,1]:
            q.put('s')
        elif keys == [0,0,1,0]:
            q.put('w')
        elif keys == [0,1,0,1]:
            q.put('sd')
        elif keys == [1,0,0,1]:
            q.put('as')
        event.pump()
    print('More to come, soon!!!')

                                        


