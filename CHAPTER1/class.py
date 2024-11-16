from threading import Thread
from queue import Queue
import time
import random

# Producer Class
class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify: item N°%d appended to queue by %s' % (item, self.name))
            time.sleep(1)  
        for _ in range(3):  
            self.queue.put(None)

# Consumer Class
class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.daemon = True  

    def run(self):
        while True:
            item = self.queue.get()
            
            # Exit loop if sentinel value (None) is received
            if item is None:
                self.queue.task_done()
                break

            print('Consumer notify: %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()
            time.sleep(2)  # Simulate time delay for consuming

# Main program
if __name__ == '__main__':
    queue = Queue()

    # Create producer and consumer threads
    producer = Producer(queue)
    consumers = [Consumer(queue) for _ in range(3)]

    # Start producer and consumer threads
    producer.start()
    for consumer in consumers:
        consumer.start()

    # Wait for the producer to finish
    producer.join()

    # Wait for all items in the queue to be processed
    queue.join()

    print("All tasks are completed.")
