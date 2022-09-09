# Rotate List Left by K
# Link: https://binarysearch.com/problems/Rotate-List-Left-by-K
# Difficulty: Easy


# Time Limit Exceded
# class Solution:
#     def solve(self, nums, k):
#         if len(nums) == k or len(nums) == 1:
#             return nums

#         else:
#             for i in range(k):
#                 x = nums.pop(0)
#                 nums.append(x)
#             return nums

#######################################################

# class Solution:
#     def solve(self, nums, k):
#         # if len(nums) == k or len(nums) == 1:
#         #     return nums
#         left_TO_K = nums[: k]
#         nums = nums[k:]
#         return nums + left_TO_K

#########################################################

class Solution:
    def solve(self, nums, k):
        return nums[k:] + nums[:k]