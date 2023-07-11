#           --------------------------- Multithreading ---------------------------
'''
# Multithreading

MultiThreading is a technique to perform parallel computing/execution

multithreading is a threading technique in python to run multiple threads
concurrently by rapidly sqitching between thread with CPU help 


# 1 - multiprocessing
# 2 - multithreading 


# 1 - multiprocessing
Multiprocessing refers to the ability of a system to support more than
one processes at the same time

# What is process ?
process can be a whole program or application 


1 - Internal Process
those process which is important to run the os


2 - External Process
External process can be a program or application which is not important to run the os

process cannot share the data by default

External process cant access the other external process data
but the internal process can access the external process data
'''

# Methods :-
# start() :-
# run() :-
# join() :-
 
# Sample Example :-
'''
def squar(data):
    for i in data:
        print(f'Square of {i} is : {i ** 2}')

def cube(data):
    for i in data:
        print(f'Cube of {i} is {i ** 3}')

data = [2,3,4,5,6,7,8]

squar(data)
cube(data)


# multiprocessing based on func (External Process):-

import multiprocessing as mp 

def squar(data):
    for i in data:
        print(f'Square of {i} is : {i ** 2}')

def cube(data):
    for i in data:
        print(f'Cube of {i} is {i ** 3}')

if __name__ == '__main__':  # after main function exceution will be start

    data = [2,3,4,5,6,7,8] 

    t1 = mp.Process(target=squar, args=(data, ))
    t2 = mp.Process(target=cube, args=(data, ))

    t1.start()
    t2.start()
'''

# Thread based function :-
import threading as th
import time
'''
def func(sec):
    print(f'Sleeping for {sec} seconds')
    time.sleep(sec)

# func(4)
# func(2)
# func(1)
time1 = time.perf_counter()

t1 = th.Thread(target=func, args=[4])
t2 = th.Thread(target=func, args=[2])
t3 = th.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)


# get thread name :-
print('main thread', th.current_thread().name)

# set thread name :-
th.current_thread().name = 'ChildThread'
print('new thread', th.current_thread().name)


# Race condition or asynchronization :-
balance = 0
print(f'Balance is : {balance}')

def myfunc():
    global balance
    for i in range(90000):
        balance += 1

t1 = th.Thread(target=myfunc)
t2 = th.Thread(target=myfunc)

t1.start()
t2.start()

t1.join()
t2.join()
print(f'Balance after thread is : {balance}')


# synchronization :-
balance = 0
print(f'Balance is : {balance}')

def myfunc(lock):
    global balance
    
    for i in range(90000):
        lock.acquire()
        balance += 1
        lock.release()

lock = th.Lock()

t1 = th.Thread(target=myfunc, args=(lock, ))
t2 = th.Thread(target=myfunc, args=(lock, ))

t1.start()
t2.start()

t1.join()
t2.join()
print(f'Balance after thread is : {balance}')
'''


