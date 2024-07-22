from typing import List
import unittest

class Interweave:
    """https://www.lintcode.com/problem/144/
    给出一个含有正整数和负整数的数组，重新排列成一个正负数交错的数组。
    
    prepare with partition O(N)
    two pointers interweaving O(N)               
    """    
    
    def rearrange(self, nums: List[int]) -> List[int]:
        # partition to pos negative
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] < 0:
                i += 1
            while i <= j and nums[j] > 0:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        # two pointer to interweave
        # i make sure neg/pos/neg, j make sure pos
        i = 0
        try:
            j = [n>0 for n in nums].index(True)  
        except ValueError: # edge case all negative
            return nums
                    
        for i in range(0, len(nums)):                        
            if i % 2 and nums[i] < 0: # odd for positive
                nums[i], nums[j] = nums[j], nums[i]
                j += 1            
                
class SortLettersByCase:
    """
    给定一个只包含字母的字符串 chars，按照先小写字母后大写字母的顺序进行排序。
    对于不同的语言，chars将以不用的形式给出，例如对于字符串 "abc" ，将以下面的形式给出

    Java: char[] chars = {'a', 'b', 'c'};
    Python：chars = ['a', 'b', 'c']
    C++：string chars = "abc";
    你需要实现原地算法解决这个问题，不需要返回任何值，我们会根据排序后的chars判断你的结果是否正确。
    """               
    def sort(self, input: List[str]):
        i = 0
        j = len(input) - 1
        while i <= j:
            while i <= j and input[i].islower():
                i += 1
            while i <= j and input[j].isupper():
                j -= 1
            if i <= j:
                input[i], input[j] = input[j], input[i]
                i += 1
                j -= 1        
                
    def sort_with_prime_pointer(self, input: List[str]):
        """Iterate the primary pointer only. The other pointers to maintain the partition.
        """
        i, j, k = -1, 0, len(input)
        while j < k:
            if input[j].islower():
                i += 1
                input[i], input[j] = input[j], input[i]
                j += 1                
            elif input[j].isupper():
                k -= 1
                input[j], input[k] = input[k], input[j]
            else:
                j += 1
        

class TestPartition(unittest.TestCase):
    def test_interveving(self):
        inter = Interweave()        
        nums = [-1, -2, -3, 4, 5, 6]
        inter.rearrange(nums)
        self.assertEqual([-1, 4, -3, 5, -2, 6], nums)
        
        
        nums = [-1, -2, 4, -3, 5, 6]
        inter.rearrange(nums)
        self.assertEqual([-1, 4, -3, 5, -2, 6], nums)
        
                
        nums = [1,2,3]
        inter.rearrange(nums)
        self.assertEqual([1,2,3], nums)
        
                
                
        nums = [-1,-2,3,4,5,6,7]
        inter.rearrange(nums)
        self.assertEqual([-1,3,-2,4,5,6,7], nums)
        
    def test_sort_by_case(self):
        sort_by_case = SortLettersByCase()
        input = ['a','b','A','c','D']
        sort_by_case.sort(input)
        self.assertEqual(['a', 'b', 'c', 'A', 'D'], input)
        
        input = ['a','b','A','c','D']
        sort_by_case.sort_with_prime_pointer(input)
        self.assertEqual(['a', 'b', 'c', 'D', 'A'], input)
        
        input = ['a','b','c']
        sort_by_case.sort_with_prime_pointer(input)
        self.assertEqual(['a', 'b', 'c'], input)
        
                
        input = ['A','B','C']
        sort_by_case.sort_with_prime_pointer(input)
        self.assertEqual(['B', 'C', 'A'], input)