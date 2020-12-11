import unittest
from sorting import insertionSort
from sorting import mergeSort

class TestSorting(unittest.TestCase):
    
    def test_insertion_sort(self):
        input = [1, 20 , 10, 7, 12]
        result = [1, 7, 10, 12, 20]

        insertionSort(input)
        self.assertEqual(input, result)

    
    def test_merge_sort(self):
        input = [1, 20 , 10, 7, 12]
        result = [1, 7, 10, 12, 20]
        
        mergeSort(input, 0 , len(input) - 1)

        self.assertEqual(input, result)

if __name__ == "__main__":
    unittest.main()
