# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        sentinel = None
        cursor = None
        while (l1 != None or l2 != None):
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum_result = x + y + carry_over
            carry_over = sum_result // 10
            if sentinel == None:
                sentinel = ListNode(sum_result % 10)
                cursor = sentinel
                l1, l2 = l1.next, l2.next
            else:
                cursor.next = ListNode(sum_result % 10)
                l1 = l1.next if l1 != None else None
                l2 = l2.next if l2 != None else None
                cursor = cursor.next
        if carry_over != 0:
            cursor.next = ListNode(carry_over)
        return sentinel
