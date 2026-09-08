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
    finish_times = {}

    # TODO: Implement the round-robin loop:
    # - Dequeue a process
    # - Run it for min(quantum, remaining burst time)
    # - If it still has remaining time, re-enqueue it
    # - Record execution order and finish times

    while queue:
        pid, _ = queue.pop(0)

        run_time = min(quantum, remaining[pid])
        time_elapsed += run_time
        remaining[pid] -= run_time

        order.append((pid, run_time, time_elapsed))

        if remaining[pid] > 0:
            queue.append((pid, remaining[pid]))
        else:
            finish_times[pid] = time_elapsed

    return order, finish_times

def run():
    processes = [("P1", 10), ("P2", 5), ("P3", 8)]
    # print(round_robin(processes, quantum=3))

    result, finish_times = round_robin(processes, quantum=3)
    print("Execution order (pid, ran_for, time_now): ")

    for entry in result:
        print(entry)

    print("\nFinish times:", finish_times)
    total_wait = 0
    burst_lookup = dict(processes)

    for pid, finish in finish_times.items():
        wait = finish - burst_lookup[pid]
        total_wait += wait
        print(f"{pid} waiting time: {wait}")

    avg_wait = total_wait / len(processes)
    print(f"\nAverage waiting time: {avg_wait}")

if __name__ == "__main__":
    run()

