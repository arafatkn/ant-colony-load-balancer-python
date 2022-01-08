import random
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
        while True:
            num = random.randint(5, 10)  # input("How many new task: ")
            tasks = list()
            for i in range(int(num)):
                task = Task(random.randint(0, 50), random.randint(0, 50))
                tasks.append(task)
                print("Task created: (", task.x, ",", task.y, "). ID:", task.id)
            AcoLoadBalancer.add(tasks)
            time.sleep(random.randint(10, 15))
