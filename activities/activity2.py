'''
    Activity 2 — Simulating a Race Condition (Critical Region Problem)
        Task: Create two threads that both increment a shared variable balance 100,000 times without any synchronization. Run the program and observe that the final value is often less than the expected 200,000.
'''

import threading
import sys

balance = 0

def update_balance():
    global balance

    for _ in range(100000):
        temp = balance
        sys.setswitchinterval(0.001)
        balance = temp + 1
        # balance += 1  # NOT ATOMIC — this is the critical region

def run():
    global balance
    balance = 0

    # TODO 1: Create two threads targeting update_balance()
    # TODO 2: Start both threads
    # TODO 3: Join both threads
    # TODO 4: Print the final balance and compare it to the expected value (200000)

    first_thread = threading.Thread(target = update_balance)
    second_thread = threading.Thread(target = update_balance)

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
