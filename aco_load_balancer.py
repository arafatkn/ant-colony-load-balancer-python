import time
import threading

from ant_colony_algo import AntColonyAlgo
from datacenter import DataCenter


class AcoLoadBalancer(object):
    tasks = list()
    running = list()

    def __init__(self, interval=1):
        self.interval = interval
        self.thread = threading.Thread(target=AcoLoadBalancer.run, args=())

    def start(self):
        self.thread.start()

    @staticmethod
    def run():
        # log = open('logs/tasks.log', 'w', 1)
        print('Waiting...\n')
        i = 1
        while True:
            if len(AcoLoadBalancer.tasks) > 0:
                for task in AcoLoadBalancer.tasks:
                    server = AntColonyAlgo.find(task)
                    if not server:
                        AcoLoadBalancer.checkForCompletion()
                        server = AntColonyAlgo.find(task)
                    AcoLoadBalancer.running.append(task)
                    i += 1
                AcoLoadBalancer.tasks = list()
                print('Waiting...\n')

    @staticmethod
    def add(tasks):
        AcoLoadBalancer.tasks += tasks

    @staticmethod
    def checkForCompletion():
        for task in AcoLoadBalancer.running:
            if task.start_time + task.required_time > time.time():
                break
            break

