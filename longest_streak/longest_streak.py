# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def longest_streak(head):
  if not head or not head.val: return 0
  if head.next == None: return 1
​
  map = {}
  prev = head
  current = head.next
  
  map[head.val] = 1
  
  while current is not None:
    if current.val in map:
      if prev.val == current.val:
        map[current.val] += 1
      else:
        map[current.val] = 1
    else:
        map[current.val] = 1
    
    prev = current
    current = current.next
  
  return max(map.values())
  
​