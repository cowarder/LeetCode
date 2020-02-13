"""

问题描述：

102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

"""
解题思路：
二叉树的层次遍历问题，每一层需要保存对应的值和左右节点
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        node_list = [root]

        while len(node_list) != 0:
            copy_node_list = []
            val_list = []
            for node in node_list:
                val_list.append(node.val)
                if node:
                    if node.left:
                        copy_node_list.append(node.left)
                    if node.right:
                        copy_node_list.append(node.right)
            result.append(val_list)
            node_list = copy_node_list
        return result
