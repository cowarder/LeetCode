"""
问题描述：
103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

"""
解题思路：跟102题类似，最后将偶数行倒置即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
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
        for i in range(len(result)):
            if i % 2 ==1:
                result[i] = result[i][::-1]
        return result