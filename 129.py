"""
问题描述：

129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

"""

"""
解题思路：
DFS
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if not root:
            return 0
        def get_path(root, path):
            if not (root.left or root.right):
                result.append(path+[str(root.val)])
                return
            if root.left:
                get_path(root.left, path+[str(root.val)])
            if root.right:
                get_path(root.right, path+[str(root.val)])
        get_path(root, [])
        result = [int("".join(x)) for x in result]
        return sum(result)