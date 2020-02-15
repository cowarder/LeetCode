"""

问题描述：

105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

"""
解题思路：
经典的知道二叉树的先序遍历和中序遍历，求出二叉树结构
1 先序遍历的第一个元素是当前树的根结点
2 在从中序遍历中找到第一个元素值，左边的是左子树，右边的是右子树
3 有了左子树，可以求出其长度，在先序遍历中截取对应的结点数目
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder[:index], inorder[0:index])
        root.right = self.buildTree(preorder[index:], inorder[index+1:])
        return root