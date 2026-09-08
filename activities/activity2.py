'''
    Activity 2 — Simulating a Race Condition (Critical Region Problem)
        Task: Create two threads that both increment a shared variable balance 100,000 times without any synchronization. Run the program and observe that the final value is often less than the expected 200,000.
'''

import threading

balance = 0

def update_balance():
    global balance

    for _ in range(100000):
        balance += 1  # NOT ATOMIC — this is the critical region

# TODO 1: Create two threads targeting update_balance()
# TODO 2: Start both threads
# TODO 3: Join both threads
# TODO 4: Print the final balance and compare it to the expected value (200000)
