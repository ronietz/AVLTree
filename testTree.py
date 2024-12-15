from AVLTree import AVLTree
from AVLTree import AVLNode

def print_tree_centered(tree):
    if not tree.root:
        print("Tree is empty")
        return

    def build_tree_structure(node):
        if not node or not node.is_real_node():
            return [], 0, 0  # Empty structure, width, and root position

        # Build structures for left and right subtrees
        left_lines, left_width, left_root_pos = build_tree_structure(node.left)
        right_lines, right_width, right_root_pos = build_tree_structure(node.right)

        # Format the current node
        node_label = f"{node.key}"
        label_width = len(node_label)

        # Calculate root position and total width
        root_pos = left_width + (label_width // 2)
        total_width = left_width + label_width + right_width

        # Prepare the current level's lines
        first_line = f"{' ' * left_width}{node_label}{' ' * right_width}"
        if left_lines or right_lines:
            left_connector = '/' if node.left and node.left.is_real_node() else '      '
            right_connector = '\\' if node.right and node.right.is_real_node() else ' '
            second_line = (
                f"{' ' * (left_root_pos)}{left_connector}"
                f"{' ' * (root_pos - left_root_pos - 1)}"
                f"{' ' * (label_width)}"
                f"{right_connector}{' ' * (total_width - root_pos - 1)}"
            )
        else:
            second_line = ""

        # Merge left and right subtree lines with padding
        max_lines = max(len(left_lines), len(right_lines))
        left_lines += [' ' * left_width] * (max_lines - len(left_lines))
        right_lines += [' ' * right_width] * (max_lines - len(right_lines))
        merged_lines = [
            f"{left}{' ' * label_width}{right}"
            for left, right in zip(left_lines, right_lines)
        ]

        # Return combined structure
        return [first_line, second_line] + merged_lines, total_width, root_pos

    # Build and print the tree structure
    lines, _, _ = build_tree_structure(tree.root)
    for line in lines:
        print(line)

def create_test_tree():
    # Create nodes
    root = AVLNode(5, "")

    treeNode1 = AVLNode(7, "")
    treeNode0 = AVLNode(3, "")
    root.right = treeNode1
    root.left = treeNode0

    treeNode3 = AVLNode(4, "")
    treeNode2 = AVLNode(2, "")
    treeNode0.right = treeNode3
    treeNode0.left = treeNode2

    treeNode4 = AVLNode(8, "")
    treeNode5 = AVLNode(6, "")
    treeNode1.right = treeNode4
    treeNode1.left = treeNode5

    treeNode4.right = AVLNode(9, "")

    # Create tree and set root
    currTree = AVLTree()
    currTree.root = root
    return currTree


if __name__ == '__main__':
    currTree = create_test_tree()

    # Print tree
    print_tree_centered(currTree)
