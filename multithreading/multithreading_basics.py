import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order from {i}")
        time.sleep(2)    


    # time.sleep(2)    
        
def brew_chai():
    for i in range(1,4):
        print(f"Brewing CHai of order numnber {i}")  
        time.sleep(3)      
 
    # time.sleep(3)      

# Create thread

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# Wait 
order_thread.join()
brew_thread.join()

print("All order complete")