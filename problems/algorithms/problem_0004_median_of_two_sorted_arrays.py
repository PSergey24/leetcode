class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_nums = nums1 + nums2
        total_nums.sort()
        a, b = divmod(len(total_nums), 2)
        if b == 0:
            return float(sum(total_nums[a-1:a+1])/2)
        else:
            return float(total_nums[a])