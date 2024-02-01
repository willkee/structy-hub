def five_sort(nums):
  
  pointer = 0
  count = 0
  
  while (pointer < len(nums)):
    if (nums[pointer] == 5):
      nums.pop(pointer)
      count += 1
    else:
      pointer += 1
  
  nums.extend([5] * count)
  
  return nums
​
print(five_sort([12, 5, 1, 5, 12, 7]))