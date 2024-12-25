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
        node_label = f"{node.key, node.height}"
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
                f"{' ' * (root_pos - left_root_pos-3 - 1)}"
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
    root = AVLNode(6, "")
    root.height = 3

    treeNode1 = AVLNode(11, "")
    treeNode0 = AVLNode(3, "")
    root.right = treeNode1
    root.left = treeNode0
    treeNode1.parent = root
    treeNode1.height = 2
    treeNode0.parent = root
    treeNode0.height = 1

    treeNode3 = AVLNode(4, "")
    treeNode2 = AVLNode(2, "")
    treeNode0.right = treeNode3
    treeNode0.left = treeNode2
    treeNode3.parent = treeNode0
    treeNode2.parent = treeNode0
    treeNode3.height = 0
    treeNode2.height = 0



    treeNode16 = AVLNode(None, "")
    treeNode17 = AVLNode(None, "")
    treeNode3.right = treeNode16
    treeNode3.left = treeNode17
    treeNode16.parent = treeNode3
    treeNode17.parent = treeNode3
    treeNode16.height = -1
    treeNode17.height = -1



    treeNode15 = AVLNode(None, "")
    treeNode14 = AVLNode(None, "")
    treeNode2.right = treeNode15
    treeNode2.left = treeNode14
    treeNode15.parent = treeNode2
    treeNode14.parent = treeNode2
    treeNode15.height = -1
    treeNode14.height = -1

    treeNode4 = AVLNode(15, "")
    treeNode5 = AVLNode(9, "")
    treeNode1.right = treeNode4
    treeNode1.left = treeNode5
    treeNode4.parent = treeNode1
    treeNode5.parent = treeNode1
    treeNode4.height = 0
    treeNode5.height = 1



    treeNode19 = AVLNode(None, "")
    treeNode18 = AVLNode(None, "")
    treeNode4.right = treeNode19
    treeNode5.left = treeNode18
    treeNode18.parent = treeNode5
    treeNode19.parent = treeNode5
    treeNode18.height = -1
    treeNode19.height = -1


    treeNode6 = AVLNode(10, "")
    treeNode5.right = treeNode6
    treeNode6.parent = treeNode4
    treeNode6.height = 0
    treeNode6.value = "noy"


    treeNode20 = AVLNode(None, "")
    treeNode21 = AVLNode(None, "")
    treeNode6.right = treeNode20
    treeNode6.left = treeNode21
    treeNode20.parent = treeNode6
    treeNode21.parent = treeNode6
    treeNode20.height = -1
    treeNode21.height = -1


    treeNode22 = AVLNode(None, "")
    treeNode4.left = treeNode21
    treeNode22.parent = treeNode4
    treeNode22.height = -1

    # Create tree and set root
    currTree = AVLTree()
    currTree.root = root
    return currTree


def search_test(tree):
    tup = currTree.search(3)
    if tup[1] != 2:
        print("search_test - Error in existing node")

    tup = currTree.search(20)
    if tup[0] != None:
        print("search_test - Error in non-existing larger node")


    tup = currTree.search(10)
    if tup[0] != None:
        print("search_test - Error in non-existing in between node")
    noy = 5

def finger_search_test(tree):
    tup = currTree.finger_search(3)
    if tup[1] != 5:
        print("finger_search_test - Error in existing node")

    tup = currTree.finger_search(20)
    if tup[0] != None:
        print("finger_search_test - Error in non-existing larger node")


    tup = currTree.finger_search(10)
    if tup[0] != None:
        print("finger_search_test - Error in non-existing in between node")

    tup = currTree.finger_search(16)
    if tup[0] != None:
        print("finger_search_test - Error in non-existing in between node")


    tup = currTree.finger_search(8)
    if tup[1] != 4:
        print("finger_search_test - Error in finding root node")
    noy = 5

