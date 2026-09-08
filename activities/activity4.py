'''
    Activity 4 — Mutual Exclusion using Semaphores (P and V Operations)
        Task: Redo Activity 2 using Python's threading.Semaphore(1) to act as a mutex, mapping directly to the P(mutex) and V(mutex) operations from the lecture.
'''

import threading

balance = 0
mutex = threading.Semaphore(1)                      # acts as P and V

def update_balance_with_semaphore():
    global balance
    
    for _ in range(100000):
        mutex.acquire()                             # P(mutex)
        balance += 1
        mutex.release()                             # V(mutex)
