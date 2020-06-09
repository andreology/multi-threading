#example of using a future to retreive results between async tasks
from concurrent.futures import ThreadPoolExecutor
import time

def how_many():
    print('cook is counting')
    time.sleep(3)
    return 32

if __name__ == '__main__':
    print("chef asks cook how many")
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many)
        print("chef is working on other tasks")
        print("cook reports a count of ", future.result()) #here the thread will be blocked until how_many is done
