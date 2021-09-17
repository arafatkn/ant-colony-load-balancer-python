from server import Server
import json
import math
import matplotlib.pyplot as plt


class DataCenter:
    server_limit = 10
    dcs = list()

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.servers = list()

    def createServers(self):
        for i in range(self.server_limit):
            x = float(self.x) + 2 * math.cos(i * 40)
            y = float(self.y) + 2 * math.sin(i * 40)
            self.servers.append(Server(x, y))

    def __repr__(self):
        return "\nName: %s, X: %s, Y: %s, Servers: %s" % (self.name, self.x, self.y, len(self.servers))

    def __str__(self):
        return "Name: %s, X is %s, Y is %s, Servers: %s\n" % (self.name, self.x, self.y, self.server_limit)

    @staticmethod
    def createFromJson():
        if len(DataCenter.dcs) > 0:
            return DataCenter.dcs
        items = json.load(open('config/datacenters_static.json'))
        dcs = list()
        for item in items:
            dc = DataCenter(item['name'], item['x'], item['y'])
            dc.createServers()
            dcs.append(dc)
        DataCenter.dcs = dcs
        return DataCenter.dcs

    @staticmethod
    def plot():
        dcs = DataCenter.dcs
        plt.ioff()
        fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axis

        ax.plot(0, 0, 'bD')
        ax.plot([obj.x for obj in dcs], [obj.y for obj in dcs], '^')

        for dc in dcs:
            enabled = list(filter(lambda s: s.status, dc.servers))
            disabled = list(filter(lambda d: d.status == 0, dc.servers))
            ax.plot([obj.x for obj in enabled], [obj.y for obj in enabled], 'g.')
            ax.plot([obj.x for obj in disabled], [obj.y for obj in disabled], 'k.')

        fig.savefig('outputs/datacenters.png')  # save the figure to file
        plt.close(fig)

