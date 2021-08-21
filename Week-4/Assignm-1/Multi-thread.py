import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")
# rewrite everything inside this main function and keep others untouched


def main1():
    for i in range(1,2):
        do_job(i)

def main2():
    for i in range(2,3):
        do_job(i)

def main3():
    for i in range(3,4):
        do_job(i)        

def main4():
    for i in range(4,5):
        do_job(i)

def main5():
    for i in range(5,6):
        do_job(i)

t1 = threading.Thread(target=main1)
t2 = threading.Thread(target=main2)
t3 = threading.Thread(target=main3)
t4 = threading.Thread(target=main4)
t5 = threading.Thread(target=main5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()