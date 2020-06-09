#demo on using producer consumer to solve thread synchronization
import queue #module queue includes lock for threads
import threading
import time

serving_line = queue.Queue(maxsize=5)

def soup_producer():
    for i in range(20):
        serving_line.put_nowait('Bowl #' + str(i))
        print('Served Bowl #', str(i), '-remaining capacity:', \
                serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2)
    serving_line.put_nowait('No more soup')
    serving_line.put_nowait('No more soup')

def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'No more soup':
            break
        print('Ate', bowl)
        time.sleep(0.3)

if __name__ == '__main__':
    for consumer in range(2):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
