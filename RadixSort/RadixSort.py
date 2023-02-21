import itertools

class RadixSort:
    def __init__(self):
        self.base = 7
        #                                _________list of bucketlists
        #                               | ________list of buckets -> list of buckets as array here
        #                               || ___________content of a bucket -> buckets as arrays here
        #                               |||
        self.bucket_list_history = []  #[[[]]] -> will look like this in the end

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, list_):
        """
        Sorts a given list using radixsort in ascending order
        @param list to be sorted
        @returns the sorted list as an 1D array
        @raises ValueError if the list is None
        """
        if isinstance(list_, type(None)):
            raise ValueError('List should not be None')

        self.bucket_list_history.clear()    #clear history list at beginning of sorting

        for i in range(self.base):
            buckets = []
            for j in range(self.base):
                buckets.append(self.bucket_sort(list_, i, j))
            self._add_bucket_list_to_history(buckets)
            list_ = list(self.merge(buckets))
        return list_


    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucketlist and adds it to the bucketlistHistory.
        @param bucket_list is your current bucketlist, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)

        self.bucket_list_history.append(arr_clone)

    def get_digit(self, num, n):
        return num // 10 ** n % 10

    def bucket_sort(self, list, i, j):
        return [num for num in list if self.get_digit(num, i) == j]

    def merge(self, list_):
        return itertools.chain(*list_)

sorter = RadixSort()
print(sorter.sort([111, 4, 4, 4]))
x = sorter.sort([101, 20, 2012, 12, 2010, 120, 202, 2221, 0, 11, 33, 914, 17216, 2123, 21123, 164584, 5142, 412, 191, 17125, 2231, 2123, 22, 6711, 21, 1123515,0,10516165,1061616, 1051416578,651613])
print(x)
