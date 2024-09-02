import unittest
from main import *

class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        node = Node(1, 'value', 'red')
        self.assertEqual(node.key, 1)
        self.assertEqual(node.value, 'value')
        self.assertEqual(node.color, 'red')
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertIsNone(node.parent)

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert(self):
        self.tree.insert(10, 'value10')
        self.tree.insert(20, 'value20')
        self.tree.insert(30, 'value30')
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.color, 'black')

    def test_search(self):
        self.tree.insert(10, 'value10')
        self.tree.insert(20, 'value20')
        self.tree.insert(30, 'value30')
        node = self.tree.search(20)
        self.assertEqual(node.key, 20)
        self.assertEqual(node.value, 'value20')

    def test_delete(self):
        self.tree.insert(10, 'value10')
        self.tree.insert(20, 'value20')
        self.tree.insert(30, 'value30')
        self.tree.delete(20)
        node = self.tree.search(20)
        self.assertEqual(node, self.tree.NIL)

    def test_update(self):
        self.tree.insert(10, 'value10')
        self.tree.update(10, 'new_value10')
        node = self.tree.search(10)
        self.assertEqual(node.value, 'new_value10')
        self.tree.update(20, 'value20')
        node = self.tree.search(20)
        self.assertEqual(node.value, 'value20')

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_insert(self):
        self.hash_table.insert('key1', 'value1')
        self.hash_table.insert('key2', 'value2')
        self.assertEqual(self.hash_table.search('key1'), 'value1')
        self.assertEqual(self.hash_table.search('key2'), 'value2')

    def test_search(self):
        self.hash_table.insert('key1', 'value1')
        self.hash_table.insert('key2', 'value2')
        self.assertEqual(self.hash_table.search('key1'), 'value1')
        self.assertEqual(self.hash_table.search('key2'), 'value2')
        self.assertIsNone(self.hash_table.search('key3'))

    def test_delete(self):
        self.hash_table.insert('key1', 'value1')
        self.hash_table.insert('key2', 'value2')
        self.hash_table.delete('key1')
        self.assertIsNone(self.hash_table.search('key1'))
        self.assertEqual(self.hash_table.search('key2'), 'value2')

    def test_update(self):
        self.hash_table.insert('key1', 'value1')
        self.hash_table.update('key1', 'new_value1')
        self.assertEqual(self.hash_table.search('key1'), 'new_value1')
        self.hash_table.update('key2', 'value2')
        self.assertEqual(self.hash_table.search('key2'), 'value2')


class TestRedBlackTreeExtended(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert_fix_cases(self):
        # Case 1: Insert into an empty tree
        self.tree.insert(10, 'value10')
        self.assertEqual(self.tree.root.key, 10)
        self.assertEqual(self.tree.root.color, 'black')

        # Case 2: Insert creating a red-red violation, simple recoloring
        self.tree.insert(20, 'value20')
        self.tree.insert(30, 'value30')
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.color, 'black')
        self.assertEqual(self.tree.root.left.key, 10)
        self.assertEqual(self.tree.root.left.color, 'red')
        self.assertEqual(self.tree.root.right.key, 30)
        self.assertEqual(self.tree.root.right.color, 'red')

        # Case 3: Insert causing rotation and recoloring
        self.tree.insert(25, 'value25')
        self.tree.insert(40, 'value40')
        self.tree.insert(35, 'value35')
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.right.key, 30)
        self.assertEqual(self.tree.root.right.left.key, 25)
        self.assertEqual(self.tree.root.right.right.key, 40)
        self.assertEqual(self.tree.root.right.color, 'red')
        self.assertEqual(self.tree.root.right.right.color, 'black')

    def test_rotate_right(self):
        self.tree.insert(30, 'value30')
        self.tree.insert(20, 'value20')
        self.tree.insert(10, 'value10')
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.left.key, 10)
        self.assertEqual(self.tree.root.right.key, 30)

        self.tree.insert(25, 'value25')
        self.assertEqual(self.tree.root.right.left.key, 25)
        self.tree.insert(28, 'value28')
        self.tree.insert(35, 'value35')
        self.assertEqual(self.tree.root.right.left.key, 25)
        self.assertEqual(self.tree.root.right.right.key, 30)

    def test_delete_fix_cases(self):
        self.tree.insert(10, 'value10')
        self.tree.insert(20, 'value20')
        self.tree.insert(30, 'value30')
        self.tree.insert(5, 'value5')
        self.tree.insert(1, 'value1')
        self.tree.insert(15, 'value15')

        # Case 1: Deleting a red node
        self.tree.delete(1)
        self.assertIsNone(self.tree.search(1).key)

        # Case 2: Deleting a black node with a red child
        self.tree.delete(5)
        self.assertIsNone(self.tree.search(5).key)

        # Case 3: Deleting a black node with black children, causing double black
        self.tree.delete(20)
        self.assertIsNone(self.tree.search(20).key)

        # Case 4: Complex case causing multiple fixes
        self.tree.delete(30)
        self.assertIsNone(self.tree.search(30).key)
        self.tree.delete(10)
        self.assertIsNone(self.tree.search(10).key)
        self.tree.delete(15)
        self.assertIsNone(self.tree.search(15).key)
if __name__ == '__main__':
    unittest.main()