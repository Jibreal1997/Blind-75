# Question1: Two Sum Array


#Brute Force approach
# class Solution:
#   def twoSum(self, nums, target):
#     for i in range(len(nums)):
#       for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#           return [i,j]

# Optimal Approach
class Solution:
  def twoSum(self, nums, target):
    hash_table = {}
    for i in range(len(nums)):
      if nums[i] in hash_table:
        return [hash_table[nums[i]], i]
      else:
        required_number = target - nums[i]
        hash_table[required_number] = i




Test = Solution()
print(Test.twoSum([1,2,4,5,6], 8))
          
    