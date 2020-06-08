#demo to show how to fix data race issue with a mutex
import threading
import time

counter = 0
mutex = threading.Lock()

def compute():
    global counter

    for i in range(5):
        #critical section
        print(threading.current_thread().getName(), "is computing")
        time.sleep(0.5)
        mutex.acquire()
        counter += 1
        mutex.release()

if __name__ == '__main__':
    machine = threading.Thread(target=compute)
    machine0 = threading.Thread(target=compute)
    machine.start()
    machine0.start()
    machine.join()
    machine0.join()
    print("Final count", counter, ' amt')
