# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        ptr1 = None
        ptr2 = head
        while ptr2 != None:
            # print(ptr2.val)
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp

        return ptr1


# Best solution:
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     prev, curr = None, head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev  = curr
#         curr = nxt
#     return prev
