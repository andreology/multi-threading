#A demo on how a deadlock may occur in thread usage
#deadlock is prevented by prioritizing mutex's and using "lock ordering"
import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count -= 1
            print(name, 'took a piece sushi remaining:', sushi_count)

        second_chopstick.release()
        first_chopstick.release()
if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('First', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('sec', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('3rd', chopstick_a, chopstick_c)).start()
