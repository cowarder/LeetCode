"""
问题描述：

94. Binary Tree Inorder Traversal



Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

"""
解题思路：二叉树中序遍历方法，需要考虑递归方法和迭代方法
中序遍历迭代的方法是利用栈进行存储
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iteration method
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                return result
            cur = stack.pop()
            result.append(cur.val)
            root = cur.right


# recursive method
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def search(node):
            if node:
                search(node.left)
                result.append(node.val)
                search(node.right)

        search(root)
        return result