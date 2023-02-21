import unittest
from datetime import date
# helpful information about unittests in python
# https://docs.python.org/3/library/unittest.html
from random import randint
import inspect

from tree_node import TreeNode
from bst import BinarySearchTree

arrList1 = [5, 18, 1, 8, 14, 16, 13, 3]
arrList2 = [10, 5, 12, 3]
arrCompleteBST = [5, 18, 3, 8, 1, 19, 4]
arrList1inorder = ["1", "3", "5", "8", "13", "14", "16", "18"]
arrList1preorder = ["5", "1", "3", "18", "8", "14", "13", "16"]
arrList1postorder = ["3", "1", "13", "16", "14", "8", "18", "5"]
arrListWithDuplicates = [5, 18, 1, 8, 14, 16, 13, 3, 8]


def create_bst(dim):
    bst = BinarySearchTree()
    for i in range(0, dim):
        bst.insert(key=i, value=str(randint(0, dim)))


def create_bst_from_list(list_):
    bst_solution = BinarySearchTree()
    for k in list_:
        bst_solution.insert(key=k, value=str(k))
    return bst_solution


def create_list_from_file(filename):
    with open(filename, 'r') as fp:
        list_ = []
        for item in fp:
            list_.append(int(item))
    return list_


def insert_list_helper(list_):
    bst = BinarySearchTree()
    for i in list_:
        bst.insert(key=i, value=str(i))
    return bst


