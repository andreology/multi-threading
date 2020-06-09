#demo on using producer consumer to solve thread synchronization
import queue #module queue includes lock for threads
import multiprocessing as mp
import time

serving_line = mp.Queue(5)

def cpu_work(work_units):
    x = 0
    for work in range(work_units * 1_000_000):
        x += 1

def soup_producer(serving_line):
    for i in range(20):
        serving_line.put_nowait('Bowl #' + str(i))
        print('Served Bowl #', str(i), '-remaining capacity:', \
                serving_line._maxsize-serving_line.qsize())
        time.sleep(0.2)
    serving_line.put_nowait('No more soup')
    serving_line.put_nowait('No more soup')

def soup_consumer(serving_line):
    while True:
        bowl = serving_line.get()
        if bowl == 'No more soup':
            break
        print('Ate', bowl)
        cpu_work(4)

if __name__ == '__main__':
    for consumer in range(2):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()
    mp.Process(target=soup_producer, args=(serving_line,)).start()
