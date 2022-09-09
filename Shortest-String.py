# Shortest String
# Link: https://binarysearch.com/problems/Shortest-String
# Difficulty: Easy


# class Solution:
#     def solve(self, s):
#         return abs(len(s) - 2 * s.count("1"))
        
##############################################################

# class Solution:
#     def solve(self, s):
#         return abs(s.count('1') - s.count('0'))

###############################################################

class Solution:
    def solve(self, s):
        stack = []
        for num in s:
            if not stack or stack[-1] == num:
                stack.append(num)
            else:  # stack[-1] != num:  eg: "10" or "01" in a string: "110001100"
                stack.pop()
        return len(stack)

#################################################################