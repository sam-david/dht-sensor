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


date = datetime.datetime.now(tz=pytz.utc)
pst_date = date.astimezone(timezone('US/Pacific'))

print(pst_date,humidty, temp)
with open('tempHumidityStats.csv','a') as fd:
    fd.writerow(['Test', "tw"])
