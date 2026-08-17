# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next

        l, r = 0, len(nodes)-1

        while l < r:
            nodes[l].next = nodes[r]
            l += 1

            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None