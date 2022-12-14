# cheap room climate control
cheap DIY room climate control with motion sensor
### Hallak mohamadanas - hm222ua
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/IMG_20220804_030602.jpg?raw=true)
The goal of this project is to make a cheap climate control with motion sensor that can double as security system
This IoT device will show if the room is too hot or too cold, or too humid by LED and if it's red you can check through the dashboard

Estimated time to complete: 30 min without a dashboard and 1,5h with dashboard

## Objective
why I choose to make this: it's because climate change is catching up with us fast, and we just had a brutally hot summer
in Sweden and it has affected my sleep a lot because the housing in Sweden is isolated for cold winters the air
the outside might be cold, but the apartment will keep the heat it stored in the morning
with the help of this device i can tell when I walk into the room if it's too room climate is suitable for sleep
if it's not i can view through the dashboard what's wrong and crack a window or turn on the humidifier


## Material
**list of what you need**

| Component                                                      | Count | Specification | Picture |
|---------------------------------------------|:-----:|:------|---------|
| LoPy4                                                          |   x1  |A micropython micro controller that have difference communication ways: <br>WIFI, LoRa, Sigfox, Bluetooth |<img src="imges/loby.jpg" width="auto" height="auto" />|
| Expansion board v3.1                                           |   x1  |Compatible with Pycom’s WiPy, LoPy, SiPy, FiPy, and GPy development boards. Needed to program and power the LoPy4 board.|<img src="imges/Expans.png" width="200" height="200" />|
| Micro USB cable                                                |   x1  |Allows you to connect to your micropython with computer for programming.|<img src="imges/micorusb.jpg" width="200" height="150" />|
| Breadboard                                                     |   x1  |A board wich you can make electical circuit without soldering|<img src="imges/breadboard.jpg" width="200" height="200" />|
| motion sensor (hc-sr501)                            |   x1  |motion sensor|<img src="imges/download%20(2).jpg" width="200" height="160" />|
| Digital temperature and humidty sensor (DHT-11 with integrated resistance) |   x1  |Read the temprature and humidty|<img src="imges/dht11.jpg" width="200" height="200" />|
All of parts can be found on amazon nothing exotic here so dont worry i got them all in 37sensor kit and it costed 40 doller ecept the LoPy4 and Expansion board v3.1 you can buy them dircatly from pycom.io for 50 dollars

## Computer setup
I'm used to VS code, but please **avoid** it. The plugin that's called PyMakr is fully broken at the time of publishing this tutorial. 

I wasted weeks trying to get it to work, not realizing it's broken, and after a lot of suffering, I realized that the plugin works on Atom 
sorry for the rant. I just needed to ensure that you (the person replicating this at home) didn't waste as much time as I did.

Now what you need to do is simple:

you start by installing [Atom](https://flight-manual.atom.io/getting-started/sections/installing-atom/) and Navigate to the Install page via Atom > Preferences > Install

Search for Pymakr and select the official Pycom Pymakr Plugin

you need this plugin to communicate with the pycom and upload your code 

If you have any problems installing it you can follow this [Guide](https://docs.pycom.io/gettingstarted/software/atom/)

Note that you might need to install dependencies programs like[Node.js](https://nodejs.org/en/download/) Atom will notify you if you need any on the bottom right corner of the screen. 


**Device firmware update**
if you are experiencing bugs or glitches, especially with the IoT environment, Adafruit. consider updating your firmware by following this guide [here](https://docs.pycom.io/updatefirmware/device/).


## Putting everything together

For this part of the tutorial, I will use the color of the cables to show what pin on each device do
When flowing this tutorial try to connect each device at the time and then put them together like legos I found that this is the easiest way


first the pycom
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/pycomirl.jpg?raw=true)

as you see there are four cables to connect to the pycom 

Red from VIN to + on Breadboard  

White from GND to - on Breadboard 

purple from P23 to middle pin on motion sensor

Black from P3 to left Pin on DHT 


DHT
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/dhtirl.jpg?raw=true)

there are three cables to connect in this step 

gray from the right pin to - on Breadboard 

white from the middle pin to + on Breadboard  

Black from left to P3 on the Pycom


motion sensor 
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/motionirl.jpg?raw=true)

there are three cables to connect in this step too

Gray from the left pin to - on Breadboard 

Blue from the right pin to + on Breadboard  

Purple from the middle pin on the motion sensor to P23 on Pycom


Breadboard 
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/powerirl.jpg?raw=true)

on the Breadboard, the cables come in pairs 

on the top, there are the Red to + and the white to - from the pycom

then there is the gray to - and white to + from DHT

last we have gray to - and Blue to + from the motion sensor 



**In case the readings from the motion sensor come back always high then switch the gray and blue cables**


This is still a development setup because I plan to add more functionality before the final deployment. Still, if you are satisfied with the functionality, I recommend making a small cardboard box.

You will need to cut two holes, one for the DHT and one for the motion sensor, and also few needle holes for the led to shine through



## platform 
For this project, I chose Adafruit.io because the dashboard will scale better for phone screens than other alternatives like datacake.co because I'm planning on deploying this device in the bedroom, and I will use the dashboard most often on the phone.

