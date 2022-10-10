from gpiozero import LED
from time import sleep
red_led=LED(17)
yellow_led=LED(27)
green_led=LED(22)
while True:
    red_led.on()
    sleep(30)
    red_led.off()
    green_led.on()
    sleep(60)
    green_led.off()
    yellow_led.on()
    sleep(20)
    yellow_led.off()