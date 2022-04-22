# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = l = head
        i = 0

        while i < n - 1:
            r = r.next
            i += 1

        if r.next is None:
            head = head.next
            del r
            # r = head
        else:
            while r.next is not None:
                r = r.next
                temp = l
                l = l.next
            temp.next = l.next
            del l

        return head
