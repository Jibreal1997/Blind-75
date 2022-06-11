# Question2:Longest Substring Without Repeating Characters

#Optimal Approach
class Solution:
  def longestSubstring(self,str):
    # Create left slider, result and window set
    left = 0
    result = 0
    windowSet = set()
    # Traverse through the array
    for right in range(len(str)):
      while(str[right] in windowSet):
        windowSet.remove(str[left])
        left += 1
      windowSet.add(str[right])
      result = max(result, (right - left) + 1)

    return result

test = Solution()
print(test.longestSubstring("JibrealJibreal"))
    
