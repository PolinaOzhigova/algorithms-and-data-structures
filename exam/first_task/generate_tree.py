import random
import matplotlib.pyplot as plt
from collections import Counter

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def gen_binary_tree(n):
    root = TreeNode(random.randint(1, 100))
    _gen_tree(root, 0, n)
    return root

def _gen_tree(parent, level, n):
    level += 1
    if level >= n:
        return
    if random.random() > 0.25:
        left_child = TreeNode(random.randint(1, 100))
        parent.left = left_child
        _gen_tree(left_child, level, n)
    if random.random() > 0.25:
        right_child = TreeNode(random.randint(1, 100))
        parent.right = right_child
        _gen_tree(right_child, level, n)
    if random.random() > 0.95:
        left_child = TreeNode(random.randint(1, 100))
        parent.left = left_child
        _gen_tree(left_child, level, n)

def preorder_traversal(node, result):
    if node:
        result.append(node.value)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)


def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)


def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.value)


def save_tree_to_file(tree, filename, root):
    nodes, edges = tree
    node_values = [random.randint(1, 100) for _ in nodes]
    node_map = {node_id: TreeNode(value) for node_id, value in zip(nodes, node_values)}

    for parent_id, child_id in edges:
        parent_node = node_map[parent_id]
        child_node = node_map[child_id]

        if parent_node.left is None:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

    with open(filename, 'w') as file:
        preorder_result = []
        preorder_traversal(root, preorder_result)
        file.write('Preorder: ' + ' '.join(map(str, preorder_result)) + '\n')

        inorder_result = []
        inorder_traversal(root, inorder_result)
        file.write('Inorder: ' + ' '.join(map(str, inorder_result)) + '\n')

        postorder_result = []
        postorder_traversal(root, postorder_result)
        file.write('Postorder: ' + ' '.join(map(str, postorder_result)) + '\n')

if __name__ == '__main__':
    max_depth = int(input('Enter the maximum depth of the binary tree: '))
    node_id = 0
    tree = gen_binary_tree(max_depth)
    filename = 'tree.txt'
    save_tree_to_file(tree, filename, tree[0][0])
