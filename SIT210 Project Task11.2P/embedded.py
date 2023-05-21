from gpiozero import MotionSensor
import adafruit_dht
from board import *
import time
import thingspeak
import time
from datetime import datetime
import requests

channel_id = 2156965
write_key = '0D0IIA9SR151XR9G'

# Initialisation for PIR Sensor
pir = MotionSensor(16)
state = 0

# Initialisation for DHT22
SENSOR_PIN = D4
dht_device = adafruit_dht.DHT22(SENSOR_PIN, use_pulseio=False)
humidity = dht_device.humidity
temperature = dht_device.temperature

# Function to take measurements from sensors
def measure(channel):
    try:
        if humidity is not None and temperature is not None:
            print("Temp = {0:0.1f}C Humidity = {0:0.1f}%".format(temperature,humidity))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('Time is: ', current_time)
        else:
            print('Failed to retrieve data from DHT sensor')

        if(pir.motion_detected==True):
            state=1
        else:
            state=0

        response = channel.update({'field1': temperature, 'field2': humidity, 'field3':state})
    except:
        print('Connection Failure')




# Main loop

if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        time.sleep(10)