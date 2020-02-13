"""

问题描述：

101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

"""

"""
解题思路，每一层的节点判断从前往后和从后往前是否是相同的
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root_list = [root]
        while len(root_list) != 0:
            child_val = []
            copy_root_list = []
            for node in root_list:
                if node:
                    if node.left:
                        child_val.append(node.left.val)
                        copy_root_list.append(node.left)
                    else:
                        child_val.append(None)
                    if node.right:
                        child_val.append(node.right.val)
                        copy_root_list.append(node.right)
                    else:
                        child_val.append(None)
                else:
                    continue
            root_list = copy_root_list
            if child_val != child_val[::-1]:
                return False

        return True