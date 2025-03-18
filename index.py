import requests
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

target =('https://arpanbhandari.com.np/')

def send_request():
    while True:
        try:
            r = requests.get(target)
            logging.info(f"Status code: {r.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred: {e}")
            break

# Number of threads to simulate multiple users
num_threads = 10

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
