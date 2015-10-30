from protocols import *
import multiprocessing

myProcesses = []

def stop_all():
    for p in myProcesses:
        p.terminate()


def start_all():
    start_http()


def start_http():
    p = multiprocessing.Process(target=http.start, args=())
    p.start()
    myProcesses.append(p)

def process_control(command):
    if command == 'stop':
        stop_all()
        return 0
    elif command == 'all':
        start_all()
        return 0
    elif command == 'http':
        start_http()
        return 0
    else:
        return 1
