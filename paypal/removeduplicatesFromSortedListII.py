# Definition for singly-linked list.
#ITERATIVE SOLUTION SELF--NOT SO CLEAR
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head):

        dummy = ListNode(-1000)


        ans = dummy
        dummy.next = head
        curr = dummy


        while curr!=None:
            nextElement = curr.next
            backup = nextElement
            if nextElement==None:
                break
            nextElementVal = nextElement.val
            c = 0
            while nextElement and nextElement.val==backup.val:
                nextElement = nextElement.next
                c+=1
            if c>1:
                curr.next = nextElement
            else:
                curr = backup
        return ans.next                



        