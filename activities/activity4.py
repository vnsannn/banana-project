'''
    Activity 4 — Mutual Exclusion using Semaphores (P and V Operations)
        Task: Redo Activity 2 using Python's threading.Semaphore(1) to act as a mutex, mapping directly to the P(mutex) and V(mutex) operations from the lecture.
'''

import threading
import sys

balance = 0
mutex = threading.Semaphore(1)                      # acts as P and V

def update_balance_with_semaphore():
    global balance
    
    for _ in range(100000):
        mutex.acquire()                             # P(mutex)
        temp = balance
        sys.setswitchinterval(0.001)
        balance = temp + 1
        # balance += 1
        mutex.release()                             # V(mutex)

def run():
    global balance
    balance = 0

    first_thread = threading.Thread(target = update_balance_with_semaphore)
    second_thread = threading.Thread(target = update_balance_with_semaphore)
    
    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    print(f"Expected Value: 200000\nFinal balance: {balance}")

if __name__ == "__main__":
    for i in range(1, 4):
        print(f"Test: {i}")
        run()
        print("")

