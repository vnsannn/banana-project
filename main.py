from activities import activity1, activity2, activity3, activity4, activity5, activity6

def head(title):
    print("")
    print("=" * 60)
    print(title)
    print("=" * 60)


if __name__ == "__main__":
    head("Activity 1: Process Creation and Termination")
    activity1.run()

    head("Activity 2: Simulating a Race Condition (Critical Region Problem)")
    for i in range(1, 4):
        print(f"Test: {i}")
        activity2.run()
        print("")

    head("Activity 3: Implementing a Test-and-Set (TS) Lock")
    for i in range(1, 4):
        print(f"Test: {i}")
        activity3.run()
        print("")

    head("Activity 4: Mutual Exclusion using Semaphores (P and V Operations)")
    for i in range(1, 4):
            print(f"Test: {i}")
            activity4.run()
            print("")

    if input("\nDo you want to continue to bonus part (5 & 6)? Y or N: ").strip().lower() == "y":
        head("Activity 5: Producer-Consumer Simulation (Bonus)")
        activity5.run()

        head("Activity 6: Simple Round-Robin Scheduler Simulation")
        activity6.run()

    else:
        print("Thanks for using the program! See you again!")