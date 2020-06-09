#demo on how to use python execution pool to control aysnc thread pool
#threadpoolexecutor is great for IO tasks unless they are cpu intensive
#hence use processpool executor for that
import threading
from concurrent.futures import ProcessPoolExecutor
import os

def vegetable_chopper(vegetable_id):
    name = os.getpid()
    print(name, 'chopped vegetable', vegetable_id)

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as pool: #pool executor is design to work with a context manager
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
        #pool.shutdown() #free up any resource that the pool is executing
