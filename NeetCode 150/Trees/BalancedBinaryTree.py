'''
Balanced Binary Tree
Difficulty: Easy

Given a binary tree, return true if it is height balanced and false otherwise.

A binary tree is height balanced if the depth of the two subtrees of every node never differ by more than 1.

Example 1:

    Input: root = [1,2,3,null,null,4]
    Output: true

Example 2:

    Input: root = [1,2,3,null,null,4,null,5]
    Output: false

Example 3:

    Input: root = []
    Output: true

'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isBalanced(root: Optional[TreeNode]) -> bool:
    
    def dfs(root):
        if not root:
            return [True, 0]
        
        lhs = dfs(root.left)
        rhs = dfs(root.right)
        balanced = lhs[0] and rhs[0] and abs(lhs[1] - rhs[1]) <= 1
        
        return [balanced, 1 + max(lhs[1], rhs[1])]
    
    return dfs(root)[0]

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

print(isBalanced(root))

'''
Notes:

    Time complexity: O(n)
    Space complexity: O(h) where h is the height of the tree
    
    Short explanation:
        - Use depth first search to traverse the tree
            - Depth First Search (DFS) involves traversing a tree or graph by going as deep as possible down a path before backtracking and trying a different path
        - Once we reach the bottom of the tree, start going up, adding one to the maximum depth of the left and right subtrees
        - After both the left and right subtrees have been traversed, check if the tree is balanced
            - Condition for a balanced tree: Difference in depth of the left and right subtrees is less than or equal to 1
'''