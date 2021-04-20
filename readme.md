# Leetcode describes Binary Trees using Lists
## This Python Code Snip converts those lists into a TreeNode Class Instance in the following form

#### Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

#### Example List
    root = [5,4,8,11,null,13,4,7,2,null,null,null,1]


## Conclusion:
## This code doesn't work because recursion naturally is depth first not Breadth first.
## This program doesn't follow that convention.
## In addition, nulls are not referenced at deeper branch levels.
## The complexity of this code outweighs the efficiency gained, so I will revisit another time.
## I found a library called binarytree that does the job,
## While this is technically a different object, it does pass in place of my original requirement
## Testing seems to work. I'll use it in practice on my next exercise.
## This in itself was a good learning exercise in the understanding of binary trees and the use of
## other developer's libraries