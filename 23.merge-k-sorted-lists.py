from heapq import heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
