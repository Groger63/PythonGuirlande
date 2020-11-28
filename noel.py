
from time import sleep
import RPi.GPIO as GPIO
import time
import random

red = 18
blue = 2
green = 3
yellow = 4

colors = [red,blue,green,yellow]

def initSensors() :
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(red, GPIO.OUT)
	GPIO.setup(yellow, GPIO.OUT)
	GPIO.setup(blue, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)

def switchLight(number) :
        GPIO.output(number, not  GPIO.input(number))
        return GPIO.input(number)

try:
    initSensors()

    while True:
        sleep(1)
        colorsOn = 0
        for color in colors :
            if random.randint(2,3) == 3 :
                colorsOn += switchLight(color)
        if colorsOn == 0 :
            switchLight(colors[random.randint(1,len(colors)-1)])

except KeyboardInterrupt:
    print("Goodbye")
    for color in colors :
        GPIO.output(color, 0)
    sleep(1)
    GPIO.cleanup()
