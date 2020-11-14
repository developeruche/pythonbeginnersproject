import time

def timeCount(x): 
    times = x
    for i in range(x):
        times -= 1
        time.sleep(1)
        print(times)

timeCount(5)

