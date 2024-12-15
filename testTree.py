from AVLTree import AVLTree
from AVLTree import AVLNode





def print_tree_centered(tree):
    if not tree.root:
        print("Tree is empty")
        return

    def get_height(node):
        return node.height if node and node.is_real_node() else -1

    def build_tree_structure(node):
        if not node or not node.is_real_node():
            return [], 0, 0  # Empty lines, width, and root position

        left_lines, left_width, left_root_pos = build_tree_structure(node.left)
        right_lines, right_width, right_root_pos = build_tree_structure(node.right)

        node_label = f"{node.key}"
        label_width = len(node_label)

        # Compute positions
        root_pos = max(left_width, left_root_pos + label_width // 2 + 1)
        total_width = max(left_width + right_width + label_width + 1, root_pos + right_root_pos)

        # Combine subtrees into the current layer
        first_line = " " * left_root_pos + node_label + " " * (total_width - root_pos - label_width)
        second_line = (
            (" " * left_root_pos + "/" + " " * (root_pos - left_root_pos - 1) + "\\" + " " * (total_width - root_pos - 1))
            if left_lines or right_lines
            else ""
        )

        # Adjust child lines with appropriate padding
        left_lines = [line + " " * (total_width - left_width) for line in left_lines]
        right_lines = [" " * left_width + line for line in right_lines]
        lines = [first_line, second_line] + [l + r for l, r in zip(left_lines, right_lines)]

        return lines, total_width, root_pos

    # Build the structure from the root
    lines, _, _ = build_tree_structure(tree.root)
    for line in lines:
        print(line)



if __name__ == '__main__':
    treeRoot = AVLNode(0,"1")
    currTree = AVLTree()

    # currTree.insert(treeRoot)
    print_tree_centered(currTree)



