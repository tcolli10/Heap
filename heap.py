
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.items = [0]
        self.current_size = 0
        self.capacity = capacity

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        elif self.items[i * 2 + 1] < self.items[i * 2]:
            return i * 2 + 1 
        else:
            return i * 2

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        elif self.items[i * 2 + 1] > self.items[i * 2]:
            return i * 2 + 1 
        else:
            return i * 2

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False
        else:
            self.items += [item]
            self.current_size += 1
            self.perc_up(self.current_size)
            return True
        


    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        return self.items[0]


    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        else:
            returnValue = self.items[1]
            self.items[1] = self.items[self.current_size]
            self.current_size -= 1
            self.items = self.items[:-1]
            self.perc_down(1)
            return returnValue


    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.items[1:]


    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist'''
        i = 0
        self.items = [0]
        if self.capacity < len(alist):
            self.capacity = len(alist)
        for item in alist:
            self.items += [alist[i]]
            self.current_size += 1
            # self.perc_up(self.current_size)
            i += 1
        minChild = self.min_child(1)
        self.perc_down(1)
        self.perc_down(minChild)
        # if self.current_size % 2 == 0:
        #     leaf1 = self.max_child(self.current_size)
        #     leaf2 = self.max_child()
        #     self.perc_up(self.max_child(self.current_size))
        #     self.perc_up(self.max_child((self.current_size-1)// 2))
        # else:
        #     self.perc_up(self.max_child((self.current_size-1)//2))
        #     self.perc_up(self.max_child((self.current_size-2)// 2))


    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.current_size == 0


    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.current_size == self.capacity
            

        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.current_size

        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
             at that location to its proper place in the heap rearranging elements as it goes.'''
        while i * 2 <= self.current_size:
            max_child = self.max_child(i)
            if self.items[max_child] > self.items[i]:
                temp = self.items[i]
                self.items[i] = self.items[max_child]
                self.items[max_child] = temp
            i = max_child   

        
    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i > 1:
            if i % 2 == 0:
                if self.items[i//2] < self.items[i]:
                    temp = self.items[i//2]
                    self.items[i//2] = self.items[i]
                    self.items[i] = temp
                    i = i//2
                else:
                    i = i // 2
            else:
                if self.items[(i-1)//2] < self.items[i]:
                    temp = self.items[(i-1)//2]
                    self.items[(i-1)//2] = self.items[i]
                    self.items[i] = temp
                    i = (i-1)//2
                else:
                    i = (i-1)//2


    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        list = []
        return_list = []
        while self.current_size > 0:
            list.append(self.dequeue())
        while len(list) > 0:
            return_list += [list[-1]]
            list = list[:-1]
        alist[:] = return_list
        return alist



# test_heap = MaxHeap(10)
# test_heap.build_heap([2, 9, 7, 6, 5, 8])
# self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])
# h = MaxHeap
# h.build_heap(h, [1, 2, 3])



# test_heap = MaxHeap()
# list1 = [2, 9, 7, 6, 5, 8]
# test_heap.heap_sort_ascending(list1)