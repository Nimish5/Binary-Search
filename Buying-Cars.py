# Buying Cars
# link: https://binarysearch.com/problems/Buying-Cars
# difficulty: Easy


class Solution:
    def solve(self, prices, k):
        prices.sort()
        total = 0
        count = 0
        for price in prices:
            total += price
            if total <= k:
                count += 1
            else: # total > k:
                break
        return count

##################################################

# class Solution:
#     def solve(self, prices, k):
#         prices.sort()
#         total = 0
#         count = 0
#         for price in prices:
#             if price + total <= k:
#                 total += price
#                 count += 1

#             else:
#                 break
#         return count

#################################################

# class Solution:
#     def solve(self, prices, k):
#         prices.sort()
#         total = 0
#         for i, price in enumerate(prices):
#             total += price
#             if total > k:
#                 return i
#         return len(prices)

##################################################
