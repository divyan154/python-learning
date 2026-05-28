import threading
import time

lock = threading.Lock()

counter = 0

def modify():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

start = time.time()
threads = [threading.Thread(target=modify) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
# end = time.time()
# print(f"End time {end - start:.2f}")
print(counter)