from multiprocessing import Process,Queue
# import threading
import time


counter = 0
def modify():
    global counter
    for i in range(10 ** 8):
        counter += i
    print("Done ")   

def prepare_chai(queue):
    queue.put("Masala Chai")
     

if __name__ == "__main__":    
    queue = Queue()
    process = Process(target=prepare_chai(queue)) 
    process.start()
    process.join()
    print(queue.get())
    # [t.start() for t in threads]
    # [t.join() for t in threads]

    
    # end = time.time()   
    # print(f"Time taken .. {end - start:.2f}") 



