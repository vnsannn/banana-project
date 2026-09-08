'''
    Activity 6 — Simple Round-Robin Scheduler Simulation
        Task: Given a list of processes with their burst times, simulate preemptive Round-Robin scheduling with a fixed time quantum, printing the order of execution and computing average waiting time.
'''

def round_robin(processes, quantum):

    """
        processes: list of tuples (pid, burst_time)
    """

    queue = processes.copy()
    remaining = dict(processes)
    time_elapsed = 0
    order = []

    # TODO: Implement the round-robin loop:
    # - Dequeue a process
    # - Run it for min(quantum, remaining burst time)
    # - If it still has remaining time, re-enqueue it
    # - Record execution order and finish times

    return order

processes = [("P1", 10), ("P2", 5), ("P3", 8)]
print(round_robin(processes, quantum=3))
