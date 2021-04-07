import sensor

sensorPattern = "Source: {} - Value: {}"

sensorData = sensor.readSensor()

print(sensorPattern.format(sensorData["source"], sensorData["value"]))
