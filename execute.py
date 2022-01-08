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
                time.sleep(1)  # seconds

            for i in range(len(DataCenter.dcs)):

                for j in range(len(DataCenter.dcs[i].servers)):
                    if not DataCenter.dcs[i].servers[j].status:
                        continue

                    tl = len(DataCenter.dcs[i].servers[j].tasks)

                    for k in range(tl):
                        task = DataCenter.dcs[i].servers[j].tasks[k]
                        if task.required_time + task.start_time < time.time():
                            print('Task ' + str(task.id) + ' execution completed and removed from server '
                                  + DataCenter.dcs[i].servers[j].id + ' of ' + DataCenter.dcs[i].name)
                            DataCenter.dcs[i].servers[j].tasks.pop(k)

                    tl = len(DataCenter.dcs[i].servers[j].tasks)

                    # Turn Off Server if no task assigned.
                    if tl < 1:
                        DataCenter.dcs[i].servers[j].status = False
