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


# Merge sorted array - Easy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        maxlength = m+n-1
        finished = False
        while not finished:
            numswaps = 0
            
            for i in range(maxlength):
                if nums1[i] > nums1[i+1]:
                    temp = nums1[i]
                    nums1[i] = nums1[i+1]
                    nums1[i+1] = temp
                    numswaps += 1   
                    
            if numswaps == 0:
                finished = True

### Result:
Runtime: 48 ms, faster than 30.75% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.###


# Valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = False
        if s == "":
            return True
        temp = ""
        teststr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in s:
            if i in teststr:
                temp = temp + i.lower()
        
        if temp == "":
            return True
        
        rev = temp[::-1]
        if temp == rev:
            result = True
        return result    


### Result: Incorrect solution.  Had a problem with padding using zeros. ###

# Add two numbers - medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def turnListIntoString(self, a1: ListNode) -> str:
        result = ""
        while a1:
            result = result + str(a1.val)
            a1 = a1.next
        return result
    
    def turnStringIntoList(self, s1: str) -> ListNode:        
        for i,item in enumerate(s1):
            if i==0:
                l = ListNode(item)
                lprime = l
            else:    
                l.next = ListNode(item)
                l = l.next            
        return lprime              
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        s1 = self.turnListIntoString(l1)
        s2 = self.turnListIntoString(l2)
        sprime1 = s1[::-1]
        sprime2 = s2[::-1]
        total = int(sprime1) + int(sprime2)        
        t1 = str(total)            
        tprime1 = t1[::-1]
        result = self.turnStringIntoList(tprime1)
        return result
        

"""
Success
Details
Runtime: 64 ms, faster than 92.80% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
"""

# Longest palindrome - medium
class Solution:
    
    def llSubstrings(self, s: str) -> list:
        result = list()
        if len(s) == 0:
            return result
        if len(s) == 1:
            result.append(s)
            return result
        if self.testForPal(s):
            result.append(s)
            return result
        else:                   
            for i in range(1, len(s)):
                numsubs = len(s) + 1 - i
                for j in range(numsubs):
                    tend = j + i
                    result.append(s[j:tend])            
        return result
    
    def testForPal(self, s: str) -> bool:
        result = False        
        sprime = s[::-1]
        if s == sprime:
            result = True
        return result
    
    def longestPalindrome(self, s: str) -> str:
        result = ""
        length = 0
        subs = self.llSubstrings(s)
        if len(subs) == 0:
            return ""
        if len(subs) == 1:
            return subs[0]
        else:
            for item in subs:
                if self.testForPal(item):
                    if len(item) > length:
                        length = len(item)
                        result = item
        return result                
        
"""
Success
Details
Runtime: 6652 ms, faster than 11.93% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 213.1 MB, less than 5.04% of Python3 online submissions for Longest Palindromic Substring.       
"""    

# Problem - Merge two sorted lists - easy.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if not l1 == None and l2 == None:
            return l1       
        
        t1 = l1
        while not t1 == None:
            v1 = t1.val
            t2 = l2
            j1 = ListNode(v1)
            m1 = None
            while not t2 == None and t2.val <= v1:
                m1 = t2
                t2 = t2.next
            if m1 == None:
                # nothing happened - need to prepend
                m1 = j1
                m1.next = t2
                l2 = m1
            if not m1 == None and t2 == None: 
                # need to append
                m1.next = j1
            if not m1 == None and not t2 == None:     
                # insert between m1 and t2                
                j1.next = t2                
                m1.next = j1                           
            
            t1 = t1.next
        return l2 

""" Memory limit exceeded.  My code worked for the example, but failed when submitted. """  
        

