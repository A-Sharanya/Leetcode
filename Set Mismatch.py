class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        duplicate = -1
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] = -nums[index]
                
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
                
        return [duplicate, missing]