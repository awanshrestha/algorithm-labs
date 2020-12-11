import unittest
from graph import *

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.network = "data/small/mammalia-voles-plj-trapping-15.edges"
        self.graph = importGraph(self.network)
        self.N = nx.number_of_nodes(self.graph)
        self.E = nx.number_of_edges(self.graph)

    def test_nodes(self):
        self.assertEqual( self.N, 50 )

    def test_edges(self):
        self.assertEqual( self.E, 60 )

    def test_avg_degree(self):
        self.assertEqual( getAvgDegree(self.E, self.N), getAvgDegreeGL(self.graph) )
    
    def test_density(self):
        self.assertEqual( getDensity(self.E, self.N), round(nx.density(self.graph), 5) )

    def test_diameter(self):
        self.assertEqual( getDiameter(self.graph), 'Graph is not connected.' )

    def test_clustering_coeff(self):
        self.assertEqual( getClusteringCoeff(self.graph), round(nx.average_clustering(self.graph), 5))
    
   
if __name__ == "__main__":
    unittest.main()