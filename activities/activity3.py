'''
    Activity 3 — Implementing a Test-and-Set (TS) Lock
        Task: Implement your own Test-and-Set style lock (do NOT use threading.Lock) using a shared flag and a busy-waiting while loop, then use it to fix the race condition from Activity 2.
'''

import threading
import time

lock_flag = 0                                # 0 = free, 1 = busy
balance = 0

def test_and_set(flag_list):
    # TODO: In ONE "atomic" step (simulate with threading.Lock only for the
    #   flag check itself), test if flag_list[0] == 0, and if so set it to 1.
    #   Return the OLD value.
    pass

def acquire_lock():
    while test_and_set(...):                # busy waiting (spinning)
        pass

def release_lock():
    global lock_flag
    lock_flag = 0

def update_balance_safe():
    global balance

    for _ in range(100000):
            acquire_lock()
            balance += 1
            release_lock()
