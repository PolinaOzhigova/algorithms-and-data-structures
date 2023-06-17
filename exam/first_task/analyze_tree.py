import random
import graphviz
from collections import Counter

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        values = lines[0].split()[1:]
        preorder = list(map(int, values))

    stack = []
    root = TreeNode(preorder[0])
    stack.append(root)

    for value in preorder[1:]:
        node = TreeNode(value)
        if stack[-1].left is None:
            stack[-1].left = node
        else:
            while stack[-1].right is not None:
                stack.pop()
            stack[-1].right = node

        stack.append(node)

    return root


def is_full_tree(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    if root.left and root.right:
        return is_full_tree(root.left) and is_full_tree(root.right)
    return False


def is_complete_tree(root, index, node_count):
    if not root:
        return True
    if index >= node_count:
        return False
    return (is_complete_tree(root.left, 2 * index + 1, node_count) and
            is_complete_tree(root.right, 2 * index + 2, node_count))


def get_tree_depth(root):
    if not root:
        return 0
    left_depth = get_tree_depth(root.left)
    right_depth = get_tree_depth(root.right)
    return max(left_depth, right_depth) + 1


def draw_tree(root):
    G = nx.Graph()
    pos = graphviz_layout(root, prog='dot')
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', font_size=12, arrows=False)
    plt.show()


if __name__ == '__main__':
    filename = 'tree.txt'
    root = build_tree_from_file(filename)

    print('Full tree:', is_full_tree(root))
    print('Complete tree:', is_complete_tree(root, 0, len(open(filename).readlines()[0].split()[1:])))
    print('Tree depth:', get_tree_depth(root))

    draw_tree(root)
