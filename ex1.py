import random
import timeit
#1.

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right  

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

#2.
# Generate a sorted vector of 10000 elements
sorted_vector = list(range(10000))

# Build a tree by inserting each element
root = None
for element in sorted_vector:
    root = insert(element, root)

# Search each element and time the search
total_time = 0
for element in sorted_vector:
    avg_time = timeit.timeit(lambda: search(element, root), number=10) / 10
    total_time += avg_time

average_time = total_time / len(sorted_vector)

print("Average Time:", average_time)
print("Total Time:", total_time)

#3.
# Shuffle the vector
random.shuffle(sorted_vector)

root = None
for element in sorted_vector:
    root = insert(element, root)

# Search each element and time the search
total_time_s = 0
for element in sorted_vector:
    avg_time_s = timeit.timeit(lambda: search(element, root), number=10) / 10
    total_time_s += avg_time_s

average_time_s = total_time_s / len(sorted_vector)

print("Average Time Shuffle:", average_time_s)
print("Total Time Shuffle:", total_time_s)

#4.
'''
The shuffle version is faster. This is because the tree is more balanced when the elements are inserted in a random order.
While the original tree is more unbalanced, making the average time complexity of the search O(n) instead of O(log n).
'''
