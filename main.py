""" Leetcode describes Binary Trees using Lists
This Python Code Snip converts those lists into a TreeNode Class Instance in the following form

Definition for a binary tree node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example List

root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]


def tree_maker(tree_list: list) -> TreeNode:
    if len(tree_list) == 1:
        btree = TreeNode(tree_list[0], None, None)
        tree_list.pop(0)
        return btree
    elif len(tree_list) == 2:
        btree = TreeNode(tree_list[0], tree_list[1], None)
        tree_list.pop(0)
    elif len(tree_list) > 2:
        btree = TreeNode(tree_list[0], tree_list[1], tree_list[2])
        tree_list.pop(0)
        btree.left = tree_maker(tree_list)
        btree.right = tree_maker(tree_list)
        print(tree_list)
    else:
        btree = TreeNode()
    return btree


my_tree = tree_maker(root)
print(my_tree)
