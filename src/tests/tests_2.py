import threading

def hello_world():
    print("Hello World")

timer = threading.Timer(10, hello_world)
timer.start()