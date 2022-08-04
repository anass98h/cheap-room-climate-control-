
from time import sleep_ms, ticks_ms, ticks_diff
from machine import Pin, I2C
from dth import DTH
import utime
import pycom
import machine
from mqtt import MQTTClient
from network import WLAN
import time

# Wireless network
WIFI_SSID = "Mi"
WIFI_PASS = "65yryr9999"


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "65yryr"
AIO_KEY = "aio_bzPW21cqKB6QuVBrcYgvsm0QmyQP"
AIO_TEMP_FEED = "65yryr/feeds/temp"
AIO_humidity_FEED = "65yryr/feeds/humidity"
AIO_working_FEED = "65yryr/feeds/working"
# RGBLED
# Disable the on-board heartbeat (blue flash every 4 seconds)
# We'll use the LED to respond to messages from Adafruit IO
pycom.heartbeat(False)
time.sleep(0.1) # Workaround for a bug.
                # Above line is not actioned if another
                # process occurs immediately afterwards
pycom.rgbled(0xff0000)  # Status red = not working

# WIFI
# We need to have a connection to WiFi for Internet access
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html

wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)

while not wlan.isconnected():    # Code waits here until WiFi connects
    machine.idle()

print("Connected to Wifi")
pycom.rgbled(0xffd7000) # Status orange: partially working
time.sleep(3)

pycom.heartbeat(False)

#diffinging pins to the sensors
motionsensor = Pin('P23', mode = Pin.IN)
th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)

RANDOMS_INTERVAL = 5000 # milliseconds
last_random_sent_ticks = 0  # milliseconds
last_time = ticks_ms() # save current time
delay = 2
tem = 0 # temperature
hum = 0 # humidity


def send_temp(): #sending temp and var to adafruit
    global last_random_sent_ticks
    global RANDOMS_INTERVAL
    global tem
    global hum
    if ((time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL):
        return; # Too soon since last one sent.
    else:
        try:
            client.publish(topic=AIO_TEMP_FEED, msg=str(tem))
            client.publish(topic=AIO_humidity_FEED, msg=str(hum))
            print("DONE")
        except Exception as e:
            print("FAILED")
        finally:
            last_random_sent_ticks = time.ticks_ms()



def tempo():  # measering the humidity and temperature
    global tem
    global hum
    th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
    result = th.read()
    if result.is_valid():
        tem = result.temperature
        hum = result.humidity
    print(tem)
    print(hum)


print("Starting Detection...")


client = MQTTClient("65yryr", AIO_SERVER,user = AIO_USER,password= AIO_KEY, port = AIO_PORT)
client.connect() # connecting to adafruit

def status(): # checking and alerting if the room is too hot or too humied
    global tem
    global hum
    if tem >= 28 or tem <= 17:
        pycom.rgbled(0x7f0000)
    elif hum >= 50 or hum <= 20:
        pycom.rgbled(0x7f0000)
    else:
        pycom.rgbled(0x007f00)


while True: # the main loop
    if motionsensor() == 1: # if motion is dedected
        print("YES")
        tempo()
        send_temp()
        status()
        client.publish(topic=AIO_working_FEED, msg="YES")

    else:
        client.publish(topic=AIO_working_FEED, msg="NO")
        status()
        print("NO")

    time.sleep(2)