def create_avl_tree_height_3():
    root = AVLNode(32, "")
    root.height = 3

    root.left = AVLNode(16, "")
    root.left.height = 2
    root.left.parent = root
    root.right = AVLNode(48, "")
    root.right.height = 2
    root.right.parent = root

    root.left.left = AVLNode(8, "")
    root.left.left.height = 1
    root.left.left.parent = root.left
    root.left.right = AVLNode(24, "")
    root.left.right.height = 1
    root.left.right.parent = root.left
    root.right.left = AVLNode(40, "")
    root.right.left.height = 1
    root.right.left.parent = root.right
    root.right.right = AVLNode(56, "")
    root.right.right.height = 1
    root.right.right.parent = root.right


    root.left.left.left = AVLNode(4, "")
    root.left.left.left.height = 0
    root.left.left.left.parent = root.left.left
    root.left.left.right = AVLNode(12, "")
    root.left.left.right.height = 0
    root.left.left.right.parent = root.left.left
    root.left.right.left = AVLNode(20, "")
    root.left.right.left.height = 0
    root.left.right.left.parent = root.left.right
    root.left.right.right = AVLNode(28, "")
    root.left.right.right.height = 0
    root.left.right.right.parent = root.left.right
    root.right.left.left = AVLNode(36, "")
    root.right.left.left.height = 0
    root.right.left.left.parent = root.right.left
    root.right.left.right = AVLNode(44, "")
    root.right.left.right.height = 0
    root.right.left.right.parent = root.right.left
    root.right.right.left = AVLNode(52, "")
    root.right.right.left.height = 0
    root.right.right.left.parent = root.right.right
    root.right.right.right = AVLNode(60, "")
    root.right.right.right.height = 0
    root.right.right.right.parent = root.right.right

    empty = AVLNode(None, None)
    empty.height = -1
    root.left.left.left.left = empty
    root.left.left.left.right = empty
    root.left.left.right.left = empty
    root.left.left.right.right = empty
    root.left.right.left.left = empty
    root.left.right.left.right = empty
    root.left.right.right.right = empty
    root.left.right.right.left = empty
    root.right.left.left.left = empty
    root.right.left.left.right = empty
    root.right.left.right.right = empty
    root.right.left.right.left = empty
    root.right.right.right.left = empty
    root.right.right.right.right = empty
    root.right.right.left.right = empty
    root.right.right.left.left = empty

    tree = AVLTree()
    tree.root = root
    return tree

def rotate_test():
    tree = create_avl_tree_height_3()
    print_tree_centered(tree)
    tree.rotate(tree.root, tree.root.left, 'r')
    print_tree_centered(tree)

def create_empty_tree():
    tree = AVLTree()
    tree.root = tree.virtual_leaf
    return tree

def insert_test():
    tree = create_empty_tree()
    print_tree_centered(tree)
    tree.insert(5, "roni")
    print_tree_centered(tree)
    tree.insert(4, "roni")
    tree.insert(7, "roni")
    tree.insert(10, "roni")
    print_tree_centered(tree)
    tree.insert(12, "roni")
    print_tree_centered(tree)
    tree.insert(14, "roni")

    tree = create_avl_tree_height_3()
    tree.insert(42 , "roni")
    # insert to parent not a leaf
    tree.insert(46, "roni")
    if tree.root.height != 4:
        print("Enter child not to a leaf - problem fixing heights")

    # insert to a parent who is a leaf
    # case 1 - promote
    tree.insert(47, "roni")
    if tree.root.right.left.height != 2:
        print("Enter child to leaf - problem fixing heights")

    # case 2 - right
    tree.insert(19, "roni")
    print_tree_centered(tree)
    tree.insert(17, "roni")
    if tree.root.left.right.left.key != 19:
        print("Enter child to leaf - single rotate right ERROR")

    # case 3 - left -> right
    tree.insert(22, "roni")
    node = tree.search(20)
    if node[0].right.key != 24:
        print("Enter child to leaf - double rotate right ERROR")

    # case 2 - left
    tree.insert(61, "roni")
    tree.insert(62, "")
    node = tree.search(56)
    if node[0].right.key != 61:
        print("Enter child to leaf - single rotate left ERROR")
    print_tree_centered(tree)
    # case 3 - right -> left
    tree = create_empty_tree()
    tree.insert(1, "")
    tree.insert(3, "")
    print_tree_centered(tree)
    tree.insert(2, "")
    if tree.root.key != 2:
        print("Enter child to leaf - double rotate right-> left ERROR")
    print_tree_centered(tree)
    tree = create_empty_tree()
    if tree.insert(3, "")[2] != 0:
        print("promote ERROR")
    if tree.insert(1, "")[2] != 1:
        print("promote ERROR")
    if tree.insert(2, "")[2] != 1:
        print("promote ERROR")

def finger_insert_test():
    tree = create_avl_tree_height_3()

    x,e,h = tree.finger_insert(80, "bla")
    print_tree_centered(tree)
    if h != 4:
        print("ERROR promoting")
    if e != 1:
        print("ERROR counting edges")
    print(h, e)
    x, e, h = tree.finger_insert(59, "bla")
    print_tree_centered(tree)
    print(h, e)

