# Exercise 2

# Question 1
# Binary Search Tree
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root
    
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

# Example usage:
bst = BST()
root = None
keys = [10, 5, 15, 7, 3, 12, 20]

for key in keys:
    root = bst.insert(root, key)

print(bst.search(root, 7))  # Output: <__main__.TreeNode object at ...> (Node with value 7)




# Binary Search in Arrays
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

# Example usage:
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
target = 11
print(binary_search(arr, target))  # Output: 4 (Index of target)



# Question 2
import timeit
import random

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root
    
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

def generate_sorted_vector(size):
    return list(range(1, size + 1))

def shuffle_vector(vector):
    random.shuffle(vector)

# Measure BST performance
def measure_bst_performance(size):
    sorted_vector = generate_sorted_vector(size)
    shuffle_vector(sorted_vector)

    bst = BST()
    root = None

    # Build BST
    for key in sorted_vector:
        root = bst.insert(root, key)

    total_time = 0
    for key in sorted_vector:
        # Time the search operation
        search_time = timeit.timeit(lambda: bst.search(root, key), number=10)
        total_time += search_time

    average_time = total_time / size
    return average_time, total_time

# Example usage
average_time, total_time = measure_bst_performance(10000)
print("Average search time:", average_time)
print("Total search time:", total_time)



# Question 3
import timeit
import random

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

# Measure binary search performance
def measure_binary_search_performance(vector):
    sorted_vector = sorted(vector)

    total_time = 0
    for key in sorted_vector:
        # Time the binary search operation
        search_time = timeit.timeit(lambda: binary_search(sorted_vector, key), number=10)
        total_time += search_time

    average_time = total_time / len(sorted_vector)
    return average_time, total_time

# Example usage
# Assuming 'shuffled_vector' is the shuffled vector from before
shuffled_vector = list(range(1, 10001))  # Sample shuffled vector
random.shuffle(shuffled_vector)

average_time, total_time = measure_binary_search_performance(shuffled_vector)
print("Average search time:", average_time)
print("Total search time:", total_time)



"""
Question 4
Determining which approach is faster depends on various factors such as the size of the dataset, the distribution of the data, and the specific implementation of the algorithms. However, we can make some educated guesses based on the typical characteristics of binary search trees (BSTs) and binary search in sorted arrays.

BST Approach:

Insertion of elements into a BST is relatively efficient, usually O(log n) in average case, but it can degrade to O(n) in the worst case if the tree becomes unbalanced.
Searching in a balanced BST is also O(log n) in the average case, but it can degrade to O(n) in the worst case for unbalanced trees.


Binary Search in Sorted Array Approach:

Sorting the array initially takes O(n log n) time complexity.
Once sorted, binary search in a sorted array has a time complexity of O(log n).
Based on these considerations:

For small datasets or datasets that are known to be uniformly distributed, binary search in a sorted array might be faster overall due to its simplicity and guaranteed logarithmic time complexity for search.
However, for larger datasets or datasets with unknown distribution, BSTs might perform better if they are well-balanced. BSTs can offer faster insertion times compared to sorting an array, and searching can be efficient as well if the tree is balanced.


In terms of why one approach might be faster than the other:

Binary search in sorted arrays has more predictable time complexity. Once sorted, the search operation is guaranteed to be O(log n). However, sorting the array initially can be computationally expensive.
Binary search trees can have variable performance depending on the balance of the tree. If the tree is balanced, both insertion and search operations are efficient. However, if the tree becomes unbalanced (e.g., due to skewed insertion order), performance can degrade 
significantly.

To conclusively determine which approach is faster for a specific dataset and use case, empirical testing and profiling are necessary.
"""