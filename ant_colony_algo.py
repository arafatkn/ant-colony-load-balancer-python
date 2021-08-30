from matplotlib import pyplot as plt
from ant_colony_optimization import AntColonyOptimizer
from scipy.spatial import distance_matrix
import pandas as pd
from datacenter import DataCenter
import numpy as np


class AntColonyAlgo:

    @staticmethod
    def find():
        dcs = DataCenter.dcs
        coordinates = AntColonyAlgo.get_coordinates(dcs)
        nodes = AntColonyAlgo.get_nodes(dcs)

        # plt.plot(coordinates[:, 0], coordinates[:, 1], 'o')

        df = pd.DataFrame(coordinates, columns=['xcord', 'ycord'], index=nodes)
        # print(df)

        problem = distance_matrix(df.values, df.values)
        # fdf = pd.DataFrame(problem, index=df.index, columns=df.index)
        # print(fdf)

        optimizer = AntColonyOptimizer(ants=20, evaporation_rate=.1, intensification=2, alpha=1, beta=1,
                                       beta_evaporation_rate=0, choose_best=.1)

        optimizer.fit(problem, 100, verbose=False)

        best = optimizer.get_best_fit()

        return best
        # optimizer.plot()

    @staticmethod
    def get_coordinates(dcs):
        coordinates = list()

        for dc in dcs:
            for i in range(10):
                coordinates.append(list([dc.x + (i/10), dc.y + (i/10)]))

        return np.array(coordinates)

    @staticmethod
    def get_nodes(dcs):
        nodes = list()

        for dc in dcs:
            for i in range(10):
                nodes.append('Datacenter: ' + dc.name + ', Server: ' + str(i + 1))

        return nodes
