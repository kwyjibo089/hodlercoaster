#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

def moveTo (angle) :
    pwm.start(angle_to_percent(angle))
    time.sleep(0.5)
    #Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()

GPIO.setwarnings(False) #Disable warnings

#Use pin 4 for PWM signal
pwm_gpio = 4
frequence = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_gpio, GPIO.OUT)

pwm = GPIO.PWM(pwm_gpio, frequence)

