# Question 5: Two SUM part 2
class Solution:
  def twoSum(self, numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
      if numbers[left] + numbers[right] < target:
        left += 1
      elif numbers[left] + numbers[right] > target:
        right -= 1
      else:
        return [left + 1, right + 1]

test = Solution()
print(test.twoSum([1,2,3,4,5,6,7,8], 10))
        