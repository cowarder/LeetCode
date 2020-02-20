"""
问题描述：

141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the
position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""

"""
解题思路：
一个走一步，一个走两步，如果是循环的话，终究会遇上的
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        step_1 = step_2 = head
        while step_2.next and step_2.next.next:
            step_1 = step_1.next
            step_2 = step_2.next.next
            if step_1 == step_2:
                return True
        return False