"""
As this is am example of threading all the thread will work randomly
Better to Comment and use first time to understand

"""

import threading

# Default thread
thread_name = threading.current_thread().getName()
print(thread_name)
# After changing thread name
threading.current_thread().name = "CustomThread"
thread_name = threading.current_thread().getName()
print(thread_name+"\n")


# Functional way to create a thread
def even_numbers():
    print("="*40)
    print("Thread name:", threading.current_thread().getName())
    for x in range(20):
        if x % 2 is 0:
            print(x)


t = threading.Thread(target=even_numbers, name="FunctionalThread")
t.start()


# Class based way to create a thread
class OddNumber(threading.Thread):
    def run(self):
        print("Thread name:", threading.current_thread().name)
        for x in range(20):
            if x % 2 is not 0:
                print(x)


obj = OddNumber()
obj.name = "ClassBaseThread"
obj.start()


# Class-function based way to create a thread
class Number(threading.Thread):
    def numbers(self):
        print("Thread name:", threading.current_thread().name)
        for x in range(20):
            print(x)


t1 = threading.Thread(target=Number().numbers(), name="ClassFunctionBased Thread")
t1.start()
