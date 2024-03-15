# Exercise 4

# Question 1
class Heap:
    def __init__(self):
        self.arr = []

    def heapify(self, arr):
        self.arr = arr
        n = len(self.arr)
        # Start from the last non-leaf node and heapify each subtree
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i, n)

    def enqueue(self, value):
        self.arr.append(value)
        self._heapify_up(len(self.arr) - 1)

    def dequeue(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()
        # Swap the root with the last element
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        max_value = self.arr.pop()
        # Heapify down to maintain heap property
        self._heapify_down(0, len(self.arr))
        return max_value

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                break

    def _heapify_down(self, index, size):
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < size and self.arr[left_child] > self.arr[largest]:
                largest = left_child
            if right_child < size and self.arr[right_child] > self.arr[largest]:
                largest = right_child

            if largest != index:
                self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
                index = largest
            else:
                break


# Example usage:
heap = Heap()
arr = [4, 10, 3, 5, 1]
heap.heapify(arr)
print("Heapified array:", heap.arr)  # Output: [10, 5, 3, 4, 1]

heap.enqueue(7)
print("After enqueuing 7:", heap.arr)  # Output: [10, 7, 3, 4, 1, 5]

max_value = heap.dequeue()
print("Dequeued max value:", max_value)  # Output: 10
print("After dequeue:", heap.arr)  # Output: [7, 5, 3, 4, 1]



# Question 2
def test_sorted_heap():
    heap = Heap()
    input_array = [10, 7, 5, 4, 3, 1]
    expected_heapified_array = [10, 7, 5, 4, 3, 1]
    heap.heapify(input_array)
    assert heap.arr == expected_heapified_array

def test_empty_array():
    heap = Heap()
    input_array = []
    expected_heapified_array = []
    heap.heapify(input_array)
    assert heap.arr == expected_heapified_array

def test_random_shuffled_list():
    heap = Heap()
    import random
    input_array = list(range(1000))
    random.shuffle(input_array)
    expected_heapified_array = sorted(input_array, reverse=True) # Max-heap
    heap.heapify(input_array)
    assert heap.arr == expected_heapified_array

# Run the tests
test_sorted_heap()
test_empty_array()
test_random_shuffled_list()
print("All tests passed successfully!")


"""
Explanation:

test_sorted_heap: This test verifies that if the input array is already a correctly sorted heap, the heap remains unchanged after the heapify method is called.

test_empty_array: This test checks if the heapify method handles an empty input array correctly by ensuring that the resulting heap is also empty.

test_random_shuffled_list: This test creates a long list of integers, shuffles it randomly, and then heapifies it. It compares the resulting heap with the expected heap, which is the sorted input array in reverse order (to create a max-heap).

Each test compares the actual heapified array with the expected heapified array and asserts whether they are equal. If all assertions pass, it indicates that the implementation behaves as expected for the given scenarios.
"""