"""
This was originally the test code from the camjam 
CamJam EduKit 3 - Robotics

Worksheet 3 - Motor Test Code
you can access the CamJam code and resources from here: 
https://camjam.me/?page_id=1035
"""

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from guizero import App, PushButton
from time import sleep

Speed = 0.3

def move_forward():
    robot.forward(Speed)

def move_backward():
    robot.backward(Speed)

def move_right():
    robot.right(0.9)
    
def move_left():
    robot.left(0.9)

def stop():
    robot.stop()

robot = CamJamKitRobot()

app = App()

Forward_button = PushButton(app, command=move_forward, text="forward")
Forward_button.width = 20
Forward_button.height = 10

Left_button = PushButton(app, command=move_left, text="Left")
Left_button.width = 20
Left_button.height = 10

back_button = PushButton(app, command=move_backward, text="Backward")
back_button.width = 20
back_button.height = 10

right_button = PushButton(app, command=move_right, text="Right")
right_button.width = 20
right_button.height = 10


Stop_button = PushButton(app, command=stop, text="Stop")
Stop_button.width = 20
Stop_button.height = 10

app.display()

