import time
import random

def get_timer_normal():
    return random.randrange(10, 150, 1)

def get_timer_power():
    return random.randrange(10, 60, 1)

def get_timer_slow():
    return random.randrange(30, 300, 1)


def sleep_normal():
    time.sleep(get_timer_normal())
    return 0

def sleep_power():
    time.sleep(get_timer_power())
    return 0

def sleep_slow():
    time.sleep(get_timer_slow())
    return 0
