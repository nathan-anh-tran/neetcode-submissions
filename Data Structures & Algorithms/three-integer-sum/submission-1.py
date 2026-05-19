class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    result.add((nums[l], nums[i], nums[r]))
                    r -= 1
        result = set(result)
        return list(result)