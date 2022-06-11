# Quesiton 4: Container with the most water

# Brute Force Approach
# class Solution:
#   def maxArea(self, hieght):
#     result = 0
#     for left in range(len(hieght)):
#       for right in range(left + 1, len(hieght)):
#         area = (right - left) * min(hieght[left], hieght[right])
#         result = max(result, area)

#     return result 



# Optimal Approach:
class Solution():
  def maxArea(self, hieght):
    result = 0
    area = 0
    left = 0
    right = len(hieght) - 1
    while(left < right):
      area = (right - left) * min(hieght[right], hieght[left])
      result = max(result, area)
      if hieght[left] > hieght[right]:
        right -= 1
      elif hieght[left] < hieght[right]:
        left += 1
      # For equal
      else:
        left += 1

    return result


test1 = Solution()
print(test1.maxArea([1,8,6,2,5,4,8,3,7]))




    