from multiprocessing import Process, Queue
import time

def producer(queue, producer_id):
    for i in range(3):
        item = f"Item {i} from Producer {producer_id}"
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.5)

def consumer(queue, consumer_id):
    while not queue.empty():
        item = queue.get()
        print(f"Consumer {consumer_id} consumed: {item}")
        time.sleep(0.5)

if __name__ == '__main__':
    queue = Queue()

    producer1 = Process(target=producer, args=(queue, 1))
    producer2 = Process(target=producer, args=(queue, 2))
    consumer1 = Process(target=consumer, args=(queue, 1))
    consumer2 = Process(target=consumer, args=(queue, 2))

    producer1.start()
    producer2.start()

    producer1.join()
    producer2.join()

    consumer1.start()
    consumer2.start()

    consumer1.join()
    consumer2.join()

    print("Producer-Consumer processes finished")
