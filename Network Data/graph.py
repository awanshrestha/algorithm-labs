import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import collections

def importGraph(url):
    header_list = ["a", "b", "w"]
    E = pd.read_csv(url, sep=" ", header=None, names=header_list)
    G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
    return G

def plotGraph(G):
    nx.draw(G)
    plt.show()

def getAvgDegree(E, N):
    avg = (2 * E) / N 
    return int(avg)

def getAvgDegreeGL(G):
    count = 0
    for v in G.nodes:
        count +=  nx.degree(G, v)
    v = nx.number_of_nodes(G)
    avg = count / v
    return int(avg)

def getDensity(E, N):
    if N > 1:
        density = ( 2 * E ) / ( N * ( N - 1 ))
        return round(density, 5)
    else:
        return 0

def getDiameter(G):
    if(nx.is_connected(G)):
        return nx.diameter(G)
    else:
        return 'Graph is not connected.'

def getClusteringCoeff(G):
    clusters = []
    for node in G.nodes():
        neighbors = [neighbor for neighbor in G.neighbors(node)]
        ki = len(neighbors)
        subgraph = nx.subgraph(G, neighbors)
        ei = subgraph.number_of_edges()
        
        if ki!= 0 and ki!=1:
            ci = (2 * ei) / ( ki * (ki - 1))
        else:
            ci = 0
        clusters.append(ci)
    
    clusteringCoeff = sum(clusters) / len(clusters)
    return round(clusteringCoeff, 5)                       

def printAll(N, E, avgerageDegree, density, diameter, clusteringCoeff):
    print('The number of nodes is ', N)
    print('The number of edges is ', E)
    print('The average degree is: ', avgerageDegree)
    print('The density is: ', density)
    print('The diameter is: ', diameter)
    print('The clustering coefficient is: ', clusteringCoeff)

def plotDistribution(G):
    sequence = sorted([d for n, d in G.degree()], reverse = True) 
    count = collections.Counter(sequence)
    degree, cnt = zip(*count.items())

    a, ax = plt.subplots()
    plt.bar(degree, cnt, color="g")

    plt.title("Degree Distribution")
    plt.ylabel("Number")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.5 for d in degree])
    ax.set_xticklabels(degree)

    plt.show()