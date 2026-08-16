# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))
            
        res = ListNode(0)
        dummy = res

        while heap:
            _, idx, node = heapq.heappop(heap)
            dummy.next = node 
            dummy = dummy.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            
        return res.next