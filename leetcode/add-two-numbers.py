# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self._get_reserved_number(l1)
        n2 = self._get_reserved_number(l2)
        n = n1 + n2
        rl3 = [int(i) for i in str(n)]
        ln = ListNode(rl3[0])
        for i in rl3[1:]:
            ln = ListNode(i, ln)
        return ln

    @staticmethod
    def _get_reserved_number(l: ListNode) -> int:
        rsl = []
        while l is not None:
            rsl.insert(0, str(l.val))
            l = l.next
        return int(''.join(rsl))

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s1 = Solution()
    l3 = s1.addTwoNumbers(l1, l2)
    while l3 is not None:
        print(l3.val)
        l3 = l3.next
