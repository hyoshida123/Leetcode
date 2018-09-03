class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache.keys():
                return [cache[diff], i]
            cache[nums[i]] = i
