from math import *

class MinHeap:

    def __init__(self):
        self.heap = []
        self._size = len(self.heap)

    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def insert(self, integer_val: int) -> None:
        """inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None
        """
        # print(integer_val)
        if isinstance(integer_val, type(None)):
            raise ValueError('integer_val should not be None')

        self.heap.append(integer_val)
        self.up_heap(len(self.heap))
        # self.down_heap(0)             # Can Also be used
        self.size += 1


    def is_empty(self) -> bool:
        """returns True if the min heap is empty, False otherwise
        @return True or False
        """
        return True if len(self.heap) == 0 else False

    def get_min(self) -> int:
        """returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        return self.heap[0] if self.heap else None

    def remove_min(self) -> int:
        """removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        v = self.get_min()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.down_heap(0)
        self.size -= 1
        return v

    def get_size(self) -> int:
        """returns the number of elements in the PQ
        @return number of elements
        """
        return len(self.heap)

    def up_heap(self, index):
        parent = self.parent(index-1)
        if index != 0:
            if self.heap[parent] > self.heap[index-1]:
                self.swap(parent, index-1)
            self.up_heap(parent)

    def down_heap(self, index):
        left_child = self.left_child(index) if index != 0 else 1
        right_child = self.right_child(index) if index != 0 else 2

        if left_child < len(self.heap):
            if self.heap[left_child] < self.heap[index]:
                self.swap(left_child, index)
            self.down_heap(left_child)
        if right_child < len(self.heap):
            if self.heap[right_child] < self.heap[index]:
                self.swap(right_child, index)
            self.down_heap(right_child)

    def parent(self, index):
        return int((index-1)/2)

    def left_child(self, index):
        return int((2*index)+1)

    def right_child(self, index):
        return int((2*index)+2)

    def swap(self, index1, index2):
        self.validate_index(index1), self.validate_index(index2)
        t = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = t

    def validate_index(self, index):
        if not isinstance(index, int):
            raise ValueError('index should be integer')

    def __repr__(self):
        return str(self.heap)


# heap = MinHeap()
#
# heap.insert(1)
# heap.insert(10)
# heap.insert(100)
# heap.insert(1000)
# heap.insert(5)
# heap.insert(15)
# heap.insert(20)
# print(heap.size)
