# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        
        # get slow to the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # get slow past middle to the first of the second half
        tmp = slow
        slow = slow.next
        # cur the linked list
        tmp.next = None

        # reverse second half
        prev = None
        nex = slow.next
        while slow:
            slow.next = prev
            prev = slow
            slow = nex
            if (slow is not None):
                nex = slow.next
        
        cur = head
        second = slow
        while slow:
            second = slow.next
            slow.next = cur.next
            cur.next = slow
            cur = slow.next
            slow = second



l4 = ListNode(1, None)
l3 = ListNode(2, l4)
l2 = ListNode(1, l3)
l1 = ListNode(1, l2)

s = Solution()
print(s.isPalindrome(l1))