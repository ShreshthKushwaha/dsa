# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        p = l1
        q = l2
        carry = 0
        dummy = ListNode(-1)
        ans = dummy
        res = dummy
        while l1 and l2:
            tempSum = l1.val +l2.val+carry
            carry = tempSum//10
            value = tempSum%10
            res.next = ListNode(value)
            res = res.next            
            l1= l1.next
            l2=l2.next
        while l1:
            tempSum = l1.val+carry
            carry = tempSum//10
            value=tempSum%10
            res.next = ListNode(value)
            res = res.next
            l1=l1.next
        while l2:
            tempSum = l2.val+carry
            carry = tempSum//10
            value=tempSum%10
            res.next = ListNode(value)
            res = res.next
            l2=l2.next
        if carry>0:
            res.next = ListNode(carry)
        return ans.next        

               
             





        
        