from protocols import *
import multiprocessing

myProcesses = []

def stop_all():
    for p in myProcesses:
        p.terminate()


def start_http():
    p = multiprocessing.Process(target=http.start, args=())
    p.start()
    myProcesses.append(p)
