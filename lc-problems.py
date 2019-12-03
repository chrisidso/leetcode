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


# Length of last word - easy
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0 or s.isspace() == True:
            return 0
        else:
            result = list()
            sprime = s.split(' ')
            for item in sprime:
                if len(item) > 0:
                    result.append(item)
            return len(result[-1])        

""" Result:
Success
Details
Runtime: 28 ms, faster than 87.24 - % of Python3 online submissions for Length of Last Word.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Length of Last Word.    """


# Plus one - easy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lprime = digits[::-1]
        mult = 1
        sum = 0
        for item in lprime:
            sum += item*mult
            mult = mult*10
        
        sum += 1
        
        sumst = str(sum)
        result = list()
        for item in sumst:
            result.append(item)
            
        return result    

""" Result:
Success
Details
Runtime: 32 ms, faster than 85.45% of Python3 online submissions for Plus One.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Plus One. """


# Sqrt(x) - easy ... (OK. Too easy.)
class Solution:
    def mySqrt(self, x: int) -> int:
        stage1 = math.sqrt(x)
        return int(stage1)

""" Result:
Success
Details
Runtime: 28 ms, faster than 97.01% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
 """

# Remove duplicates from sorted linked list. - easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            mine = ListNode(head.val)       
            mt = mine

            mark = head.val
            ht = head
            while ht.next:
                if not ht.next.val == None and not ht.next.val == mark:
                    temp = ListNode(ht.next.val)
                    mt.next = temp
                    mt = mt.next
                    mark = ht.next.val
                ht = ht.next                 

            return mine
        else:
            return None
                
""" Result:
Success
Details
Runtime: 48 ms, faster than 57.48% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.   """              



    



