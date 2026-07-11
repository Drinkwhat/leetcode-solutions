class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if target - nums[i] in data: 
                return [data[res], i]
            data[nums[i]] = i

        