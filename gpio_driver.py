import RPi.GPIO as GPIO

from config import (
    pwm_pin,
    pwm_freq,
    digital_outputs_dic
)
class GPIODriver():
    pin = pwm_pin
    frequency = pwm_freq

    # configure and initialize PWM
    def __init__(self):
        self.status = False
        self.duty_cycle = 100
        self.digital_outputs = digital_outputs_dic
        self.gpio = GPIO
        self.gpio.setmode(GPIO.BOARD)  # set GPIO mode to BOARD
        self.init_pwm()  # initialize pwm on pin selected in config.py
        self.init_do()  # initilaize digital outputs basing on config dictionary

    # pwm gpio initialization
    def init_pwm(self):
        self.gpio.setup(GPIODriver.pin, GPIO.OUT)  # PWM pin set as output
        self.pwm = self.gpio.PWM(GPIODriver.pin, GPIODriver.frequency)  # initialize PWM

    # set digital outputs basing on config dictionary
    def init_do(self):
        for key in self.digital_outputs:
            self.gpio.setup(self.digital_outputs[key], GPIO.OUT)  # pin set as output
            self.set_do_value(key, 0)  # set low state
        pass

    # set digital output by name from configuration dictionary
    def set_do_value(self, do_name, value):
        try:
            do_num = self.digital_outputs[do_name]
            self.gpio.output(do_num, value)
        except:
            print('wrong digital output name')

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

