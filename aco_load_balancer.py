import csv
import sys
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
        i = 0
        max_lat = 0
        min_lat = sys.maxsize
        avg_lat = 0
        file = open('outputs/latency_result.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['Latency', 'Min latency', 'Max Latency', 'Avg Latency'])

        while True:
            if len(AcoLoadBalancer.tasks) > 0:
                for task in AcoLoadBalancer.tasks:
                    # print('Task '+task.id+' assigning... finding best server...')
                    st = time.time()
                    server = AntColonyAlgo.find(task)
                    if server:
                        AcoLoadBalancer.running.append(task)

                    taken = time.time() - st

                    if taken > max_lat:
                        max_lat = taken

                    if taken < min_lat:
                        min_lat = taken

                    avg_lat = (avg_lat * i + taken) / (i + 1)
                    i = i + 1
                    print('Latency: Min: %dms | Max: %dms | Avg: %dms' % (min_lat*1000/60, max_lat*1000/60, avg_lat*1000/60))
                    writer.writerow([taken*1000/60, min_lat*1000/60, max_lat*1000/60, avg_lat*1000/60])

                AcoLoadBalancer.tasks = list()
                print('Waiting for more tasks...')

    @staticmethod
    def add(tasks):
        AcoLoadBalancer.tasks += tasks

    @staticmethod
    def append(task):
        AcoLoadBalancer.tasks.append(task)
