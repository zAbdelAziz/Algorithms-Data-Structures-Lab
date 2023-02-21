from typing import Any


class TreeNode:

    def __init__(self, key: int, value: Any, right: 'TreeNode' = None,
                 left: 'TreeNode' = None, parent: 'TreeNode' = None):
        """Initialize TreeNode.

        Args:
            key (int): Key used for sorting the node into a BST.
            value (Any): Whatever data the node shall carry.
            right (TreeNode, optional): Node to the right, with a larger key. Defaults to None.
            left (TreeNode, optional): Node to the left, with a lesser key. Defaults to None.
            parent (TreeNode, optional): Parent node. Defaults to None.

        Raises:
            ValueError:
                - When any of the inputs are not of their fields type.
        """
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent
        if not isinstance(self.key, int):
            raise ValueError('Key Should be integer')
        if self.right and not isinstance(self.right, TreeNode):
            raise ValueError('right Should be a TreeNode')
        if self.left and not isinstance(self.left, TreeNode):
            raise ValueError('left Should be a TreeNode')
        if self.parent and not isinstance(self.parent, TreeNode):
            raise ValueError('parent Should be a TreeNode')


    def __repr__(self) -> str:
        return f"TreeNode({self.key}, {self.value})"

    @property
    def depth(self) -> int:
        """Return depth of the node, i.e. the number of parents/grandparents etc.

        Returns:
            int: Depth of node
        """
        parent = self.parent
        d = 0
        while parent:
            parent = parent.parent
            d += 1
        return d

    @property
    def is_external(self) -> bool:
        """Return if node is an external node (= leaf)."""
        return not self.is_internal

    @property
    def is_internal(self) -> bool:
        """Return if node is an internal node."""
        return True if self.right or self.left else False

    @property
    def is_root(self):
        return True if not self.parent else False