class UnitTestTemplate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    ####################################################
    # Definition of test cases
    ####################################################

    def test_insert(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree()
        bst.insert(key=5, value="5")
        bst.insert(key=18, value="18")
        bst.insert(key=1, value="1")
        bst.insert(key=8, value="8")
        bst.insert(key=14, value="14")
        bst.insert(key=16, value="16")
        bst.insert(key=13, value="13")
        bst.insert(key=3, value="3")

        self.assertEqual(5, bst._root.key, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertEqual(1, bst._root.left.key, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertIsNone(bst._root.left.left, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertEqual(3, bst._root.left.right.key, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertIsNone(bst._root.left.right.left,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertIsNone(bst._root.left.right.right,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertEqual(18, bst._root.right.key, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertIsNone(bst._root.right.right, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertEqual(8, bst._root.right.left.key, "Incorrect tree after insert: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        self.assertIsNone(bst._root.right.left.left,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertEqual(14, bst._root.right.left.right.key,
                         "Incorrect tree after insert: " + self.print_tree(
                             bst._root) + " should be: " + self.print_tree(
                             bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertEqual(16, bst._root.right.left.right.right.key,
                         "Incorrect tree after insert: " + self.print_tree(
                             bst._root) + " should be: " + self.print_tree(
                             bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertEqual(13, bst._root.right.left.right.left.key,
                         "Incorrect tree after insert: " + self.print_tree(
                             bst._root) + " should be: " + self.print_tree(
                             bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertIsNone(bst._root.right.left.right.right.left,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertIsNone(bst._root.right.left.right.right.right,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertIsNone(bst._root.right.left.right.left.left,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))
        self.assertIsNone(bst._root.right.left.right.left.right,
                          "Incorrect tree after insert: " + self.print_tree(
                              bst._root) + " should be: " + self.print_tree(
                              bst_solution.get_root()) + "for insert sequence " + str(arrList1))

    def test_insert_duplicates(self):
        bst = BinarySearchTree()
        bst.insert(key=1, value="1")
        with self.assertRaises(KeyError):
            bst.insert(key=1, value="1")

    def test_insert_with_size(self):
        bst = BinarySearchTree()
        bst.insert(key=5, value="5")
        self.assertEqual(1, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(1) + ") after insert")
        bst.insert(key=18, value="18")
        self.assertEqual(2, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(2) + ") after insert")
        bst.insert(key=1, value="1")
        self.assertEqual(3, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(3) + ") after insert")
        bst.insert(key=8, value="8")
        self.assertEqual(4, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(4) + ") after insert")
        bst.insert(key=14, value="14")
        self.assertEqual(5, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(5) + ") after insert")
        bst.insert(key=16, value="16")
        self.assertEqual(6, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(6) + ") after insert")
        bst.insert(key=13, value="13")
        self.assertEqual(7, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(7) + ") after insert")
        bst.insert(key=3, value="3")
        self.assertEqual(8, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(8) + ") after insert")

    def test_insert_duplicates_with_size(self):
        bst = create_bst_from_list(arrList1)
        with self.assertRaises(KeyError):
            bst.insert(key=1, value="1")
        self.assertEqual(8, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(
            8) + ") after insert " + str(arrList1) + " (with inserting 1 twice)")

    def test_insert_none(self):
        bst = BinarySearchTree()
        with self.assertRaises(ValueError, msg="ERROR: Tree does not raise an exception when a None item is inserted"):
            bst.insert(None, None)
        with self.assertRaises(ValueError,
                               msg="ERROR: Tree does not raise an exception when an item with None key is inserted"):
            bst.insert(key=None, value="1")

    def test_depth(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size
        self.assertEqual(0, bst.find(5).depth, "ERROR: Node depth for key = 5 (" + str(
            bst.find(5).depth) + ") does not match the expected node depth (" + str(
            0) + ") for insert sequence " + str(arrList1))
        self.assertEqual(1, bst.find(18).depth,
                         "ERROR: Node depth for key = 18 (" + str(
                             bst.find(18).depth) + ") does not match the expected node depth (" + str(
                             1) + ") for insert sequence " + str(arrList1))
        self.assertEqual(1, bst.find(1).depth, "ERROR: Node depth for key = 1 (" + str(
            bst.find(1).depth) + ") does not match the expected node depth (" + str(
            1) + ") for insert sequence " + str(arrList1))
        self.assertEqual(2, bst.find(8).depth, "ERROR: Node depth for key = 8 (" + str(
            bst.find(8).depth) + ") does not match the expected node depth (" + str(
            2) + ") for insert sequence " + str(arrList1))
        self.assertEqual(2, bst.find(3).depth, "ERROR: Node depth for key = 3 (" + str(
            bst.find(3).depth) + ") does not match the expected node depth (" + str(
            2) + ") for insert sequence " + str(arrList1))
        self.assertEqual(3, bst.find(14).depth,
                         "ERROR: Node depth for key = 14 (" + str(
                             bst.find(14).depth) + ") does not match the expected node depth (" + str(
                             3) + ") for insert sequence " + str(arrList1))
        self.assertEqual(4, bst.find(13).depth,
                         "ERROR: Node depth for key = 13 (" + str(
                             bst.find(13).depth) + ") does not match the expected node depth (" + str(
                             4) + ") for insert sequence " + str(arrList1))
        self.assertEqual(4, bst.find(16).depth,
                         "ERROR: Node depth for key = 16 (" + str(
                             bst.find(16).depth) + ") does not match the expected node depth (" + str(
                             4) + ") for insert sequence " + str(arrList1))

    def test_find(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size
        self.assertEqual(5, bst.find(5).key, "ERROR: find() does not return correct value for key = 5: was: (" + str(
            bst.find(5)) + ") expected: 5 for insert sequence " + str(arrList1))
        self.assertEqual(18, bst.find(18).key, "ERROR: find() does not return correct value for key = 18: was: (" + str(
            bst.find(18)) + ") expected: 18 for insert sequence " + str(arrList1))
        self.assertEqual(1, bst.find(1).key, "ERROR: find() does not return correct value for key = 1: was: (" + str(
            bst.find(1)) + ") expected: 1 for insert sequence " + str(arrList1))
        self.assertEqual(8, bst.find(8).key, "ERROR: find() does not return correct value for key = 8: was: (" + str(
            bst.find(8)) + ") expected: 8 for insert sequence " + str(arrList1))
        self.assertEqual(14, bst.find(14).key, "ERROR: find() does not return correct value for key = 514 was: (" + str(
            bst.find(14)) + ") expected: 14 for insert sequence " + str(arrList1))
        self.assertEqual(16, bst.find(16).key, "ERROR: find() does not return correct value for key = 16: was: (" + str(
            bst.find(16)) + ") expected: 16 for insert sequence " + str(arrList1))
        self.assertEqual(13, bst.find(13).key, "ERROR: find() does not return correct value for key = 13: was: (" + str(
            bst.find(13)) + ") expected: 13 for insert sequence " + str(arrList1))
        self.assertEqual(3, bst.find(3).key, "ERROR: find() does not return correct value for key = 3: was: (" + str(
            bst.find(3)) + ") expected: 3 for insert sequence " + str(arrList1))

    def test_find_non_existing_key(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size
        with self.assertRaises(KeyError):
            bst.find(2)

    def test_find_none_key(self):
        bst = BinarySearchTree()
        with self.assertRaises(ValueError, msg="ERROR: find(None) did not raise an exception"):
            bst.find(None)

    def test_remove(self):
        bst_solution = create_bst_from_list(arrList1)  # [5, 18, 1, 8, 14, 16, 13, 3]
        temp_tree = create_bst_from_list(arrList1)
        bst = BinarySearchTree(temp_tree.get_root())
        bst._size = bst_solution.size

        bst_solution.remove(5)
        bst.remove(5)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 5: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(14)
        bst.remove(14)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 14: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(8)
        bst.remove(8)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 8: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(16)
        bst.remove(16)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 16: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(13)
        bst.remove(13)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 13: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(1)
        bst.remove(1)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 1: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(18)
        bst.remove(18)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove for key = 18: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))
        bst_solution.remove(3)
        bst.remove(3)
        self.assertTrue(bst.is_valid, "Incorrect tree after remove: " + self.print_tree(
            bst._root) + " should be: " + self.print_tree(bst_solution.get_root()) + "for insert sequence " + str(
            arrList1))

        self.assertIsNone(bst._root, "Incorrect tree after remove of all values: " + self.print_tree(
            bst._root) + "for insert sequence " + str(
            arrList1))

    def test_remove_None(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        with self.assertRaises(ValueError, msg="ERROR: remove(None) did not raise an exception"):
            bst.remove(None)

    def test_remove_non_existing_key(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size
        with self.assertRaises(KeyError, msg="ERROR: Remove non existing key did not raise KeyError for insert "
                                             "sequence " + str(arrList1)):
            bst.remove(20)

    def test_size_with_remove(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size
        bst.remove(1)
        self.assertEqual(7, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(
            7) + ") after remove for insert sequence " + str(arrList1))
        bst.remove(8)
        self.assertEqual(6, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(
            6) + ") after remove for insert sequence " + str(arrList1))
        bst.remove(5)
        self.assertEqual(5, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(
            5) + ") after remove for insert sequence " + str(arrList1))

    def test_size_with_remove_non_existing(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size

        with self.assertRaises(KeyError):
            bst.remove(20)
        self.assertEqual(8, bst.size, "ERROR: Tree size (" + str(
            bst.size) + ") does not match the expected tree size (" + str(
            8) + ") after remove of non existing key for insert sequence " + str(arrList1))

    def test_inorder(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        bst_inorder_student = bst.inorder(bst_solution.get_root())
        inorder_list = []
        self.assertTrue(inspect.isgenerator(bst_inorder_student), "inorder does not yield a generator object!")
        for x in bst_inorder_student:
            inorder_list.append(x.value)
        self.assertEqual(inorder_list, arrList1inorder,
                         "ERROR: inorder returns incorrect array (" + str(
                             bst_inorder_student) + ") should be: " + str(arrList1inorder))

    def test_preorder(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        bst_preorder_student = bst.preorder(bst_solution.get_root())
        preorder_list = []
        self.assertTrue(inspect.isgenerator(bst_preorder_student), "preorder does not yield a generator object!")
        for x in bst_preorder_student:
            preorder_list.append(x.value)
        self.assertEqual(preorder_list, arrList1preorder,
                         "ERROR: preorder returns incorrect array (" + str(
                             bst_preorder_student) + ") should be: " + str(arrList1preorder))

    def test_postorder(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        bst_postorder_student = bst.postorder(bst_solution.get_root())
        postorder_list = []
        self.assertTrue(inspect.isgenerator(bst_postorder_student), "preorder does not yield a generator object!")
        for x in bst_postorder_student:
            postorder_list.append(x.value)
        self.assertEqual(postorder_list, arrList1postorder,
                         "ERROR: postorder returns incorrect array (" + str(
                             bst_postorder_student) + ") should be: " + str(arrList1postorder))

    def test_get_parent(self):
        bst_solution = create_bst_from_list(arrList2)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        self.assertEqual(10, bst.find(5).parent.key, "ERROR: get_parent returned wrong parent (" + str(
            bst.find(5).parent.key) + ") for key = 5. Should be 10 for insert sequence " + str(arrList2))
        self.assertEqual(10, bst.find(12).parent.key, "ERROR: get_parent returned wrong parent (" + str(
            bst.find(12).parent.key) + ") for key = 12. Should be 10 for insert sequence " + str(arrList2))
        self.assertEqual(5, bst.find(3).parent.key, "ERROR: get_parent returned wrong parent (" + str(
            bst.find(3).parent.key) + ") for key = 3. Should be 5 for insert sequence " + str(arrList2))

    def test_get_parent_of_root(self):
        bst_solution = create_bst_from_list(arrList2)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size
        self.assertIsNone(bst.find(10).parent,
                          "ERROR: get_parent of root returned " + str(
                              bst.find(10).parent) + " but should be None for insert sequence " + str(arrList2))

    def test_is_root(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size

        self.assertTrue(bst.find(5).parent is None,
                        "ERROR: is_root returned False for key = 5 but should be True for insert sequence " + str(
                            arrList1))
        self.assertFalse(bst.find(18).parent is None,
                         "ERROR: is_root returned True for key = 18 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(1).parent is None,
                         "ERROR: is_root returned True for key = 1 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(8).parent is None,
                         "ERROR: is_root returned True for key = 8 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(14).parent is None,
                         "ERROR: is_root returned False for key = 14 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(16).parent is None,
                         "ERROR: is_root returned True for key = 16 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(13).parent is None,
                         "ERROR: is_root returned True for key = 13 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(3).parent is None,
                         "ERROR: is_root returned True for key = 3 but should be False for insert sequence " + str(
                             arrList1))

    def test_is_internal(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size

        self.assertTrue(bst.find(5).is_internal,
                        "ERROR: is_internal returned False for key = 5 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(18).is_internal,
                        "ERROR: is_internal returned False for key = 18 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(1).is_internal,
                        "ERROR: is_internal returned False for key = 1 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(8).is_internal,
                        "ERROR: is_internal returned False for key = 8 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(14).is_internal,
                        "ERROR: is_internal returned False for key = 14 but should be True for insert sequence " + str(
                            arrList1))
        self.assertFalse(bst.find(16).is_internal,
                         "ERROR: is_internal returned True for key = 16 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(13).is_internal,
                         "ERROR: is_internal returned True for key = 13 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(3).is_internal,
                         "ERROR: is_internal returned True for key = 3 but should be False for insert sequence " + str(
                             arrList1))

    def test_is_external(self):
        bst_solution = create_bst_from_list(arrList1)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst.size

        self.assertFalse(bst.find(5).is_external,
                         "ERROR: is_external returned True for key = 5 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(18).is_external,
                         "ERROR: is_external returned True for key = 18 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(1).is_external,
                         "ERROR: is_external returned True for key = 1 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(8).is_external,
                         "ERROR: is_external returned True for key = 8 but should be False for insert sequence " + str(
                             arrList1))
        self.assertFalse(bst.find(14).is_external,
                         "ERROR: is_external returned True for key = 14 but should be False for insert sequence " + str(
                             arrList1))
        self.assertTrue(bst.find(16).is_external,
                        "ERROR: is_external returned False for key = 16 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(13).is_external,
                        "ERROR: is_external returned False for key = 13 but should be True for insert sequence " + str(
                            arrList1))
        self.assertTrue(bst.find(3).is_external,
                        "ERROR: is_external returned False for key = 3 but should be True for insert sequence " + str(
                            arrList1))

    # note: this testcase might take around 30 seconds
    def test_runtime_comparison_check_bst_with_pregen_list(self):
        test_list = None
        try:
            test_list = create_list_from_file("testListWithoutDuplicates.txt")
        except FileNotFoundError:
            print("@Tutor: runtimeComparison() could not be tested as testfile could not be loaded "
                  "(testListWithoutDuplicates.txt). Pls check path and test again.")
        key = int(test_list[len(test_list) - 1])
        bst = insert_list_helper(test_list)
        result = bst.find_comparison(key)
        self.assertEqual(53, result[1], "ERROR: runtimeComparison() returns wrong number of comparisons (" + str(
            result[0]) + ") for searching the last key of a given list in a BST with 1000000 values should be: 53")

    # note: this testcase might take around 30 seconds
    def test_runtime_comparison_check_list_with_pregen_list(self):
        test_list = None
        try:
            test_list = create_list_from_file("testListWithoutDuplicates.txt")
        except FileNotFoundError:
            print("@Tutor: runtimeComparison() could not be tested as testfile could not be loaded "
                  "(testListWithoutDuplicates.txt). Pls check path and test again.")
        key = int(sorted(test_list)[len(test_list) - 1])
        bst = insert_list_helper(test_list)
        result = bst.find_comparison(key)
        self.assertEqual(len(test_list), result[0],
                         "ERROR: runtimeComparison() returns wrong number of comparisons (" + str(result[1]) +
                         ") for searching the last key of a given list in a BST with 1000000 values should be: " +
                         str(len(test_list)))

    def test_runtime_comparison_assignment_example_BST_check(self):
        test_list = [8, 17, 10, 3, 1]
        bst = insert_list_helper(test_list)
        result = bst.find_comparison(3)
        self.assertEqual(3, result[1], "runtimeComparison() returns wrong number of comparisons (" + str(
            result[0]) + ") for searching key '3' in a BST base on the list sequence: 8,17,10,3,1. should be 3")

    # adapted because now if does not compare to the initial list, but to the in order list
    def test_runtime_comparison_assignment_example_list_check(self):
        test_list = [8, 17, 10, 3, 1]

        bst = insert_list_helper(test_list)
        result = bst.find_comparison(3)
        self.assertEqual(2, result[0], "runtimeComparison() returns wrong number of comparisons (" + str(
            result[1]) + ") for searching key '3' in a list base on the sequence: 8,17,10,3,1. should be 2")

    def test_runtime_comparison_sorted_list(self):
        bst = BinarySearchTree()
        test_list = []
        num_keys = 10
        key = num_keys - 1

        for i in range(0, num_keys):
            test_list.append(i)
            bst.insert(key=i, value=str(i))
        result = bst.find_comparison(key)

        self.assertEqual(len(test_list) * 2 - 1, result[1],
                         "runtimeComparison() returns wrong number of comparisons (" + str(result[0]) +
                         ") for search key 9 in a BST base on the sequence: 0,1,2,3,4,5,6,7,8,9. should be: " +
                         str(len(test_list) * 2 - 1))
        self.assertEqual(len(test_list), result[0],
                         "runtimeComparison() returns wrong number of comparisons (" + str(result[1]) +
                         ") for search key 9 in a list base on the sequence: 0,1,2,3,4,5,6,7,8,9. should be: " +
                         str(len(test_list)))

    def test_is_valid_true(self):
        arr = [13, 5, 18, 1, -8, 14, 16, -13, 3]
        bst_solution = create_bst_from_list(arr)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size

        self.assertTrue(bst.is_valid,
                        "ERROR: is_complete returned False but should be True for input: " + str(arr))

    def test_is_valid_false(self):
        root13 = TreeNode(key=13, value="13")
        node5 = TreeNode(key=5, value="5")
        node18 = TreeNode(key=18, value="18")
        node1 = TreeNode(key=1, value="1")
        node8 = TreeNode(key=18, value="8")
        node14 = TreeNode(key=14, value="14")
        node16 = TreeNode(key=16, value="16")
        node13 = TreeNode(key=13, value="13")
        node3 = TreeNode(key=3, value="3")
        root13.left = node5
        root13.right = node18
        node5.left = node1
        node5.right = node8
        node1.right = node3
        node8.right = node13
        node18.left = node14
        node13.right = node16

        bst = BinarySearchTree(root13)
        bst._size = 9
        self.assertFalse(bst.is_valid,
                         "ERROR: is_valid returned True but should be False using tree: " + self.print_tree(root13))

    def test_return_min_key(self):
        bst_solution = create_bst_from_list(arrCompleteBST)
        bst = BinarySearchTree(bst_solution.get_root())
        bst._size = bst_solution.size

        res = bst.return_min_key().key
        self.assertEqual(1, res, "ERROR: return_min_key returned wrong min key (" + str(res) + ") but should be \"1\"")

    ####################################################
    # Helper Methods
    ####################################################

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def resolve_method_name_from_id(self, argument):
        idx = self.id().rfind('.')
        # print("****"+self.id()[idx+1:])
        return self.id()[idx + 1:]

    def print_tree(self, tree_root):
        if tree_root is not None:
            ret_str = "\n"
            lines, _, _, _ = self.display_aux(tree_root)
            for line in lines:
                ret_str += line + "\n"
                # print(line)
            return ret_str + "\n"
        else:
            return ""

    def display_aux(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = self.display_aux(cur_node.left)
            s = '%s' % cur_node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = self.display_aux(cur_node.right)
            s = '%s' % cur_node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display_aux(cur_node.left)
        right, m, q, y = self.display_aux(cur_node.right)
        s = '%s' % cur_node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    unittest.main()
