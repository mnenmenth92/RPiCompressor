import RPi.GPIO as GPIO

from config import (
    pwm_pin,
    pwm_freq
)
class GPIODriver():
    pin = pwm_pin
    frequency = pwm_freq

    # configure and initialize PWM
    def __init__(self):
        self.status = False
        self.duty_cycle = 100
        # pwm init
        self.gpio = GPIO
        self.gpio.setmode(GPIO.BOARD)  # set GPIO mode to BOARD
        self.gpio.setup(GPIODriver.pin, GPIO.OUT)  # PWM pin set as output
        self.pwm = self.gpio.PWM(GPIODriver.pin, GPIODriver.frequency)  # initialize PWM

    # start pwm or updates duty cycle if already running
    def set_pwm(self):
        if not self.status:
            self.pwm.start(self.duty_cycle)
        else:
            self.pwm.ChangeDutyCycle(self.duty_cycle)
        self.status = True

    # stops PWM
    def stop_pwm(self):
        self.pwm.stop()
        self.status = False


    # cleans up gpio - to be used before app close
    def cleanup_gpio(self):
        self.stop_pwm()
        self.gpio.cleanup()

