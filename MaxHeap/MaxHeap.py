import math



class MaxHeap:
    def __init__(self, list):
        """
        @param list from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up maxheap in place.
        """
        if isinstance(list, type(None)):
            raise ValueError('List cannot be None')
        self.heap = None
        self.size = len(list)
        self.height = math.ceil(math.log2(len(list)+1))
        if len(list) > 1:
            for i in range(len(list)//2-1, -1, -1):
                self.heap = self.down_heap_list(list, i)
        else:
            self.heap = list


    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Do not search the entire array sequentially, but use the properties of a heap
        """
        if isinstance(val, type(None)):
            raise ValueError('List cannot be None')
        return True if self.find(0, val) else False
        # Can Also return the index of the element
        # return self.find(0,val)

    def is_empty(self):
        """
        @return True if the heap is empty, False otherwise
        """
        return True if self.size > 0 else False

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        v = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.down_heap(0)
        self.size -= 1
        return v

    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        self.heap = [self.remove_max() for _ in range(self.size)][::-1]
        self.size = len(self.heap)
        return self.heap


    def parent(self, index):
        return int((index-1)/2)

    def left(self, index):
        return int((2*index)+1)

    def right(self, index):
        return int((2*index)+2)

    def down_heap_list(self, list, index):
        root = index
        left = self.left(index)
        right = self.right(index)
        if len(list) > left:
            if list[left] > list[root]:
                root = left
        if len(list) > right:
            if list[right] > list[root]:
                root = right
        if root != index:
            list[index], list[root] = list[root], list[index]
            self.down_heap_list(list, root)
        return list

    def find(self, index, val):
        left = self.left(index)
        right = self.right(index)
        found = True if index == 0 and val == self.heap[index] else False

        if len(self.heap) > left:
            if self.heap[left] == val:
                found = left
            if self.heap[left] > val:
                found = self.find(left, val)
        if len(self.heap) > right and not found:
            if self.heap[right] == val:
                found = right
            if self.heap[right] > val:
                found = self.find(right, val)
        return found


    def down_heap(self, index):
        left_child = self.left(index) if index != 0 else 1
        right_child = self.right(index) if index != 0 else 2

        if left_child < len(self.heap):
            if self.heap[left_child] > self.heap[index]:
                self.swap(left_child, index)
            self.down_heap(left_child)
        if right_child < len(self.heap):
            if self.heap[right_child] > self.heap[index]:
                self.swap(right_child, index)
            self.down_heap(right_child)

    def swap(self, index1, index2):
        t = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = t
