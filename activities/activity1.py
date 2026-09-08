'''
    Activity 1 — Process Creation and Termination
        Task: Write a Python program that creates 3 child processes, each of which prints its own process ID and a message, then terminates. The parent process must wait for all child processes to finish (similar to how a Unix parent uses wait() to collect a terminated/zombie child) before it prints "All child processes terminated."
'''

import multiprocessing
import os
import time

def child_task(task_id):
    print(f"Child {task_id} started. PID = {os.getpid()}")
    time.sleep(1)
    print(f"Child {task_id} finished.")

def run():
    print(f"Parent PID = {os.getpid()}")

    processes = []

    # TODO 1: Create 3 processes using multiprocessing.Process()
    #    target=child_task, args=(i,)
    # TODO 2: Start each process
    # TODO 3: Use .join() on each process (this is the "wait" step)

    for i in range(1, 4):
        process = multiprocessing.Process(target = child_task,args = (i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All child processes terminated.")

if __name__ == "__main__":
    run()