import random
import json

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_random_binary_tree(size, max_depth):
    def insert_node_recursive(root, value, depth):
        if depth == 0:
            return None
        if root is None:
            return Node(value)
        else:
            if random.choice([True, False]):
                root.left = insert_node_recursive(root.left, value, depth - 1)
            else:
                root.right = insert_node_recursive(root.right, value, depth - 1)
        return root

    root = None
    for _ in range(size):
        value = random.randint(1, 100)
        root = insert_node_recursive(root, value, max_depth)
    return root


def convert_tree_to_dict(node):
    if node is None:
        return None

    data = {
        'value': node.value,
        'left': convert_tree_to_dict(node.left),
        'right': convert_tree_to_dict(node.right)
    }

    return data

def save_tree_to_file(tree, filename):
    data = convert_tree_to_dict(tree)
    with open(filename, 'w') as file:
        json.dump(data, file)

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

def save_to_file(tree, filename):
    with open(filename, 'w') as file:
        preorder_result = []
        preorder_traversal(tree, preorder_result)
        file.write('Preorder: ' + ' '.join(map(str, preorder_result)) + '\n')

        inorder_result = []
        inorder_traversal(tree, inorder_result)
        file.write('Inorder: ' + ' '.join(map(str, inorder_result)) + '\n')

        postorder_result = []
        postorder_traversal(tree, postorder_result)
        file.write('Postorder: ' + ' '.join(map(str, postorder_result)) + '\n')


max_depth = int(input("Введите максимальную глубину дерева: "))
size = 2*max_depth-1
tree = generate_random_binary_tree(size, max_depth)

filename = 'tree.txt'
save_tree_to_file(tree, filename)
save_to_file(tree, 'tree1.json')
print("Дерево сохранено в файл", filename)
