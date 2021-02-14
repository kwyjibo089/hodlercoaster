#!/usr/bin/env python3
#-- coding: utf-8 --
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


GPIO.setwarnings(False) #Disable warnings

#Use pin 4 for PWM signal
pwm_gpio = 4
frequence = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_gpio, GPIO.OUT)

pwm = GPIO.PWM(pwm_gpio, frequence)

#Init at 90°
pwm.start(angle_to_percent(90))
time.sleep(1)
pwm.stop()
time.sleep(5)

#Go at 120°
pwm.ChangeDutyCycle(angle_to_percent(120))
time.sleep(1)
pwm.stop()
time.sleep(5)

#Go at 70°
pwm.ChangeDutyCycle(angle_to_percent(70))
time.sleep(1)
pwm.stop()
time.sleep(5)

#Go back to 90
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)
pwm.stop()
time.sleep(5)



#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()
