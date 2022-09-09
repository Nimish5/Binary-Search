# Sum of Two Numbers with Sorted List
# Link: https://binarysearch.com/problems/Sum-of-Two-Numbers-with-Sorted-List
# Difficulty: Easy


# class Solution:
#     def solve(self, nums, k):
#         s = set()
#         for num in nums:
#             if k - num in s:
#                 return True

#             s.add(num)
#         return False

###############################################

class Solution:
    def solve(self, nums, k):
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_up = nums[left] + nums[right]
            if sum_up == k:
                return True

            elif sum_up > k:
                right -= 1
                continue

            else:   # sum_up < k:
                left += 1

        return False