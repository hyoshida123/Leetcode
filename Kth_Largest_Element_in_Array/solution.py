class Solution(object):
	def findKthLargest(self, nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	return sorted(nums)[len(nums) - k]
