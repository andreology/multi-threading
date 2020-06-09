#A demo to show the use of try lock for threads
import threading
import time

items_on_notepad = 0
mutex = threading.Lock()

def shopper():
    global items_on_notepad
    name = threading.current_thread().getName()
    items_to_add = 0
    while items_on_notepad <= 20:
        if items_to_add and mutex.acquire(blocking=False):
            
            items_on_notepad += items_to_add
            print(name, 'added', items_to_add, 'items(s) to notepad')
            items_to_add = 0
            time_to_add = 0
            time.sleep(0.3)
            mutex.release()
        else:
            time.sleep(0.1)
            items_to_add += 1
            print(name, 'found something else to buy')
if __name__ == '__main__':
    first_shopper = threading.Thread(target=shopper, name='Shopper1')
    sec_shopper = threading.Thread(target=shopper, name='Shopper2')
    start_time = time.perf_counter()
    first_shopper.start()
    sec_shopper.start()
    first_shopper.join()
    sec_shopper.join()
    elapsed_time = time.perf_counter() - start_time
    print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))
