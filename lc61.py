# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        
        curNode = head
        end = head
        lenn = 0
        while curNode is not None:
            end = curNode
            curNode = curNode.next
            lenn += 1

        if k >= lenn:
            k %= lenn
        if k == 0:
            return head
            
        rotate = lenn - k - 1
        mid = head
        while rotate != 0:
            mid = mid.next
            rotate -= 1

        newHead = mid.next
        end.next = head
        mid.next = None

        return newHead


