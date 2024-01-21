def most_frequent_char(s):
  dict = {}
  
  for ltr in s:
    if ltr in dict:
      dict[ltr] += 1
    else:
      dict[ltr] = 1
  
  max_count = 0
  max_letter = None
  
  for letter, count in dict.items():
    
    if (count > max_count):
      max_count = count
      max_letter = letter
    
  return max_letter
    