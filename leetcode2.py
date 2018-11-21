# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, x):
  #      self.val = x
   #     self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        num1=0
        num2=0
        summ=0
        digit=0
        
        while l1:
            num1 = num1 + l1.val * pow(10,digit)
            l1=l1.next
            digit+=1
        
        
        digit=0
        while l2:
            num2 = num2 + l2.val * pow(10,digit)
            l2=l2.next
            digit+=1
        
        
        add = num1 + num2
        add = str(add)
        
        
       
        head = ListNode(add[len(add)-1])
        answer = head
        for i in reversed(range(0, len(add)-1)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer

