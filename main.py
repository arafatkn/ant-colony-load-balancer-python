from ant_colony_algo import AntColonyAlgo
from datacenter import DataCenter
from handle_tasks import HandleTasks
from aco_load_balancer import AcoLoadBalancer
from task import Task

if __name__ == '__main__':

    # Showing load balancer in (0,0)
    # plt.plot(0, 0, 'bD')

    # Creating Datacenter and servers
    dcs = DataCenter.loadFromCsv()
    print(DataCenter.dcs)
    # DataCenter.plot()

    lb = AcoLoadBalancer()
    lb.start()

    HandleTasks()
