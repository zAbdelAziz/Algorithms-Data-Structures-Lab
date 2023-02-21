from avl_node import AVLNode


class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.height = 0
        self.size = 0
        self.preorder = []


# Root
    def get_tree_root(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root


# Height
    def get_tree_height(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        return self.root.height if self.root else -1

    def get_node_height(self, node):
        return node.height if node else -1

    # def get_height_difference(self, node): [Remove this - Only used once]
    #     return self.get_node_height(node.left) - self.get_node_height(node.right) if node else 0



# Size
    def get_tree_size(self):
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size



# Representation
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



# Search / Find
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




# Insert
    def insert(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        # print('inserting', key, 'into', self.to_array())
        if key is None or value is None:
            raise ValueError('Missing Key or Value!')

        # Returns False if Value exists [Stupid way - Replace in insert BST] (Can be removed after last update)
        # if self._find_node(key, self.root):
        #     return False

        # Insert New Node
        if self.root:
            return self._insert(key, value, self.root)
        else:
            self.root = AVLNode(key, value)
            self.size += 1

        # Returns True if Value was added [Further Validation - useless - remove]
        if self._find_node(key, self.root):
            return True


    def _insert(self, key, value, node):
        """Inserts a new node into AVL tree recursively. [BST Insert]
        :param key: Key of the new node.
        :param value: Data of the new node.
        :param node: Root Node of the Subtree.
        :calls validate_insert if the insert was successful, returns False otherwise.
        :returns False when node exists [replace the find in the main func]
        """
        if key < node.key:
            if node.left is None:
                node.left = AVLNode(key, value)
                node.left.parent = node
                self.validate_insert(node.left)
                self.size += 1
            else:
                self._insert(key, value, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = AVLNode(key, value)
                node.right.parent = node
                self.validate_insert(node.right)
                self.size += 1
            else:
                self._insert(key, value, node.right)
        else:
            return False


    def validate_insert(self, node, zyx=[]):
        # Stores X,Y,Z into Array to insert it recursively
        if node.parent == None:
            # Nothing to Validate
            return
        else:
            # Prepend to zyx
            zyx = [node] + zyx

        if abs(self.get_node_height(node.parent.left) - self.get_node_height(node.parent.right)) > 1:
            # prepend the parent to zyx then balance the node [Height Diff. is larger than 1]
            zyx = [node.parent] + zyx
            self.balance_node(zyx[0], zyx[1], zyx[2])
            return
        # self.update_height()          # Remove [Treat each Update on its own] (Reason -> validate_remove stuff)
        # Update Height
        if  node.height + 1 > node.parent.height:
            node.parent.height =  node.height + 1

        self.validate_insert(node.parent, zyx)







# Remove
    def remove_by_key(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError('Missing Key!')
        node = self._find_node(key, self.root)
        if not node:
            return False
        else:
            self.size -= 1
            return self._remove_node(node)



    def _remove_node(self, node):
        if node is None:
            return False

        parent = node.parent
        children = list(filter(None, [node.left, node.right]))

        # Leaf [Case 1]
        if len(children) == 0:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                parent.height = 1 + max(self.get_node_height(parent.left), self.get_node_height(parent.right))
                self.validate_remove(parent)

            else:
                self.root = None
            return True

        # 1 Child [Case 2]
        if len(children) == 1:
            child  = node.left if node.left else node.right
            if parent:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
            child.parent = parent

            if parent:
                parent.height = 1 + max(self.get_node_height(parent.left), self.get_node_height(parent.right))
                self.validate_remove(parent)
            if self.root:
                self.update_height()
            return True

        # 2 Children [Case 3]
        if len(children) == 2:
            leftmost_child = self.get_leftmost_node(node.right)
            node.key, node.value = leftmost_child.key, leftmost_child.value
            self._remove_node(leftmost_child)
            return True



    def validate_remove(self, node):
        if node and abs(self.get_node_height(node.left) - self.get_node_height(node.right)) > 1:
            y = self.max_height_node(node)
            x = self.max_height_node(y)
            self.balance_node(node, y, x)
        else:
            return
        self.validate_remove(node.parent)





# Node Balancing / Rotation
    # Balance Node Based on Cut/Link presented in the lecture [A little modification to reduce number of functions to be written]
    def balance_node(self, z, y, x):
        if y == z.left:
            if x == y.left:
                self.rotate_right(z)
            elif x == y.right:
                self.rotate_left(y)
                self.rotate_right(z)
        elif y == z.right:
            if x == y.right:
                self.rotate_left(z)
            elif x == y.left:
                self.rotate_right(y)
                self.rotate_left(z)
        else:
            raise TypeError('I should be chilling instead')

    # Left Rotate [Single] (Based on Lecture)
    def rotate_left(self, z):
        g_parent = z.parent
        y = z.right
        t1 = y.left

        y.left = z
        z.parent = y

        z.right = t1

        if t1 != None:
            t1.parent = z

        y.parent = g_parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
        y.height = 1 + max(self.get_node_height(y.left), self.get_node_height(y.right))

    # Right Rotate [Single] (Based on Lecture)
    def rotate_right(self, z):
        g_parent = z.parent
        y = z.left
        t2 = y.right

        y.right = z
        z.parent = y

        z.left = t2

        if t2 != None:
            t2.parent = z

        y.parent = g_parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_node_height(z.left), self.get_node_height(z.right))
        y.height = 1 + max(self.get_node_height(y.left), self.get_node_height(y.right))




# Helper Functions [For reuse allover the class]
    def get_leftmost_node(self, node):
        # returns left most child [For Deletion Purposes]
        current = node
        while current.left != None:
            current = current.left
        return current

    def max_height_node(self, node):
        # returns the node with largest height
        return node.left if self.get_node_height(node.left) >= self.get_node_height(node.right) else node.right

    def update_height(self):        # Reduce that code as much as possible
        self.root.height = 1 + self.max_height_node(self.root).height




# Work on Documentation More!!
