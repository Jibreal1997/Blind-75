class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0
        left = 0
        right = 0
        # For the odd conditon 
        for middle in range(len(s)):
            left , right = middle, middle
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > resultLength:
                    resultLength = right - left + 1
                    result = s[left:right + 1]
                
                left -= 1
                right += 1
                
        
        # For the even condition
            left, right = middle, middle + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > resultLength:
                    resultLength = right - left + 1
                    result = s[left:right + 1]
                
                left -= 1
                right += 1
        
        return result
        
            
        
test = Solution()
print(test.longestPalindrome("babad"))
