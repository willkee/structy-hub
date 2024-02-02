# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def reverse_list(head):
  
  current = head
  prev = None
  next = None
  
  while (current is not None):
    next = current.next
    current.next = prev
    prev = current
    
    current = next
  
  return prev
    
  
​