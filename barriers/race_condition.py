#demo on race conditions and how to solve the issue
import threading

bags_of_chips = 1 #one in list already
pencil = threading.Lock()
barr = threading.Barrier(10) #barrier

def cpu_work(work_units):
    x = 0
    for work in range(work_units * 1_000_000):
        x += 1

def first_shopper():
    global bags_of_chips
    cpu_work(1)
    barr.wait()
    with pencil:
        bags_of_chips *= 2
        print("First shopper doubled the bags of chips")

def sec_shopper():
    global bags_of_chips
    cpu_work(1)
    with pencil:
        bags_of_chips += 3
        print("Second shopper added 3 bags of chips")
    barr.wait()

if __name__ == '__main__':
    shoppers = []
    for s in range(5):
        shoppers.append(threading.Thread(target=first_shopper))
        shoppers.append(threading.Thread(target=sec_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bargs of chips')
