import json
import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree_from_dict(data):
    if data is None:
        return None

    node = Node(data['value'])
    node.left = build_tree_from_dict(data['left'])
    node.right = build_tree_from_dict(data['right'])

    return node

def read_tree_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        data = json.loads(content)
        return build_tree_from_dict(data)

def build_graph(node, graph):
    if node is None:
        return

    graph.node(str(id(node)), str(node.value))

    if node.left:
        graph.edge(str(id(node)), str(id(node.left)), label='Left')
        build_graph(node.left, graph)

    if node.right:
        graph.edge(str(id(node)), str(id(node.right)), label='Right')
        build_graph(node.right, graph)

def visualize_tree(tree):
    graph = graphviz.Digraph(format='png')
    build_graph(tree, graph)
    graph.render('tree_graph', view=True)


def is_full_tree(node):
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left is not None and node.right is not None:
        return is_full_tree(node.left) and is_full_tree(node.right)

    return False

def is_complete_tree(node, index, count):
    if node is None:
        return True

    if index >= count:
        return False

    return (is_complete_tree(node.left, 2 * index + 1, count) and
            is_complete_tree(node.right, 2 * index + 2, count))


def calculate_depth(node):
    if node is None:
        return 0

    left_depth = calculate_depth(node.left)
    right_depth = calculate_depth(node.right)

    return max(left_depth, right_depth) + 1

def calculate_size(node):
    if node is None:
        return 0

    return 1 + calculate_size(node.left) + calculate_size(node.right)


filename = input("Введите имя файла с деревом: ")
tree = read_tree_from_file(filename)

tree_size = calculate_size(tree)
print("Полнота дерева:", is_full_tree(tree))
print("Строгость дерева:", is_complete_tree(tree, 0, tree_size))
print("Глубина дерева:", calculate_depth(tree))

visualize_tree(tree)