def join_test():
    tree = create_empty_tree()
    tree.insert(10, "bla")
    tree.insert(15, "bla")
    tree.insert(3, "bla")
    tree.insert(7, "bla")
    tree.insert(5, "bla")

    tree2 = create_empty_tree()
    tree2.insert(1, "bla")
    # join shorter and smaller tree
    tree.join(tree2, 2, "blabla")
    if (tree.root.key != 5):
        print("ERROR joining shorter and smaller tree")

    # join shorter and bigger tree
    tree2 = create_empty_tree()
    tree2.insert(29, "bla")
    tree2.insert(33, "bla")
    tree2.insert(21, "bla")
    tree.join(tree2, 17, "blabla")
    if tree.search(17)[0].right.key != 29:
        print("ERROR joining shorter and bigger tree")

    # join taller and smaller tree
    tree = create_empty_tree()
    tree.insert(17, "bla")
    tree.insert(20, "bla")
    tree.insert(15, "bla")
    tree2 = create_empty_tree()
    tree2.insert(3, "bla")
    tree2.insert(5, "bla")
    tree2.insert(7, "bla")
    tree2.insert(4, "bla")
    tree2.insert(6, "bla")
    tree2.insert(8, "bla")
    tree2.insert(11, "bla")
    tree.join(tree2, 14, "bla")
    if tree.root.right.key != 14:
        print("ERROR joining taller and smaller tree")

    # join taller and bigger tree
    tree = create_empty_tree()
    tree.insert(17, "bla")

    tree2 = create_empty_tree()
    tree2.insert(30, "bla")
    tree2.insert(33, "bla")
    tree2.insert(25, "bla")
    tree2.insert(40, "bla")
    tree2.insert(56, "bla")
    tree2.insert(31, "bla")
    tree2.insert(27, "bla")
    tree2.insert(38, "bla")
    tree2.insert(45, "bla")
    tree2.insert(49, "bla")
    tree2.insert(58, "bla")
    tree2.insert(99, "bla")
    tree.join(tree2, 22, "bla")
    if tree.root.height != 3:
        print("ERROR joining taller and bigger tree")

    # join same height smaller tree
    tree = create_empty_tree()
    tree.insert(17, "bla")
    tree.insert(20, "bla")
    tree.insert(15, "bla")
    tree2 = create_empty_tree()
    tree2.insert(2, "bla")
    tree2.insert(3, "bla")
    tree2.insert(5, "bla")
    tree.join(tree2, 10, "bla")
    if tree.root.key != 10:
        print("ERROR joining same heights smaller tree")

    # join same height bigger tree
    tree = create_empty_tree()
    tree.insert(17, "bla")
    tree2 = create_empty_tree()
    tree2.insert(30, "bla")
    tree.join(tree2, 18, "")
    if tree.root.key != 18:
        print("ERROR joining same heights bigger tree")


def delete_test(currTree):
    #case4 - 2 rotates
    print("------------- case4 - 2 rotates --------------")
    node = currTree.max_node()
    currTree.delete(node)
    print_tree_centered(currTree)

    # case3 - demote + rotate
    print("------------- case3 - demote + rotate --------------")
    currTree.insert(15, "roni")
    print_tree_centered(currTree)
    node = currTree.root.right.left
    currTree.delete(node)
    print_tree_centered(currTree)

    # case1 - decrease
    print("------------- case2 - demote --------------")
    currTree.insert(20, "roni")
    print_tree_centered(currTree)
    node = currTree.root.right.right
    currTree.delete(node)
    print_tree_centered(currTree)

    #case3 - 2 rotates
    print("------------- case3 - one rotates r l --------------")
    currTree.insert(8, "roni")
    print_tree_centered(currTree)
    node = currTree.root.right.right
    currTree.delete(node)
    print_tree_centered(currTree)

    #case 5 - deleting node from the middle
    print("------------- case5 - middle node --------------")
    print_tree_centered(currTree)
    currTree.delete(currTree.root)
    print_tree_centered(currTree)

    # case 6 - deleting max node from the middle
    print("------------- case6 - another middle node --------------")
    print_tree_centered(currTree)
    node = currTree.root.left
    currTree.delete(node)

def split_test(tree):
    node = tree.search(9)[0]
    tree.split(node)

    # node = tree.search(3)[0]
    # tree.split(node)
    #
    # node = tree.search(6)[0]
    # tree.split(node)
    noy = 5



if __name__ == '__main__':
    currTree = create_test_tree()

    # Print tree
    #print_tree_centered(currTree)

    #search_test(currTree)
    # finger_search_test(currTree)

    # search_test(currTree)
    # finger_search_test(currTree)

    #rotate_test()

    #insert_test()

    # finger_insert_test()
    #join_test()
    # delete_test(currTree)
    print_tree_centered(currTree)
    split_test(currTree)

    # noy = currTree.avl_to_array()
    # for tup in noy:
    #     print(str(tup[0]) + "  " + str(tup[1]))
    # gal = 5


    print_tree_centered(currTree)
