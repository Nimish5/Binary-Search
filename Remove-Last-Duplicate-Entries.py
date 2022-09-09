# Remove Last Duplicate Entries
# Link: https://binarysearch.com/problems/Remove-Last-Duplicate-Entries
# Difficulty: Easy


from collections import Counter
class Solution:
    def solve(self, nums):
        count = Counter(nums)
        sett = set()
        # if you take list instead of sett it will also work but in binary serach it will through an error i.e Time Limit Exceeded.

        for i in reversed(range(len(nums))):
            # if count[nums[i]] != 1 and nums[i] not in sett:
            if count[nums[i]] > 1 and nums[i] not in sett:
                sett.add(nums[i])
                nums.pop(i)
        return nums


##################################################################
# Time Limit Exceeded

# class Solution:
#     def solve(self, nums):
#         duplicate = {}
#         for i in range(len(nums)):
#             if nums.count(nums[i]) > 1:
#                 duplicate[nums[i]] = i
        
#         for val in reversed(sorted(duplicate.values())):
#             nums.pop(val)
#         return nums

##################################################################

# class Solution:
#     def solve(self, nums):
#         count = Counter(nums)
#         result = []

#         for num in reversed(nums):
#             if count[num] == 1:
#                 result.append(num)
#             else:  # count[num] != 1 or count[num] > 1:
#                 count[num] = 1
#         result.reverse()
#         return result

###################################################################

# class Solution:
#     def solve(self, nums):
#         count = Counter(nums)
#         nums.reverse()
#         # print(nums)

#         for i, j in count.items():
#             if j > 1:
#                 nums.remove(i)
#         nums.reverse()
#         return nums

###################################################################

