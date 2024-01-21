def anagrams(s1, s2):
  dict = {}
  for char in s1:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  
  for char in s2:
    if char not in dict:
      return False
    elif dict[char] == 0:
      return False
    
    dict[char] -= 1
  
  for val in dict.values():
    if val != 0: return False
  
  return True