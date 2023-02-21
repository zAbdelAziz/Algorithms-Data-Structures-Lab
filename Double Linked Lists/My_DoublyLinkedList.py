from typing import Union

from My_ListNode import My_ListNode


class My_DoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    ## Do not change! ##

    def __init__(self, new_head: Union[None, 'My_ListNode'] = None, new_tail: Union[None, 'My_ListNode'] = None,
                 new_size=0):
        """Create a list and default values are None."""
        self._header = new_head
        self._tail = new_tail
        self._size = new_size
        self._descending = True

    def _len_(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def _descending(self) -> bool:
        """Return the current order type of the list."""
        return self._descending

    def list_is_empty(self) -> bool:
        """Return True if list is empty."""
        return self._size == 0

    def _get_header(self) -> Union[None, 'My_ListNode']:
        return self._header

    def _get_tail(self) -> Union[None, 'My_ListNode']:
        return self._tail

    ## -- ##

    # EXAMPLE 2
    # The following methods are required for example 2.

    def _insert(self, character_val: str) -> None:
        """Add the element `character_val` to the list, keeping the list in descending/ascending order, depending on
        the descending property.

        Args:
            character_val (str): Character value to be added.

        Raises:
            ValueError: If character_val is not an integer.
        """
        if not isinstance(character_val, str) or len(character_val) != 1 or character_val == None:
        # if not isinstance(character_val, str):
        # if not isinstance(character_val, int):
            raise ValueError

        def insert_head(character_val):
            node = My_ListNode(character_val)
            self._header = node
            self._tail = node
            self._size += 1

        def insert_middle(current_node, character_val):
            if current_node.get_prev_node():
                node = My_ListNode(character_val, prev_node=current_node.get_prev_node(), next_node=current_node)
                current_node.get_prev_node().set_next_node(node)
                current_node.set_prev_node(node)
                self._size += 1
            else:
                node = My_ListNode(character_val, prev_node=None, next_node=current_node)
                current_node.set_prev_node(node)
                self._header = node
                self._size += 1

        def insert_tail(character_val):
            # -> Fetch the Last Node -> Create a New Node with previous value as Tail and next value as None
            # -> Update the next node of the tail to be the new node -> update the tail of the list to be the new node
            current_node = self._get_tail()
            node = My_ListNode(character_val, prev_node=current_node, next_node=None)
            current_node.set_next_node(node)
            self._tail = node
            self._size += 1

        # Insert into Ordered Position
        if not self.list_is_empty():
            current_node = self._get_header()
            for i in range(self._len_() + 1):
                if not self._descending:
                    # Ascending Order
                    # [if Current Node's Value < Value to insert -> Skip]
                    if i < self._len_() and current_node.get_data() < character_val:
                        current_node = current_node.get_next_node()
                    # Tail Node
                    # [if theres's no current_node 'Reached the end of the list', insert tail]
                    elif current_node == None:
                        insert_tail(character_val)
                        return
                    # Middle Nodes
                    # [if Current Node's Value >= Value to insert -> Insert into the middle]
                    elif current_node.get_data() >= character_val:
                        insert_middle(current_node, character_val)
                        return
                else:
                    # Descending Order
                    # [if Current Node's Value > Value to insert -> Skip]
                    if i < self._len_() and current_node.get_data() > character_val:
                        current_node = current_node.get_next_node()
                    # Tail Node
                    # [if theres's no current_node 'Reached the end of the list', insert tail]
                    elif current_node == None:
                        insert_tail(character_val)
                        return
                    # Middle Nodes
                    # [if Current Node's Value <= Value to insert -> Insert into the middle]
                    elif current_node.get_data() <= character_val:
                        insert_middle(current_node, character_val)
                        return
        else:
            # Add Head [First Node to Insert]
            insert_head(character_val)
            return


    def get_character_value(self, index: int) -> str:
        """Return the value (data) at position `index`, without removing the node.

        Args:
            index (int): 0 <= index < Length of list

        Returns:
            (String): Retrieved value.

        Raises:
            ValueError: If the passed index is not an integer or out of range.
        """
        if not isinstance(index, int) or index >= self._len_() or index < 0:
            raise ValueError

        current_node = self._get_header()
        for i in range(index + 1):
            if not i == index:
                current_node = current_node.get_next_node()
            else:
                return current_node.get_data()


    def _remove(self, character_val: str) -> bool:
        """Remove the first occurence of given character value `character_val`.

        Args:
            character_val (str): the value to remove

        Returns:
            (bool): Whether an element was successully removed or not.

        Raises:
            ValueError: If the passed character is not a string
       """

        if not isinstance(character_val, str):
           raise ValueError

        current_node = self._get_header()
        while current_node:
            if current_node.get_data() != character_val:
                current_node = current_node.get_next_node()
            else:
                # Character Exists in Middle [Most Common Case]
                if current_node != self._get_header() and current_node != self._get_tail():
                    self.remove_middle(current_node)
                    return True
                # Only One Node Exists [head = tail = node]
                elif current_node == self._get_header() and current_node == self._get_tail():
                    del current_node
                    self._size -= 1
                    self.validate_empty()
                    return True
                # Character Exists in Header [Least Common Case]
                elif current_node == self._get_header():
                    self.remove_header(current_node)
                    return True
                # Character Exists in Tail [Least Common Case]
                elif current_node == self._get_tail():
                    self.remove_tail(current_node)
                    return True
        return False

    def _remove_all(self, character_val: str) -> bool:
        """Remove every character value `character_val` in the list.

        Args:
            character_val (str): the value to remove

        Returns:
            (bool): Whether an element was successully removed or not.

        Raises:
            ValueError: If the passed character is not a string
        """

        if not isinstance(character_val, str):
           raise ValueError

        current_node = self._get_header()
        found_char = False                                          # [Can Also be a Counter returning number of removed nodes]
        while current_node:
            if current_node.get_data() != character_val:
                current_node = current_node.get_next_node()
            else:
                # Character Exists in Middle [Most Common Case]
                if current_node != self._get_header() and current_node != self._get_tail():
                    self.remove_middle(current_node)
                # Only One Node Exists [head = tail = node]
                elif current_node == self._get_header() and current_node == self._get_tail():
                    del current_node
                    self._size -= 1
                    self.validate_empty()
                # Character Exists in Header [Least Common Case]
                elif current_node == self._get_header():
                    self.remove_header(current_node)
                # Character Exists in Tail [Least Common Case]
                elif current_node == self._get_tail():
                    self.remove_tail(current_node)
                current_node = current_node.get_next_node()
                found_char = True
        if found_char:
            return True
        else:
            return False

    def remove_duplicates(self) -> None:
        """Remove all duplicates from the list such that the remaining elements are all unique.

        Example:
            ['a','a','d','d','d','f','g'] -> ['a','d','f','g']
        """
        if self.list_is_empty() or self._header == self._tail:
            return

        current_node = self._get_header()
        # Loop Through All Elements
        while current_node:
            # Loop from Next Node to Tail
            next_node = current_node.get_next_node()
            while next_node:
                if current_node.get_data() != next_node.get_data():
                # Skip if not Equal
                    next_node = next_node.get_next_node()
                else:
                    # Handle Middle / Tail Elements Only since Headr cannot be a duplicate [First Element]
                    temp_next = next_node.get_next_node()
                    if next_node != self._get_header() and next_node != self._get_tail():
                        self.remove_middle(next_node)
                    elif next_node == self._get_tail():
                        self.remove_tail(next_node)
                    next_node = temp_next
            current_node = current_node.get_next_node()
        return

    def reorder_list(self):
        """Reorder list from a descending order into an ascending order and vice versa. It also changes the way how
        the list inserts future elements to the list (in descending order, when it was changed to descending order and
        vice versa). No return value nor an error is specified, as this method is an internal method

        Example: ['a','d','f','g'] -> ['g','f','d','a'] -> ['a','d','f','g'].
        """

        head = self._get_header()
        tail = self._get_tail()
        current_node = self._get_header()
        while current_node:
            prev = current_node.get_prev_node()
            current_node.set_prev_node(current_node.get_next_node())
            current_node.set_next_node(prev)
            current_node = current_node.get_prev_node()
        self._header = tail
        self._tail = head
        self._descending = False if not self._descending else True
        return




    def validate_empty(self):
        if self._len_() == 0:
            self._header = None
            self._tail = None

    def remove_middle(self, node):
        node.get_prev_node().set_next_node(node.get_next_node())
        node.get_next_node().set_prev_node(node.get_prev_node())
        del node
        self._size -= 1
        self.validate_empty()

    def remove_header(self, node):
        node.get_next_node().set_prev_node(None)
        self._header = node.get_next_node()
        del node
        self._size -= 1
        self.validate_empty()

    def remove_tail(self, node):
        node.get_prev_node().set_next_node(None)
        self._tail = node.get_prev_node()
        del node
        self._size -= 1
        self.validate_empty()







# list = My_DoublyLinkedList()
# list._insert('A')
# list._insert('A')
# list._insert('B')
# list._insert('O')
# list._insert('G')
# list._insert('G')
# list._insert('G')
# list._insert('M')
# list._insert('N')
# list._insert('C')
# list._insert('B')
# list._insert('D')
# list._insert('L')
# list._insert('F')
# list._insert('F')
#
# list._remove('C')
# list._remove_all('F')
# list.reorder_list()
# list.remove_duplicates()
#
#
# x1 = list._get_header()
# x2 = x1.get_next_node()
# x3 = x2.get_next_node()
# x4 = x3.get_next_node()
# x5 = x4.get_next_node()
# x6 = x5.get_next_node()
# x7 = x6.get_next_node()
# xn = list._get_tail()
# print(x1.get_data(), x2.get_data(), x3.get_data(), x4.get_data(), x5.get_data(), x6.get_data(), x7.get_data(), xn.get_data())
