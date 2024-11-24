# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Edge case: if the list is empty or k == 1, no need to reverse
        if not head or k == 1:
            return head
          
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break

            group_next = kth.next  
            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def getKthNode(self, curr, k):
        """
        Helper function to get the kth node from the current node.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
