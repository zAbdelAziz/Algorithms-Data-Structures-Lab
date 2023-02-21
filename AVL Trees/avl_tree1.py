from avl_node import AVLNode


class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.height = 0
        self.size = 0
        self.preorder = []

    def get_tree_root(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def get_tree_height(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        return self.height if self.root else -1

    def get_node_height(self, node):
        return node.height if node else 0

    def get_height_difference(self, node):
        return self.get_node_height(node.left) - self.get_node_height(node.right) if node else 0

    def get_tree_size(self):
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def to_array(self):
        """Yields an array representation of the tree's values (pre-order).
        :return Array representation of the tree values.
        """
        self._preorder(self.root)
        order = self.preorder
        self.preorder = []
        return order

    def _preorder(self, node):
        if not node:
            return
        self.preorder.append(node.key)
        self._preorder(node.left)
        self._preorder(node.right)

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError('Please Assign a key to find!')

        r = self._find_node(key, self.root)
        if r:
            # return r.key
            return r.value
        else:
            return None


    def _find_node(self, key, node):
        """Returns node with given key.
        :param key: Key to search.
        :param node: starting node to search from.
        :return Corresponding node if key was found, None otherwise.
        """
        if node:
            # Traverse Left
            if key < node.key:
                return self._find_node(key, node.left)
            # Traverse Right
            elif key > node.key:
                return self._find_node(key, node.right)
            # Key Found
            elif key == node.key:
                return node
        else:
            return None

    def insert(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None or value is None:
            raise ValueError('Missing Key or Value!')

        if self._find_node(key, self.root):
            return False

        if self.root:
            node = self._insert(key, value, self.root)
        else:
            self.root = AVLNode(key, value)
            self.size += 1

        if self._find_node(key, self.root):
            return True
        # else:
        #     return False

    def _insert(self, key, value, node):
        """Inserts a new node into AVL tree recursively.
        :param key: Key of the new node.
        :param value: Data of the new node.
        :param node: Root Node of the Subtree.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        # BST Insert
        if not node:
            self.size += 1
            return AVLNode(key, value)
        if key < node.key:
            left_node = self._insert(key, value, node.left)
            node.left = left_node
            left_node.parent = node
        elif key > node.key:
            right_node = self._insert(key, value, node.right)
            node.right = right_node
            right_node.parent = node
        else:
            # print('Duplicate')
            return None
        # Update Height
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

        # Calculate Height Difference
        height_diff = self.get_height_difference(node)

        return self.balance(node)
        # # Balance Sub Tree
        # if height_diff > 1:
        #     if key < node.left.key:
        #         return self.rotate_right(node)
        #     else:
        #         node.left = self.rotate_left(node.left)
        #         return self.rotate_right(node)
        # if height_diff < -1:
        #     if key > node.right.key:
        #         return self.rotate_left(node)
        #     else:
        #         node.right = self.rotate_right(node.right)
        #         return self.rotate_left(node)
        # return node

    def remove_by_key(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        pass



    def balance(self, node):
        if node.height_diff < -1:
            if node.right.height_diff > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            else:
                return self.rotate_left(node)
        elif node.height_diff > 1:
            if node.left.height_diff < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            else:
                return self.rotate_right(node)
        else:
            return node



    def rotate_right(self, z):
        y = z.left
        t = y.right

        y.right = z
        y.parent = z.parent
        z.parent = y

        z.left = t
        if t:
            t.parent = z

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
        z.height_diff = self.get_node_height(z.left) - self.get_node_height(z.right)

        y.height = 1 + max(self.get_node_height(y.left), self.get_node_height(y.right))
        y.height_diff = self.get_node_height(y.left) - self.get_node_height(y.right)

        return y



    def rotate_left(self, z):
        y = z.right
        t = y.left

        y.left = z
        y.parent = z.parent
        z.parent = y

        z.right = t
        if t:
            t.parent = z

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
        z.height_diff = self.get_node_height(z.left) - self.get_node_height(z.right)

        y.height = 1 + max(self.get_node_height(y.left), self.get_node_height(y.right))
        y.height_diff = self.get_node_height(y.left) - self.get_node_height(y.right)

        return y



    # def rotate_left(self, z):
    #     y = z.right
    #     t1 = y.left
    #
    #     y.left = z
    #     z.right = t1
    #
    #     height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
    #     z.height, y.height = height, height
    #     print(self.to_array())
    #     return y
    #
    # def rotate_right(self, z):
    #
    #     y = z.left
    #     t2 = y.right
    #
    #     y.right = z
    #     z.left = t2
    #
    #     height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
    #     z.height, y.height = height, height
    #     return y



# tree = AVLTree()
# tree.insert(5,0)
# tree.insert(18,0)
# tree.insert(2,0)
# tree.insert(8,0)
# tree.insert(14,1)
# print(tree.to_array())
#
# print(tree.root.key)
# print(tree.root.left.key)
# print(tree.root.right.key)
