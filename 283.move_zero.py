from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(nums[last_non_zero_index])
                print(nums[i])
                nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
                last_non_zero_index += 1
   

        
        print("finally...")
        print(nums)


a = Solution()
a.moveZeroes([0,0,1])
        