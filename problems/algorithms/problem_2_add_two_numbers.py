# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = self.process_next(l1, l2, 0)
        return answer

    def process_next(self, l1, l2, flag):
        if l1 is None and l2 is None:
            value, flag = self.add([0, 0, flag])
            return self.last_answer(value, flag)
        elif l1 is None and l2 is not None:
            value, flag = self.add([0, l2.val, flag])
            return ListNode(value, next=self.process_next(None, l2.next, flag))
        elif l1 is not None and l2 is None:
            value, flag = self.add([l1.val, 0, flag])
            return ListNode(value, next=self.process_next(l1.next, None, flag))
        else:
            value, flag = self.add([l1.val, l2.val, flag])
            return ListNode(value, next=self.process_next(l1.next, l2.next, flag))

    @staticmethod
    def add(array_values):
        value = sum(array_values) % 10
        flag = int(sum(array_values) // 10)
        return value, flag

    @staticmethod
    def last_answer(value, flag):
        if value != 0:
            return ListNode(value, next=None)
