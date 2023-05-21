import thingspeak
import adafruit_dht
from board import *
import time
from datetime import datetime
import requests
# r = requests.post('https://maker.ifttt.com/trigger/{temperature_trigger}/with/key/{6Aqi2Pq9eLMbew3A5izqH}', params = {"value1": "temperature"} )

# Thingspeak Channel related details
channel_id = 2153782
write_key = 'Q64UOI1XZOEX304R'

# Initialising components
SENSOR_PIN = D4
dht_device = adafruit_dht.DHT22(SENSOR_PIN, use_pulseio=False)
humidity = dht_device.humidity
temperature = dht_device.temperature
print('Temperature and humidity output from DHT22 Sensor')
		
	
	
def measure(channel):
    try:
        if humidity is not None and temperature is not None:
            print("Temp = {0:0.1f}C Humidity = {0:0.1f}%".format(temperature,humidity))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('Time is: ', current_time)
        else:
            print('Failed to retrieve data from DHT sensor')
        response = channel.update({'field1': temperature, 'field2': humidity})
    except:
        print('Connection Failure')
            
        
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        time.sleep(15)
        
        
        
        
# Start a wihle loop so it repeatedly reads the data and prints it out to console
#while True:
#	if humidity is not None and temperature is not None:
#		print("Temp = {0:0.1f}C Humidity = {0:0.1f}%".format(temperature,humidity))
#		now = datetime.now()
#		current_time = now.strftime("%H:%M:%S")
#		print(current_time)
		#if(temperature > 27): r = requests.post('https://maker.ifttt.com/trigger/{temperature_trigger}/with/key/{6Aqi2Pq9eLMbew3A5izqH}', params = {"value1": "temperature"} )
#	else:
#		print("Failed to retrieve data from DHT sensor")
#	time.sleep(15)
        
        
        
        
        