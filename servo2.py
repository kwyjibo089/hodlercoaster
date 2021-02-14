import RPi.GPIO as GPIO
from time import sleep

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)

pwm=GPIO.PWM(4, 50)
pwm.start(0)

setAngle(35)

pwm.stop()
GPIO.cleanup()

