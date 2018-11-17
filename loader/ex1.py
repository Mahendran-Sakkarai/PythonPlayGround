from threading import Thread
from time import sleep
import sys

def thread_function():
    global threadCompleted
    sleep(10)
    threadCompleted = True

def loader():
    while(True):
        val = 0
        for i in range(6):
            # sys.stdout.write("\033")
            # sys.stdout.flush()
            sys.stdout.write("*")
            sys.stdout.flush()
            val += 1
            sleep(1)

        sys.stdout.write("\r")
        sys.stdout.flush()

        for j in range(val):
            sys.stdout.write(" ")

        sys.stdout.write("\r")
        sys.stdout.flush()
        if(threadCompleted):
            break

if __name__ == "__main__":
    threadCompleted = False
    thread = Thread(target=thread_function)
    loaderThread = Thread(target=loader)
    thread.start()
    loaderThread.start()
    thread.join()
    loaderThread.join()
    # sys.stdout.write("\r")
    # sys.stdout.flush()