import time
import threading

from ant_colony_algo import AntColonyAlgo


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
        print('Waiting...')
        i = 1
        while True:
            if len(AcoLoadBalancer.tasks) > 0:
                for task in AcoLoadBalancer.tasks:
                    # print('Task '+task.id+' assigning... finding best server...')
                    server = AntColonyAlgo.find(task)
                    if server:
                        AcoLoadBalancer.running.append(task)
                    i += 1
                AcoLoadBalancer.tasks = list()
                print('Waiting for more tasks...')

    @staticmethod
    def add(tasks):
        AcoLoadBalancer.tasks += tasks

