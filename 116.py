"""
问题描述：

116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""

"""
解题思路：
每一层的前一个元素右面的元素作为其后继元素

第一种方法是递归方法，比较简单
第二种方法是迭代方法，首先按照高度迭代，再按照宽度迭代，在每一层遵循：
    node.left.next = node.right
    node.right.next = node.next.left
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):

    # recursive
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

    # iterative
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        while root.left:
            next = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                root = root.next
            root = next