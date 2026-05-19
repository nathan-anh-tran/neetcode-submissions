class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[i], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1
                    r -= 1
                    l += 1
        return result