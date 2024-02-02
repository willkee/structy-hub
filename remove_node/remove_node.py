# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def remove_node(head, target_val):
  if not head: return None
  if head.val == target_val: 
    if head.next == None: return None
    else: head = head.next
  
  prev = head
  current = head.next
  
  while current is not None:
    if current.val != target_val: 
      prev = current
      current = current.next
    else:
      prev.next = current.next
      break
    
  return head
​