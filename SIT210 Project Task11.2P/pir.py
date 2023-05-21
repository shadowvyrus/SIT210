from gpiozero import MotionSensor
import time
import thingspeak
import time
from datetime import datetime
import requests

channel_id = 2155295
write_key = 'JXXE070KU9NC5YGD'

pir = MotionSensor(16)
state = 0
#print(pir.motion_detected)

def measure(channel):
    try:
        print(pir.motion_detected)
        if(pir.motion_detected==True):
            state=1
        else:
            state=0
        response = channel.update({'field1': state})
    except:
        print('Connection Failure')


if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        time.sleep(5)
