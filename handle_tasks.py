import csv
import random
import sys
import time
import threading
from aco_load_balancer import AcoLoadBalancer
from task import Task


class HandleTasks(object):
    def __init__(self, interval=1):
        self.interval = interval
        self.thread = threading.Thread(target=HandleTasks.run, args=())
        self.thread.daemon = True
        self.thread.start()

    @staticmethod
    def run():
        st = time.time()
        filename = 'data/tasks.csv'
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                next(reader, None)
                for row in reader:
                    if st + int(row[3]) > time.time():
                        time.sleep(st + int(row[3]) - time.time())

                    task = Task(int(row[0]), int(row[1]), float(row[2]))
                    print("Task created: (", task.x, ",", task.y, "). ID:", task.id)
                    AcoLoadBalancer.append(task)

            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
