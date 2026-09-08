'''
    Activity 3 — Implementing a Test-and-Set (TS) Lock
        Task: Implement your own Test-and-Set style lock (do NOT use threading.Lock) using a shared flag and a busy-waiting while loop, then use it to fix the race condition from Activity 2.
'''

import threading
import sys

lock_flag = [0]                                # 0 = free, 1 = busy
balance = 0
flag_check = threading.Lock()

def test_and_set(flag_list):
    # TODO: In ONE "atomic" step (simulate with threading.Lock only for the
    #   flag check itself), test if flag_list[0] == 0, and if so set it to 1.
    #   Return the OLD value.
    
    with flag_check:
        old_value = flag_list[0]
        flag_list[0] = 1

    return old_value

def acquire_lock():
    while test_and_set(lock_flag) == 1:                # busy waiting (spinning)
        pass

def release_lock():
    global lock_flag
    lock_flag[0] = 0

def update_balance_safe():
    global balance

    for _ in range(100000):
            acquire_lock()
            temp = balance
            sys.setswitchinterval(0.001)    
            balance = temp + 1
            # balance += 1
            release_lock()

def run():
    global balance
    balance = 0

    first_thread = threading.Thread(target = update_balance_safe)
    second_thread = threading.Thread(target = update_balance_safe)
    
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
