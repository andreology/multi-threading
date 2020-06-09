#demo on using condition variable with mutex for thread usage
import threading

slowcooker_lid = threading.Lock()
soup_servings = 11
#condition variable
soup_taken = threading.Condition(lock=slowcooker_lid)

def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid: #try lock using context manager
            while (person_id != (soup_servings % 5)) and (soup_servings > 0):
                print('Person', person_id, 'checked... then put the lid back.')
                soup_taken.wait()
            if soup_servings > 0:
                soup_servings -= 1
                print("Person", person_id, 'took soup. Servings left: ', soup_servings)
                soup_taken.notifyAll()

if __name__ == '__main__':
    for person in range(5):
        threading.Thread(target=hungry_person, args=(person,)).start()
