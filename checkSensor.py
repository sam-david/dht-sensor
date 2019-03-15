import Adafruit_DHT
import time
import datetime
from pytz import timezone
import pytz
import csv

sensor = Adafruit_DHT.DHT22
pin = 4

def read_sensor():
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    return { 'humidity': humidity, 'temp': temp }

def write_to_csv(humidity, temp):
    fields = [humidity, celsius_to_fahrenheit(temp), current_time()]
    with open('tempHumidityStats.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(fields)

def current_time():
    date = datetime.datetime.now(tz=pytz.utc)
    pst_date = date.astimezone(timezone('US/Pacific'))
    return pst_date

def celsius_to_fahrenheit(degrees):
    (9.0/5.0) * degrees + 32


sensor_data = read_sensor()
write_to_csv(sensor_data['humidity'], sensor_data['temp'])
