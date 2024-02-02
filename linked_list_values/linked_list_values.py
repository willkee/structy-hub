# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def linked_list_values(head):
  my_list = []
  
  current = head
  while (current is not None):
    my_list.append(current.val)
    current = current.next
  
  return my_list
​