# thread is small part in a big task
# thread is single process in multi processes
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)


t1 = Hello()
t2 = Hi()
'''
t1.run()
t2.run()
'''
# To print hello and hii simultaneously we should require a thread ,so we have to import thread from threading.
# In general every program have to run with a thread which is main thread.
# if we want to create a thread we have import thread and inherits thread to our class
# once you import thread you should not used class methods to execute the class we should use start() method
# which makes our thread(our class) to execute
# as we are using threads and we use start method our class should only be named as run not with other names
t1.start()
sleep(0.2)
t2.start()
# here we see both hello hii are execute  simultaneously but there is a collision in this process
# so we use a function called sleep doing this by importing sleep() from time
t1.join()
t2.join()
print("Bye")