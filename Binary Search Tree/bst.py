from typing import Any, Generator, Tuple

from tree_node import TreeNode



class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.

        Raises:
            ValueError: root is not a TreeNode or not None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        if self._root and not isinstance(self._root, TreeNode):
            raise ValueError('Root is not a TreeNode')

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        self.validate_key(key)

        def insert_node(node, key):
            if not node.key == key:
                if node.key < key:
                    if node.right:
                        insert_node(node.right, key)
                    else:
                        inserted_node = TreeNode(key, value, parent=node)
                        node.right = inserted_node
                        self._size += 1
                        return inserted_node
                else:
                    if node.left:
                        insert_node(node.left, key)
                    else:
                        inserted_node = TreeNode(key, value, parent=node)
                        node.left = inserted_node
                        self._size += 1
                        return inserted_node
            else:
                raise KeyError('Key Already exists in the tree')

        if self._root:
            insert_node(self._root, key)
        else:
            self._root = TreeNode(key, value)
            self._size += 1
            return self._root


    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        self.validate_key(key)


        def search(node, key):
            if node.key == key:
                return node
            else:
                if node.right and node.key < key:
                    node = node.right
                    return search(node, key)
                elif node.left and node.key > key:
                    node = node.left
                    return search(node, key)
                else:
                    raise KeyError('Key Not Found')

        if self._root:

            if self._root.key == key:
                return self._root
            else:
                return search(self._root, key)

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        return self._size

    def __len__(self):
        return self._size

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        self.validate_key(key)
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        # self.validate_key(key)
        self.find(key)
        if len(self) == 1:
            self._root = None
        self.delete_node(self._root, key)
        self._size -= 1

    # Hint: The following 3 methods can be implemented recursively, and
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here:
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        if node.left:
            for n in self.inorder(node.left):
                yield n
        yield node
        if node.right:
            for n in self.inorder(node.right):
                yield n


    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        if node:
            yield node
        if node.left:
            for n in self.preorder(node.left):
                yield n
        if node.right:
            for n in self.preorder(node.right):
                yield n


    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        if node.left:
            for n in self.postorder(node.left):
                yield n
        if node.right:
            for n in self.postorder(node.right):
                yield n
        yield node


    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]:
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        return self.validate(self._root)

    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key (None if tree is empty)."""
        return self.get_min_node(self._root)

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self.preorder())

        def count_tree(node, key, c):
            if key == node.key:
                return c
            elif key < node.key:
                c += 2
                return count_tree(node.left, key, c)
            else:
                c += 2
                return count_tree(node.right, key, c)

        def count_list(key):
            cl = 1
            found = False
            while not found:
                if python_list[cl] == key:
                    found = True
                cl += 1
            return cl

        ct = count_tree(self._root, key, 1)


        return (count_list(key), ct)

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})" if self._root else 'BinarySearchTree has no Root'

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self):
        return self.inorder(self._root)

    def _preorder(self):
        return self.preorder(self._root)

    def _postorder(self):
        return self.postorder(self._root)

    def delete_node(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if not node.left:
                t = node.right
                node = None
                return t
            elif not node.right:
                t = node.left
                self._root = t if key == self._root.key else self._root
                node = None
                return t
            t = self.get_min_node(node.right)
            node.key = t.key
            node.right = self.delete_node(node.right, t.key)
        return node

    def validate_key(self, key):
        if not isinstance(key, int):
            raise ValueError('Key should be integer')

    def get_min_node(self, node):
        while node.left:
            node = self.get_min_node(node.left)
        return node

    def get_max_node(self, node):
        while node.right:
            node = self.get_max_node(node.right)
        return node

    def validate(self, node):
        if not self._root:
            return True
        inorder = [node.key for node in self.inorder(self._root)]
        sorter = sorted([node.key for node in self.inorder(self._root)])
        if not sorter == inorder:
            return False
        else:
            return True

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)
