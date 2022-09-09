# Word Formation
# Link: https://binarysearch.com/problems/Word-Formation
# Difficulty: Easy


# class Solution:
#     def solve(self, words, letters):
#         letter_count = Counter(letters)
#         print(letter_count)

#         maxL = 0

#         words.sort()
#         print(words)
#         for word in words:
#             possible = True
#             for letter in word:
#                 if letter in letter_count and letter_count[letter] >= word.count(letter):
#                     continue
                
#                 else:  # letter not in letter_count:  or letter_count <= word.count(letter)
#                     possible = False
#                     break
                    
#             if possible:
#                 maxL = max(len(word), maxL)
#         return maxL

####################################################################################

# class Solution:
#     def solve(self, words, letters):
#         letter_count = Counter(letters)
#         print(letter_count)

#         maxL = 0

#         # words.sort()
#         # print(words)
#         for word in words:
#             count = 0
#             for letter in word:
#                 if letter in letter_count and letter_count[letter] >= word.count(letter):
#                     count += 1 
#                 else:  # letter not in letter_count: or letter_count[letter] <= word.count(letter):
#                     count = 0
#                     break 

#             if len(word) == count:
#                 maxL = max(len(word), maxL)
#         return maxL

##################################################################################

class Solution:
    def solve(self, words, letters):
        max_length = 0
        letterCount = {}
        for letter in letters:
            if letter in letterCount:
                letterCount[letter] += 1
            else:  # letter not in letterCount:
                letterCount[letter] = 1

        for word in words:
            wordCount = {}
            possible = True
            for w in word:
                if w in wordCount:
                    wordCount[w] += 1
                else:
                    wordCount[w] = 1

            for w in wordCount:
                if w in letterCount and letterCount[w] >= wordCount[w]:
                    continue
                else:
                    possible = False
                    break

            if possible:
                max_length = max(len(word), max_length)

        return max_length