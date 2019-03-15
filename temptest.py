import Adafruit_DHT
import time
import datetime
from pytz import timezone
import pytz
import csv

sensor = Adafruit_DHT.DHT22
pin = 4

def read_sensor():
    humidty, temp = Adafruit_DHT.read_retry(sensor, pin)
    return { 'humidty': humidty, 'temp': temp }

def write_to_csv(humidy, temp):
    fields = [humidty, temp, current_time()]
    with open('tempHumidityStats.csv','a') as fd:
        fd.write(['Test', "tw"])

def current_time():
    date = datetime.datetime.now(tz=pytz.utc)
    pst_date = date.astimezone(timezone('US/Pacific'))
    return pst_date


sensor_data = read_sensor()
write_to_csv(sensor_data['humidty'], sensor_data['temp'])
