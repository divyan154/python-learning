import threading
import requests
import time

start = time.time()
# print(f"{start:.1f}")

def download(url):
    print(f"Starting Download from {url}")
    try:
        respone = requests.get(url)
        print(f"Download finished .. response {len(respone.content)}")
    except Exception as e:
        print(e)


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]    

threads = []
for url in urls:
    t = threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"End time .. {end - start:.2f}")   
