from multiprocessing import Process

def print_message(msg):
    print(f"Message: {msg}")

if __name__ == "__main__":
    p1 = Process(target=print_message, args=("Hello from Process 1",))
    p2 = Process(target=print_message, args=("Hello from Process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes have finished execution")
