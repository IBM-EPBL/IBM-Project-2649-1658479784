import random
from time import sleep

while (True):
    temperature = random.randrange(0, 100)
    if (temperature >= 50):

        humidity = random.randrange(0, 20)
    else:
        humidity = random.randrange(21, 50)
    print("the temperature of the room is {} fahrenheit".format(temperature))

    print("the humidity of the room is {}".format(humidity))

    if (temperature > 60 and humidity < 50):
        print("****the alarm must be detected****")
        break
    sleep(2)
