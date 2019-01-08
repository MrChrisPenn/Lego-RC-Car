"""
This was originally the test code from the camjam 
CamJam EduKit 3 - Robotics has been extended by Chris Penn

Worksheet 3 - Motor Test Code
you can access the CamJam code and resources from here: 
https://camjam.me/?page_id=1035
"""

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from guizero import App, PushButton, Picture, Text
from time import sleep

Speed = 0.3

def move_forward():
    print("Forward")
    robot.forward(Speed)

def move_backward():
    print("Backward")
    robot.backward(Speed)

def move_right():
    print("Right")
    robot.right(0.9)
    
def move_left():
    print("Left")
    robot.left(0.9)

def stop():
    print("Stop")
    robot.stop()

robot = CamJamKitRobot()

app = App(title="Lego RC GUI v2", width=230, height=400, layout="grid")

Title = Text(app, text="Lego RC 2.0",grid=[1,0])
Logo = Picture(app, image="lego.png",grid=[1,2])


Forward_button = PushButton(app, text="Forward", command=move_forward,grid=[1,3])
Forward_button.width = 5
Forward_button.height = 5

Stop_button = PushButton(app, text="Stop", command=stop,grid=[1,4])
Stop_button.width = 5
Stop_button.height = 5

Left_button = PushButton(app, text="Left", command=move_left,grid=[0,4])
Left_button.width = 5
Left_button.height = 5

back_button = PushButton(app, text="Back", command=move_backward,grid=[1,5])
back_button.width = 5
back_button.height = 5

right_button = PushButton(app, text="Right", command=move_right,grid=[2,4])
right_button.width = 5
right_button.height = 5


app.display()
