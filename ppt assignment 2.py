#!/usr/bin/env python
# coding: utf-8
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

**Example 1:**
Input: nums = [1,4,3,2]
Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4

# In[19]:


#step by step process:
    
#1.initialize variable sum to 0
#2.lterate through the input array nums and add the even indexed element to sum
#3.return the value of sum

def arrayPairsum(nums):
    sum =0
    nums.sort()
    for i in range(0, len(nums), 2):
        sum += nums[i]
    
    return sum


# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 
# 
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 
# 
# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
# 
# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# 
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

# In[20]:


def maxCandies(candytype):
    unique_candies =set(candyType)
    return min(len(unique_candies), len(candyType) // 2)


# In[21]:


candyType = [1, 1, 2, 2, 3, 3]
max_count =maxCandies(candyType)
print(max_count)


# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.
# 
# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.
# 
# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
# 
# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# 
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# In[23]:


#create an empty dictionary count to store the count of each number 
#iterate through the nums array.
#in each iteration, update the count of the current number in the count dictionary 
#initialize a variable max_lenght to 0
# in each iteration check if the count of the current number plus the count of the number plus one is greater than the current max_lenght
#if is update max_lenght with the new value.
#return the value of max_lenght

def findHLS(nums):
    count = {}
    for num in nums:
        count[nums] = count.get(num, 0 ) + 1
        
    max_lenght= 0
    for num in count:
        if num + 1 in count:
            max_lenght =max(max_lenght, count[num]+ count[num + 1])
            
    return max_lenght


# In[8]:


input_string = input([1, 3, 2, 2, 5, 2, 3, 7])

num_strings = input_string.split()

num = [int(num) for num in num_strings]

print(num)


# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# 
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# In[10]:


def place_flower(flowerbed, n):
    lenght = len(flowerbed)
    count = 0
    i = 0
    
    while i <lenght:
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i -1] == 0) and (i == lenght - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1
    return count >= n

flowerbed = [1, 0, 0, 0, 1]
n = 1
result = place_flower(flowerbed, n)
print(result)


# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# In[13]:


def Maximum_product(nums):
    num.sort()
    n = len(nums)
    
    product1 = nums[0]*nums[n - 2]*nums[n-3]
    product2 = nums[0]*nums[1]*nums[n-1]
    return max(product1, product2)


# In[15]:


nums = [1, 2, 3]
result = Maximum_product(nums)
print(result)


# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# 
# Explanation: 9 exists in nums and its index is 4

# In[21]:


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# In[22]:


nums = [-1, 0, 3, 5, 9, 12]
target =9
result = binary_search(nums, target)
print(result)


# An array is monotonic if it is either monotone increasing or monotone decreasing.
# 
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
# monotone decreasing if for all i <= j, nums[i] >= nums[j].
# 
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
# 
# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# In[24]:


def is_monotonic(nums):
    is_increasing = True
    is_decreasing = True
    
    for i in range (1, len(nums)):
        if nums[i] < nums[i - 1]:
            is_increasing = False
        if nums[i] > nums[i - 1]:
            is_decreasing = False
            
    return is_increasing or is_decreasing


# In[25]:


nums = [1, 2, 2, 3]
result = is_monotonic(nums)
print(result)


# You are given an integer array nums and an integer k.
# 
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.
# 
# The score of nums is the difference between the maximum and minimum elements in nums.
# 
# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
# 
# Example 1:
# Input: nums = [1], k = 0
# Output: 0
# 
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

# In[32]:


def min_score(nums, k):
    min_val = min(nums)
    max_val = max(nums)
    
    if min_val + k >= max_val - k:
        return 0
    return max_val - min_val - 2* k


# In[33]:


nums = [1]
k = 0
result = min_score(nums, k)
print(result)


# In[ ]:




