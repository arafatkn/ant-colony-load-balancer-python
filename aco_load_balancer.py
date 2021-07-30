import time
import threading
from matplotlib import pyplot as plt
from datacenter import DataCenter


class AcoLoadBalancer(object):
    tasks = list()

    def __init__(self, interval=1):
        self.interval = interval
        self.thread = threading.Thread(target=AcoLoadBalancer.run, args=())
        self.thread.start()

    @staticmethod
    def run():
        log = open('logs/tasks.log', 'w', 1)
        log.write('Waiting...\n')
        i = 1
        while True:
            if len(AcoLoadBalancer.tasks) > 0:
                for task in AcoLoadBalancer.tasks:
                    log.write('Task ' + str(i) + ' (' + str(task.x) + ', ' + str(task.y) + ') Assigned. State: '
                                                                                           'Executing\n')
                    i += 1
                AcoLoadBalancer.tasks = list()
                log.write('Waiting...\n')

    @staticmethod
    def add(tasks):
        AcoLoadBalancer.tasks += tasks
