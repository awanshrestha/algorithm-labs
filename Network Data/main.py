from graph import *

def run():
    # Data Credits: http://networkrepository.com/

    # smallNetwork = 'data/small/mammalia-voles-bhp-trapping-55.edges'
    # network1 = 'data/DD21.edges'
    # network2 = 'data/Erdos02.mtx'
    # network3 = 'data/ca-Erdos992.mtx'
    # network4 = 'data/bio-dmela.mtx'
    network5 = 'data/as-735.mtx'

    graph = importGraph(network5)

    plotGraph(graph)
    N = nx.number_of_nodes(graph)
    E = nx.number_of_edges(graph)
    avgerageDegree = getAvgDegree(E, N)
    density = getDensity(E, N)
    diameter = getDiameter(graph)
    clusteringCoeff = getClusteringCoeff(graph)

    printAll(N, E, avgerageDegree, density, diameter, clusteringCoeff)
    plotDistribution(graph)

if __name__ == '__main__':
    run()



