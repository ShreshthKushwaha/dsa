# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def reverseKGroup(self, head, k: int):
        
      
   
        def reverse(head,k):
            if head==None or head.next==None:
                return head
            if k==1:


                return head
            ans = reverse(head.next,k-1)
            head.next.next = head
            head.next= None
            return ans
        
       
        dummy = ListNode(-1)


        dummy.next = head
        cur = head
        prev = dummy

        while cur!=None:
            tail = cur
            index = 0
            while cur and index<k:
                cur=cur.next
                index+=1
            if index==k:
                prev.next = reverse(tail,k)
                prev = tail
            else:
                prev.next = tail
        return dummy.next                   



        