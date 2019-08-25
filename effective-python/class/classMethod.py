import logging
from pprint import pprint
from sys import stdout as STDOUT

# Example 1
class InputData(object):
    def read(self):
        raise NotImplementedError

# Example 2
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


# Example 3
class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
    
    def reduce(self, other):
        self.result += other.result

import os

def generate_input(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    inputs = generate_input(data_dir)
    workers = create_workers(inputs)
    return execute(workers)