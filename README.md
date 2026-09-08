# Laboratory Activity: Process Synchronization, Scheduling, and Mutual Exclusion using Python

## I. Objectives
At the end of this activity, students should be able to:
1. **Simulate process creation and termination** using Python's `multiprocessing` module, relating it to the concepts of `fork`, `exit`, and parent-child process hierarchy.
2. **Demonstrate a race condition** that occurs when concurrent processes/threads access a shared critical region without synchronization.
3. **Implement a simple Test-and-Set (TS) lock** in Python and observe the problem of busy waiting.
4. **Implement mutual exclusion (mutex)** using Python's semaphore-like tools, applying the `P` (wait/test) and `V` (signal/increment) operations discussed in class.
5. **Simulate a basic process scheduler (Round-Robin)** to relate scheduling concepts (priority, time quantum) to actual code behavior.
6. **Compare the efficiency and correctness** of busy-waiting locks vs. blocking (semaphore) locks.

## II. Materials / Requirements
* **Python 3.8** or later
* **Text editor / IDE** (VS Code, PyCharm, IDLE, or Jupyter Notebook)
* **Built-in modules only:** `multiprocessing`, `threading`, `time`, `random`, `sys`
