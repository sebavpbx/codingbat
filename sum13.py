def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    if nums.count(13) == 0:
      return sum(nums)
    else:
      next2change = False
      listCopy = []
      listCopy.extend(nums)
      for x in nums:
        if next2change:
          listCopy.remove(x)
          next2change = False
        else:
          if x == 13:
            listCopy.remove(13)
            next2change = True
      return sum(listCopy)
