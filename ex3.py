import random
import timeit
import sys

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right  



def expression_to_tree(expression):
    num = []
    op = []
    status = None
    for i, c in enumerate(expression):
        if status == 1 and c == '(':
            op[-1].right = expression_to_tree(expression[i+1:])
            op[-1].right.parent = op[-1]
            break
        if c.isdigit():
            if status == 1:
                op[-1].right = Node(c)
                op[-1].right.parent = op[-1]
                status = 0
            else:
                num.append(Node(c))
        elif c in '+-*/':
            root = Node(c)
            op.append(root)
            if num:
                root.left = num.pop()
            else:
                root.left = op[-2]
                op[-2].parent = root
            status = 1
    parent = op[0]
    while 1:
        prev = parent
        parent = parent.parent
        if parent is None:
            return prev

def compute(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.data)

    left = compute(root.left)
    right = compute(root.right)

    if root.data == '+':
        return left + right
    elif root.data == '-':
        return left - right
    elif root.data == '*':
        return left * right
    elif root.data == '/':
        return left / right

expression = sys.argv[1]
tree = expression_to_tree(expression)
computed = compute(tree)
print(computed)