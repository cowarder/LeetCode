"""
问题描述：

109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

"""
解题思路：
平衡二叉搜索树的构造，每次去中间元素构建根结点，左侧构建左子树，右侧构建右子树
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
            
        def build_tree(head, node_list):
            if not node_list:
                return
            mid_index = len(node_list)//2
            head.val = node_list[mid_index]
            if node_list[:mid_index]:
                head.left = TreeNode(0)
                build_tree(head.left, node_list[:mid_index])
            if node_list[mid_index+1:]:
                head.right = TreeNode(0)
                build_tree(head.right, node_list[mid_index+1:])
        h = TreeNode(None)
        build_tree(h, vals)
        return h