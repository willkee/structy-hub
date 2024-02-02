# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def get_node_value(head, index):
  
  current_index = 0
  while (head is not None):
    if index == current_index:
      return head.val
    current_index += 1
    head = head.next
  
  return None