import numpy
import random
import matplotlib.pyplot as plt
from datacenter import DataCenter
from handle_tasks import HandleTasks
from aco_load_balancer import AcoLoadBalancer
from task import Task

if __name__ == '__main__':

    plt.ion()

    # Showing load balancer in (0,0)
    plt.plot(0, 0, 'bD')

    # Creating Datacenter and servers
    dcs = DataCenter.createFromJson()
    print(dcs)
    DataCenter.plot()

    lb = AcoLoadBalancer()

    ht = HandleTasks()

    plt.show()

