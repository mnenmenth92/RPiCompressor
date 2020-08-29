from gpio_driver import GPIODriver
from analog_input import AnalogInput
from rpi_compressor import RpiCompressor
from config import pressure_check_time_interval
from time import sleep

gpio_driver = GPIODriver()
analog_input = AnalogInput()
rpi_compressor = RpiCompressor(analog_input, gpio_driver)







if __name__ == '__main__':
    try:
        # ToDo run flask server
        # TEMPORARY
        while True:
            rpi_compressor.manage_pressure()
            sleep(pressure_check_time_interval)

    except AttributeError:
        pass
    finally:
        gpio_driver.cleanup_gpio()
