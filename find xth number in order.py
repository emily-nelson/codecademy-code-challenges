def getX(x, nums):
  if x > len(nums) or not nums:
    return 0

  return sorted(nums)[x-1]

print(getX(2, [6, 3, -1, 5]))

# x is position, nums is a list of numbers
# sorts list then uses [x-1] to find index and return it