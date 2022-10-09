import random
import time
temp = [25,26,27,28,29,31,32,33,34,35,36,37]#temperature is taken in terms of celsius
humidity=[50,55,60,65,70,75,80,85,90,95,100]#humidity is taken in terms of percentage(%)
sel_temp=random.choice(temp)
if sel_temp<100:
    iteration=True
    while iteration:
        sel_temp=random.choice(temp)
        sel_humidity=random.choice(humidity)
        print(f"the temperature is {sel_temp} celsius")
        print(f"The humidity level is {sel_humidity}%")
        if sel_temp>30 and sel_humidity<65:
            print("****Alert****,the temperature is increasing")
            time.sleep(5)
        else:
            print(f"***Alert***,the temperature is decreasing")
            time.sleep(5)

else:
    ieration=False
