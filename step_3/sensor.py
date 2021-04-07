"""

sensor.py

Reading out sensor data

"""


def readSensor():
    # do something
    dataVolts = 10.4
    result = {
        "source": "voltage_sensor",
        "value": dataVolts,
    }
    return result


class Sensor:
    def __init__(self):
        self.sensorName = "sensor-01"

    def read_sensor(self):
        return {
            "source": self.sensorName,
            "value": 4.2,
        }