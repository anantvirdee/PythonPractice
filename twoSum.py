#https://leetcode.com/problems/two-sum/
#Brute force approach, O(n^2) time

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for item in range(len(nums)):
        for i in range(item + 1, len(nums)):
            if nums[item] + nums[i] == target:
                return [item, i]

res = twoSum([2,7,11,15],9)

print(res)