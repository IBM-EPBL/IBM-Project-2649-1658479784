import random
while True:
    temperature = random.randrange(-50, 120)
    humidity = random.randrange(0, 100)
    print(f'Temperature is {temperature} Degree')
    print(f'Humidity is {humidity}%')
    if temperature >= 90 and humidity <= 50:
        print("Alarm is Detected")
        break
    else:
        print("Alarm Is not detected")
        continue