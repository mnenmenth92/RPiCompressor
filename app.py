from gpio_driver import GPIODriver
from analog_input import AnalogInput
from rpi_compressor import RpiCompressor
from config import pressure_check_time_interval
from time import sleep
from flask import Flask
from flask import render_template

gpio_driver = GPIODriver()
analog_input = AnalogInput()
rpi_compressor = RpiCompressor(analog_input, gpio_driver)

app = Flask(__name__)

@app.route('/Pressure')
def index():
    return render_template('pressure.html',
                           current_pressure=analog_input.current_value,
                           target_pressure=rpi_compressor.pressure_limit)



if __name__ == '__main__':
    try:
        app.run(debug=True)
        # ToDo check how to run while loop along with flask server
        while True:
            rpi_compressor.manage_pressure()
            sleep(pressure_check_time_interval)

    except AttributeError:
        pass
    finally:
        gpio_driver.cleanup_gpio()
