class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxValue = 0
        counter = 0
        for n in nums:     
            if n == 1:
                counter += 1
                if counter > maxValue:
                    maxValue = counter
            elif n == 0:
                counter = 0
                

        return maxValue