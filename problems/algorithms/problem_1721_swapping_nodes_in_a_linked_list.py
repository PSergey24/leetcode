from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kPointer = head
        tailPointer = head

        for i in range(k-1):
            kPointer = kPointer.next
        headPointer = kPointer

        while headPointer.next:
            headPointer = headPointer.next
            tailPointer = tailPointer.next

        kPointer.val, tailPointer.val = tailPointer.val, kPointer.val
        return head
