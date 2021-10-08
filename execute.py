import time
import threading
from aco_load_balancer import AcoLoadBalancer
from datacenter import DataCenter


class Execute(object):
    def __init__(self, interval=1):
        self.interval = interval
        self.thread = threading.Thread(target=Execute.run, args=())
        self.thread.daemon = True
        self.thread.start()

    @staticmethod
    def run():
        while True:
            if len(AcoLoadBalancer.running):
                time.sleep(3)
            i = 0
            while i < len(DataCenter.dcs):
                j = 0
                while j < len(DataCenter.dcs[i].servers):
                    if not DataCenter.dcs[i].servers[j].status:
                        continue

                    k = 0
                    while k < len(DataCenter.dcs[i].servers[j].tasks):
                        task = DataCenter.dcs[i].servers[j].tasks[k]
                        if task.required_time + task.start_time < time.time():
                            print('Task ' + str(task.id) + ' execution completed ')
                            DataCenter.dcs[i].servers[j].tasks.pop(k)
