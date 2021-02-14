import RPi.GPIO as GPIO
from time import sleep

servoPin = 4

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servoPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPin, False)
    pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

pwm=GPIO.PWM(servoPin, 50)
pwm.start(0)

setAngle(90)

pwm.stop()
GPIO.cleanup()

