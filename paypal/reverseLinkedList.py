# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#ITERATIVE MY SOLUTION --> NOT THE CLEANEST
class Solution:
    def reverseList(self, head):

        if head==None or head.next==None:
            return head
        if head.next.next==None:
            ans = head.next
            ans.next = head
            head.next = None
            return ans
        
        

#     None<-1<-2<-3<-4<-5 None
#                    a  b  c
#ans is in a, when b==None and ctries to go to none's next

        a = None
        b = head
        c = head.next

        while b!=None:
            b.next = a
            a = b
            b = c
            if c==None:
                break
            c = c.next
        return a   
##CLEAN-------
    
class Solution:
    def reverseList(self, head):

        prev = None
        current = head

        while current!=None:
            further = current.next
            current.next = prev
            prev = current
            current = further
        return prev   
##recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):

        def reverse(n):
            if n==None:
                return n
            if n.next==None:
                return n

            res = reverse(n.next)
            n.next.next = n
            n.next = None
            return res
        return reverse(head)            







        