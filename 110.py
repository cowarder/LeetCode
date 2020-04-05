"""
问题描述：

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
"""

"""
解题思路：
平衡二叉树判断，首先利用height递归函数求出左右子树的高度，判断它们高度之间的差是否大于1
然后递归判断左右子树是否均为平衡二叉树
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.height(root.left, 0) - self.height(root.right, 0)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root, h):
        if not root:
            return h
        return max(self.height(root.left, h + 1), self.height(root.right, h + 1))
