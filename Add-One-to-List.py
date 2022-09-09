# Add One to List
# Link: https://binarysearch.com/problems/Add-One-to-List
# Difficulty: Easy


# Not sutaible for some test cases

# class Solution:
#     def solve(self, nums):
#         nums[-1] += 1
#         if nums[-1] == 10:
#             nums.pop(-1)
#             nums.extend([1, 0])
#         return nums

#####################################################
# Not suitable for some test case

# class Solution:
#     def solve(self, nums):
#         if nums[-1] >= 9:
#             nums[-1] = 0
#             if len(nums) == 1:
#                 nums.insert(0, 1)
#             else:
#                 nums[-2] += 1
#         else:  
#             nums[-1] += 1
#         return nums

#######################################################
# Prefreable Solution

class Solution:
    def solve(self, nums):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] < 9:   # nums[i] + 1 <= 9:
                nums[i] += 1
                break
            else:    # nums[i] == 9:  
                nums[i] = 0
            i -= 1
        if i < 0:   # len(nums) == 0:
            nums.insert(0, 1)
        return nums

#############################################################

# class Solution:
#     def solve(self, nums):
#         new = nums[::-1]
#         i = 0
#         while True:
#             if new[i] == 9:
#                 new[i] = 0
#                 if i == len(new) - 1:
#                     new.append(1)
#                     break
#                 # i += 1
#             else:
#                 new[i] += 1
#                 break
#             i += 1

#         return new[::-1]
