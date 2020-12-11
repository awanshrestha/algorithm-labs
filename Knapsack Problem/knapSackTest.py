import unittest
from knapSack import dynamic, bruteforce, greedy, bruteforce_fractional

class TestBruteForce(unittest.TestCase):

    def setUp(self):
        self.p = [100, 20, 60, 40] 
        self.w = [3, 2, 4, 1] 
        self.m = 5

    def test_bruteforce(self):
        self.assertEqual( bruteforce(self.p, self.w, self.m), ('1001', 140) )
    
    def test_bruteforce_fractional(self):
        self.assertEqual( bruteforce_fractional(self.p, self.w, self.m), ([1, 0 , 0.25, 1], 155) )

    def test_greedy(self):
        self.assertEqual( greedy(self.p, self.w, self.m), ([1, 0, 0.25, 1], 155) )

    def test_dynamic(self):
        self.assertEqual( dynamic(self.p, self.w, self.m), ('1001', 140) )

if __name__ == "__main__":
    unittest.main()