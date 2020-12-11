import unittest
from bst import BinarySearchTree

class BSTTestCase(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.add(20, "Value for 20")
        self.bst.add(12, "Value for 12")
        self.bst.add(3, "Value for 3")
        self.bst.add(7, "Value for 7")
        self.bst.add(29, "Value for 29")
        self.bst.add(11, "Value for 11")
        self.bst.add(33, "Value for 33")
        self.bst.add(19, "Value for 19")
        self.bst.add(56, "Value for 56")
        self.bst.add(27, "Value for 27")
        self.bst.add(39, "Value for 39")

        self.bst2 = BinarySearchTree()
        self.bst2.add(1, "Value for 1")
        self.bst2.add(2, "Value for 2")
        self.bst2.add(3, "Value for 3")
        self.bst2.add(4, "Value for 4")
        self.bst2.add(5, "Value for 5")
    
    def test_add(self):

        self.assertEqual(self.bst.size(), 11)
        self.assertEqual(self.bst2.size(), 5)

        self.bst.add(11, "Value for 11")
        self.assertEqual(self.bst.size(), 12)
        self.assertEqual(self.bst.search(11), "Value for 11")

        self.bst2.add(6, "Value for 6")
        self.assertEqual(self.bst2.size(), 6)
        self.assertEqual(self.bst2.search(6), "Value for 6")

    def test_inorder(self):
        self.assertListEqual(self.bst.inorder_walk(), [3, 7, 11, 12, 19, 20, 27, 29, 33, 39, 56])

        self.assertListEqual(self.bst2.inorder_walk(), [1, 2, 3, 4, 5])
        self.bst2.add(6, "Value for 6")
        self.assertListEqual(self.bst2.inorder_walk(), [1, 2, 3, 4, 5, 6])

    def test_postorder(self):
        self.assertListEqual(self.bst.postorder_walk(), [11, 7, 3, 19, 12, 27, 39, 56, 33, 29, 20])

        self.assertListEqual(self.bst2.postorder_walk(), [5, 4, 3, 2, 1])
        self.bst2.add(6, "Value for 6")
        self.assertListEqual(self.bst2.postorder_walk(), [6, 5, 4, 3, 2, 1])

    def test_preorder(self):
        self.assertListEqual(self.bst.preorder_walk(), [20, 12, 3, 7, 11, 19, 29, 27, 33, 56, 39])

        self.assertListEqual(self.bst2.preorder_walk(), [1, 2, 3, 4, 5])
        self.bst2.add(6, "Value for 6")
        self.assertListEqual(self.bst2.preorder_walk(), [1, 2, 3, 4, 5, 6])
    
    def test_search(self):
        self.assertEqual(self.bst.search(3), "Value for 3")
        self.assertFalse(self.bst2.search(0))

        self.bst2.add(6, "Value for 6")
        self.assertEqual(self.bst2.search(6), "Value for 6")

    def test_remove(self):
        self.bst.remove(27)
        self.assertEqual(self.bst.size(), 10)

        self.bst2.remove(3)
        self.assertListEqual(self.bst2.inorder_walk(), [1, 2, 4, 5])
        self.assertListEqual(self.bst2.preorder_walk(), [1, 2, 4, 5])
        self.assertListEqual(self.bst2.postorder_walk(), [5, 4, 2, 1])


    def test_smallest(self):
        self.assertTupleEqual(self.bst.smallest(), (3, "Value for 3"))

        self.assertTupleEqual(self.bst2.smallest(), (1, "Value for 1"))
        self.bst2.add(0, "Value for 0")
        self.assertTupleEqual(self.bst2.smallest(), (0, "Value for 0"))

    def test_largest(self):
        self.assertTupleEqual(self.bst.largest(), (56, "Value for 56"))
        self.bst.add(57, "Value for 57")
        self.assertTupleEqual(self.bst.largest(), (57, "Value for 57"))

        self.assertTupleEqual(self.bst2.largest(), (5, "Value for 5"))
        self.bst2.remove(5)
        self.assertTupleEqual(self.bst2.largest(), (4, "Value for 4"))

if __name__ == "__main__":
    unittest.main()    