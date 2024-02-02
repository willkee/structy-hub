class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def create_linked_list(values):
  if not len(values): return
​
  head = Node(values[0])
  current = head
  
  for i in range(1, len(values)):
    current.next = Node(values[i])
    current = current.next
  
  return head
    
​