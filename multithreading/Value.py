from multiprocessing import Process,Value

def increment(counter):
    for i in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__== "__main__":
    counter = Value('i',0)
    process = [Process(target=increment,args = (counter,) ) for _ in range(3)]
    [p.start() for p in process]
    [p.join() for p in process]

    print(counter.value)

    
