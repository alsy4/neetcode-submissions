# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        nodes = []

        while current is not None:
            nodes.append(current)
            current = current.next

        
        nodes.pop(len(nodes) - n)

        if not nodes:
            return None

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
        return nodes[0]