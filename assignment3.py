from gpizero import LED
from time import sleep
RED=LED(16)
YELLOW=LED(18)
GREEN=LED(17)
while(True):
    RED.on()
    sleep(30)
    RED.off()
    YELLOW.on()
    sleep(10)
    YELLOW.off()
    GREEN.on()
    sleep(30)
    GREEN.off()
