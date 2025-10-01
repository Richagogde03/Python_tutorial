from threading import Thread
# from threading import *
# from time import sleep
import time


class Hello(Thread):
    def run(self):
        for i in range(8):
            print("Hello")
            time.sleep(1)


class Hii(Thread):
    def run(self):
        for i in range(8):
            print("Hii")
            time.sleep(1)


t1 = Hello()
t2 = Hii()

# this is normal function calling
# this will print hello hii one after another instead of simultaneously
# t1.run()
# t2.run()

# to run simultaneously both functions we need to use start() and
# to see results clearly we need to use time here to sleep
t1.start()
# time.sleep(1)
t2.start()

# print("Bye Bye")

# to wait for t1 and t2 to execute before the main thread to print byee
t1.join()
t2.join()

print("Bye")
