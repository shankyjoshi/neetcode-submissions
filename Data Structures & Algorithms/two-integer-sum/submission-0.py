class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # run a loop over all numbers
        # starting with first number and adding rest of the numbers to get to target sum 
        # retrun the answer with smallest index first


        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
        
        return [-1, -1]