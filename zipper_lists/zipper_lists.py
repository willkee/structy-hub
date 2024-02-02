# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def zipper_lists(head_1, head_2):
  
  current1 = head_1
  current2 = head_2
  tail = current1
  count = 0
​
  current1 = current1.next
  
  while (current1 is not None and current2 is not None):
    if count % 2 == 0:
      # even number ( get from list 2 )
      print(tail.val, tail.next.val, 'even')
      tail.next = current2
      tail = current2
      
      current2 = current2.next
    else:
      # odd number ( get from list 1 )
      print(tail.val, tail.next.val, 'odd')
      tail.next = current1
      tail = current1
      
      current1 = current1.next
      
    count += 1
    
  if (current1 is not None):
    tail.next = current1
  else:
    tail.next = current2
  
  return head_1
​
  