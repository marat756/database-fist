import threading 
import time

def sanash1():
    for x in range(150):
        if x == 50:
            break
        time.sleep(0.1)
        print("Marat: ")

def sanash2():
    for x in range( 150):
        if x == 100:
            break
        time.sleep(0.1)
        print("Tagaev: ")

def sanash3():
    for x in range(150):
        time.sleep(0.1)
        print("Baqitjan ogli: ")

t1 = threading.Thread(target=sanash1)
t2 = threading.Thread(target=sanash2)
t3 = threading.Thread(target=sanash3)


t1.start()
t2.start()
t3.start()