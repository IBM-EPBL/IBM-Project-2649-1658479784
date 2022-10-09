from gpiozero import LED
from time import sleep

red = LED(22)
yellow = LED(27)
green = LED(17)
While (True):
      red.on()
      sleep(10)
      red.off()
      yellow.on()
      sleep(10)
      yellow.off()
      green.on()
      sleep(10)
      green.off()
