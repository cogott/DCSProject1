'''Please implement the producer-consumer solution using semaphores and a finite
buffer (cf. slides 27-30 of the presentation about advanced synchronization).
You can use arbitrary elements.
Both threads (the producer and the consumer) should print the info about
produced/consumed elements to the standard output.
Use random processing times (simulated by sleeping - Thread.Sleep() in C#, or
time.sleep() in Python).'''

import threading
import random
import time

buffer = []
buffer_size = 10

empty_slots = threading.Semaphore(buffer_size)
filled_slots = threading.Semaphore(0)
lock = threading.Lock()


class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 100)
            empty_slots.acquire()
            lock.acquire()
            buffer.append(item)
            print(f"Producer {self.name} added {item} to the buffer")
            lock.release()
            filled_slots.release()
            time.sleep(random.random())


class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            filled_slots.acquire()
            lock.acquire()
            item = buffer.pop(0)
            print(f"Consumer {self.name} consumed {item} from the buffer")
            lock.release()
            empty_slots.release()
            time.sleep(random.random())


producer1 = Producer()
producer1.name = "producer1"
producer2 = Producer()
producer2.name = "producer2"
consumer1 = Consumer()
consumer1.name = "consumer1"
consumer2 = Consumer()
consumer2.name = "consumer2"

producer1.start()
producer2.start()
consumer1.start()
consumer2.start()
'''This implementation uses four semaphores: empty_slots, filled_slots, and lock.
The empty_slots semaphore is used to keep track of the number of empty slots in the buffer, and is initialized to the maximum buffer size.
The filled_slots semaphore is used to keep track of the number of filled slots in the buffer, and is initialized to 0.
the lock to protect the buffer from concurrent access.
Two threads of Producer class are producing random ints between 1-100 and adding it to buffer, and two threads of Consumer class are consuming them from the buffer.
Both class calls sleep with a random value, this simulate the processing time.'''