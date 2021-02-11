import RPi.GPIO as GPIO
from time import sleep

servoPIN = 4

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(duty)


GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

setAngle(0)

setAngle(30)

setAngle(-30)

pwm.stop()
GPIO.cleanup()