Adafruit.io is free and easy to implement thanks to their " in my opinion" excellent documentation. 

This is a cloud-based platform, so it doesn't store all the data for a long time, but I don't feel this will be a limitation in this case. 

If you plan on scaling this project up, you might need to pay for more data points per min and Unlimited dashboards.

If you choose to use [io.adafruit](https://io.adafruit.com/)
start by making a free account 

![image](https://user-images.githubusercontent.com/24983326/183108095-1e58fdb3-80b1-4043-81e1-04538c440ca9.png)

then you need to navigate to "feeds" and create three new Feeds, one for the temperature, one for humidity, and one for motion sensing. 

![image](https://user-images.githubusercontent.com/24983326/183108158-dc7f0460-1d27-48f6-b03b-22047405d7e2.png)

Next, you want to go to the dashboard tab and create a new dashboard. 

![image](https://user-images.githubusercontent.com/24983326/183108357-2640b715-156f-468c-8d7d-0b034c416f79.png)

Open your dashboard and click on the sitings icon on the top right side of the screen. Then from the menu, you need to click on  "Create New Block" here, and you can 

create a visualization. I chose two graphs for the temperature and humidity and the status indicator for the motion sensor.

But feel free to try other options to see what works best for you. Just make sure you connect it to the right feed.

My dashboard ended up looking like this:


![image](https://user-images.githubusercontent.com/24983326/183107946-7d1858dd-b5cf-401c-87f6-a97a0cca7cc6.png)

### The code 

You are alomst done !! 
you need to add your user name and key that can be found by clicking on the key botten

![image](https://user-images.githubusercontent.com/24983326/183109925-c631cf28-7ca2-40db-a198-05d86ebdfad6.png)


now you need to grap the url of the feeds you created and through them in the code:

```python=
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "65yryr"
AIO_KEY = "aio_bzPW21cqKB6QuVBrcYgvsm0QmyQP"
AIO_TEMP_FEED = "65yryr/feeds/temp"
AIO_humidity_FEED = "65yryr/feeds/humidity"
AIO_working_FEED = "65yryr/feeds/working"
```

Dont forget to change the wifi info too!!


## code


In this part of the tutorial, I will highlight features of the code that I think the end user might want to change 

I will start with the parameters that define when the led turns red 

```python=

def status(): # checking and alerting if the room is too hot or too humied
    global tem
    global hum
    if tem >= 28 or tem <= 17:
        pycom.rgbled(0x7f0000)
    elif hum >= 50 or hum <= 20:
        pycom.rgbled(0x7f0000)
    else:
        pycom.rgbled(0x007f00)

```
The "tem" variable is the one that define the temperture and its set by default between 28 and 17

The "hum" variable is the one that define the humitity  and its set by default between 50% and 20%



```python=
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
```

This function controls the behavior when detecting motion. It can be used to add functionality when motion is detected 

by default is sends YES and the temperature and the humidity value to adafruit io


## Transmeting the data/ connectivity

The data is sent every time motion is detected. You can adjust the delay in the motion sensor using the dials on the motion sensor.[Guide](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/)

For this project, I used wifi since its intended for indoor use, and I live far away from a city, and LoRa isn't available. 

Also, since this device is not meant to be moved one set up. 

The range of the wifi wasn't an issue, nor was the power consumption since it's meant to be connected to a power supply or a computer via USB 

MQTT protocol has been used to send the data since adafruit io has a ready to use library that was easy to implement you can find it on [their github page](https://github.com/adafruit/Adafruit_IO_Python)

I must mention that adafuit also supports REST API and has libraries ready for it. 

## Presenting the data
As mentioned before, I used io.adafruit because it scales nicely on a mobile screen.

For now, I have the temperature and humidity reading on a graph because I'm interested to see if there are any patterns throughout the day. Still, I might change it in the future for raw numbers for easier readability.

I have also outlined the process of changing how the dashboard looks earlier and i encourage you to play around with the different options to find what works the best for you.

![image](https://user-images.githubusercontent.com/24983326/183291148-b7236ef0-36af-4009-8895-257d1a61fa0f.png)

For a free account, the data is saved for 30 days, but if you upgrade your account, you can keep the data for 60 days.

As for me, I don't think that I will need data further than the 24 hours displayed on the dashboard graph.

But if you want to see all the data that is stored, you can refer to the feed tab 

## Finalizing the design
![alt text](https://github.com/anass98h/cheap-room-climate-control-/blob/main/imges/IMG_20220804_030602.jpg?raw=true)

This was an exciting project, and I was motivated to finish it since I was reminded of it every time I walked into the bedroom.

It might not be the prettiest device on earth, but I like the development look. I think it gives it more character than something bought in a store and leaves it open for more improvement in the future. I want to add a CO2 sensor when I find one for a reasonable price. 

Also, it would be nice to add some relays to control a small lamb through ada fruit one sad fact is that I learned that I couldn't trust the labels on the sensors.

I could only get them to work after some trial and error, and from want, I understand different sensors from the same manufacturer might have different pin layouts.

Also, if you plan on building an IoT device, plan where and how it will be used before starting. I wanted to use data cake, but what I haven't  considered is how it scales on the phone screen, so I had to switch mid-way through the project.
