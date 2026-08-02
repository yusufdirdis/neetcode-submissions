class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} #Value , Index

        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[j] = i
        


        