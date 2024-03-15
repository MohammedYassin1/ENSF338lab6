# Exercise 5

# Question 1
class ListNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = ListNode(value, priority)
        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def display(self):
        current = self.head
        while current:
            print(f"Value: {current.value}, Priority: {current.priority}")
            current = current.next

# Example usage:
pq = ListPriorityQueue()
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)

print("Initial Queue:")
pq.display()

print("\nDequeueing:")
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())

print("\nQueue after dequeue:")
pq.display()



# Question 2
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        self.heap.append((priority, value))
        self._bubble_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()[1]
        else:
            priority, value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._bubble_down(0)
            return value

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index][0] > self.heap[index][0]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while index * 2 + 1 < len(self.heap):
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2 if index * 2 + 2 < len(self.heap) else None

            min_child_index = left_child_index
            if right_child_index is not None and self.heap[right_child_index][0] < self.heap[left_child_index][0]:
                min_child_index = right_child_index

            if self.heap[index][0] > self.heap[min_child_index][0]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

    def display(self):
        print("Priority Queue (Priority, Value):", self.heap)


# Example usage:
pq = HeapPriorityQueue()
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)

print("Initial Queue:")
pq.display()

print("\nDequeueing:")
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())

print("\nQueue after dequeue:")
pq.display()



# Question 3
import random
import timeit

# Importing the implementations
from heapq import heappop, heappush
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heappush(self.heap, (priority, value))

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        _, value = heappop(self.heap)
        return value

class ListNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = ListNode(value, priority)
        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value


# Generate a random list of tasks
tasks = []
for _ in range(1000):
    if random.random() < 0.7:
        tasks.append(("enqueue", random.randint(0, 1000)))
    else:
        tasks.append(("dequeue", None))

# Measure execution time of HeapPriorityQueue
heap_time = timeit.timeit(stmt="pq = HeapPriorityQueue(); " +
                                  "for task in tasks: " +
                                  "   if task[0] == 'enqueue': pq.enqueue(task[1], task[1]) " +
                                  "   else: pq.dequeue()",
                           setup="from __main__ import HeapPriorityQueue, tasks",
                           number=1)

# Measure execution time of ListPriorityQueue
list_time = timeit.timeit(stmt="pq = ListPriorityQueue(); " +
                                  "for task in tasks: " +
                                  "   if task[0] == 'enqueue': pq.enqueue(task[1], task[1]) " +
                                  "   else: pq.dequeue()",
                           setup="from __main__ import ListPriorityQueue, tasks",
                           number=1)

# Calculate average time per task
avg_time_heap = heap_time / len(tasks)
avg_time_list = list_time / len(tasks)

print("HeapPriorityQueue:")
print(f"Overall time: {heap_time} seconds")
print(f"Average time per task: {avg_time_heap} seconds")

print("\nListPriorityQueue:")
print(f"Overall time: {list_time} seconds")
print(f"Average time per task: {avg_time_list} seconds")



"""
Question 4
In general, the heap-based priority queue implementation (HeapPriorityQueue) tends to be faster compared to the linked list-based priority queue implementation (ListPriorityQueue), especially for large datasets. This is due to the fundamental properties of the underlying data structures used in each implementation.

Here's why the heap-based implementation is typically faster:

Time Complexity:
The heap-based implementation has better time complexity for both enqueue and dequeue operations. Enqueueing an element into a heap has a time complexity of O(log n), and dequeueing the smallest element from a heap also has a time complexity of O(log n) due to the need to maintain the heap property. On the other hand, the linked list-based implementation has an average time complexity of O(n) for both enqueue and dequeue operations since it requires traversing the list to find the correct position for insertion and removal.

Memory Access Patterns:
Heap data structure is often implemented as an array. Arrays have better memory locality compared to linked lists, which improves cache performance and reduces the number of cache misses. This can significantly impact performance, especially for large datasets where cache efficiency becomes crucial.

Data Structure Overhead:
Linked lists require additional memory for storing pointers/references to the next node, which can increase memory overhead compared to arrays used in the heap-based implementation. Higher memory overhead can lead to more frequent cache misses and slower performance.

Optimization:
The heap data structure is optimized for priority queue operations. Efficient heap implementations use techniques like sift-up and sift-down (or heapify) to maintain the heap property efficiently. These optimizations contribute to faster performance compared to the linked list-based implementation, which may require more complex traversal and manipulation logic.
Overall, while both implementations can achieve the same functionality, the heap-based priority queue tends to offer better performance characteristics, especially in terms of time complexity and memory access patterns, making it faster for processing large datasets.
"""