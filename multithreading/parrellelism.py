from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing {name} Chai ....")
    time.sleep(3)
    print(f"End of chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target= brew_chai , args = (f" Makers {i + 1}",))
        for i in range(4)
    ]
    for p in chai_makers:
       p.start()

    for p in chai_makers:
       p.join()

    print("All Order complete") 

   