# My solutions ro leetcode problems:

# Palidrome number - easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ispal = False
        s = str(x)        
        sprime = s[::-1]        
        if s == sprime:
            ispal = True
        return ispal   


# Two Sum - easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums) - 1
        result = list()
        for i in range(l):
            b = i+1
            for j in range(b,len(nums)):
                if nums[j] + nums[i] == target:
                    result.append(i)
                    result.append(j)
                    return result
        return result  


# Reverse Integer - easy

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = -x
            neg = True
        s = str(x)
        sprime = s[::-1]
        y = int(sprime)
        if neg == True:
            y = -y
        if y < pow(-2,31) or y > pow(2,31)-1:
            return 0
        else:
            return y


# Valid Parentheses - easy

class Solution:
    def isopen(self, c: str) -> bool:
        if c == '[' or c == '(' or c == '{':
            return True
        
    def compare(self, a: str, b: str) -> bool:
        result = False
        if a == '{' and b == '}':
            result = True
        if a == '[' and b == ']':
            result = True
        if a == '(' and b == ')':
            result = True
            
        return result    
    
    def isValid(self, s: str) -> bool:
        l = list()
        for i in s:
            if self.isopen(i):
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                else:
                    ind = len(l) - 1
                    if self.compare(l[-1], i):
                        item = l.pop(ind)
                    else:
                        return False
        if len(l) == 0:
            return True
        else:
            return False


# Remove Element - easy

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        finished = False        
        l = len(nums)  - 1
        while not finished: 
            numswaps = 0
            for i in range(l):
                if nums[i] == val and not nums[i+1] == val:
                    # swap
                    w = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = w
                    numswaps += 1
            if numswaps == 0:
                finished = True
        return len(nums) - nums.count(val)        
    



