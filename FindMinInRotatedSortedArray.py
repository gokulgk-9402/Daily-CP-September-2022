from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            elif nums[mid] == nums[left] and nums[mid] == nums[right]:
                right = right - 1
                left = left + 1
            elif nums[mid] >= nums[left] and nums[mid] <= nums[right]:
                right = mid - 1
            elif nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1

        return nums[mid]

print(Solution().findMin(nums = [2,2,2,0,1]))