#demo on how a reentrant or recursive lock may be used to
#fix a data race issue
import threading

counter = 0
counter0 = 0
mutex = threading.RLock()

def compute():
    global counter
    mutex.acquire()
    counter += 1
    mutex.release()
def compute0():
    global counter0
    mutex.acquire()
    counter0 += 1
    #potential for bottleneck if RLock was not here
    compute()
    mutex.release()
def work():
    for i in range(10_000):
        compute()
        compute0()

if __name__ == '__main__':
    thread = threading.Thread(target=work)
    thread0 = threading.Thread(target=work)
    thread.start()
    thread0.start()
    thread.join()
    thread0.join()
    print("counter total", counter)
    print("counter 0 total ", counter0)
