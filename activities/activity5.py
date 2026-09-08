'''
    Activity 5 — Producer-Consumer Simulation (Bonus)
        Task: Using three semaphores (full, empty, mutex), implement the classic Producer-Consumer problem from the lecture using a bounded buffer (Python list) of size 5.
'''

import threading
import time
import random

BUFFER_SIZE = 5
buffer = []

empty = threading.Semaphore(BUFFER_SIZE)                # counts empty slots
full = threading.Semaphore(0)                           # counts full slots
mutex = threading.Semaphore(1)                          # mutual exclusion

def producer():
    for i in range(10):
        item = f"item-{i}"

        empty.acquire()                                 # P(empty)
        mutex.acquire()                                 # P(mutex)

        buffer.append(item)
        print(f"Produced: {item} | Buffer: {buffer}")

        mutex.release()                                 # V(mutex)
        full.release()                                  # V(full)

        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for i in range(10):
        full.acquire()                                  # P(full)
        mutex.acquire()                                 # P(mutex)

        item = buffer.pop(0)
        print(f"Consumed: {item} | Buffer: {buffer}")

        mutex.release()                                 # V(mutex)
        empty.release()                                 # V(empty)

        time.sleep(random.uniform(0.1, 0.5))

# TODO: Create and start a producer thread and a consumer thread, then join both.