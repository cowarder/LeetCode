"""
问题描述
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""

"""
解题思路：
广度优先搜索
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        """
        if not root:
            return 0
        nodes = [root]
        depth = 1
        while nodes:
            new_nodes = []
            for node in nodes:
                if not (node.left or node.right):
                    return depth
                else:
                    if node.left:
                        new_nodes.append(node.left)
                    if node.right:
                        new_nodes.append(node.right)
            depth += 1
            nodes = new_nodes
        return depth