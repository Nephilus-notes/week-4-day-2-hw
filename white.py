from itertools import zip_longest
# Reformat the String
# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# Return the reformatted string or return an empty string if it is impossible to reformat the string.
# Example 1:
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# Example 2:
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# Example 3:
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.
# Example 4:
# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# Example 5:
# Input: s = "ab123"
# Output: "1a2b3
# """

# def reformat(str_1):
#     num_list = []
#     char_list = []
#     alter_list= []
#     for element in str_1:
#         if element.isdigit():
#             num_list.append(element)
#         elif element.isalpha():
#             char_list.append(element)
#     num_len = len(num_list)
#     char_len = len(char_list)
#     if num_len > char_len + 1 or char_len > num_len + 1:
#         return ''
#     else:
#         if num_len > char_len:
#             return ''.join(list(map(list, zip_longest(num_list, char_list))))
            
#         else:
#             return ''.join(list(map(list, zip_longest(char_list, num_list))))

def reformat(str_1):
    num_list = []
    char_list = []
    alter_list= []
    for element in str_1:
        if element.isdigit():
            num_list.append(element)
        elif element.isalpha():
            char_list.append(element)
    num_len = len(num_list)
    char_len = len(char_list)
    if num_len > char_len + 1 or char_len > num_len + 1:
    # if abs(num_len - char_len) > 1:
        return ''
    else:
        if num_len > char_len:
            while char_list:
                alter_list.append(char_list.pop())
                alter_list.append(num_list.pop())
            if num_list:
                alter_list.append(num_list.pop())
            return ''.join(alter_list)
        else:
            while num_list:
                alter_list.append(char_list.pop())
                alter_list.append(num_list.pop())
            if char_list:
                alter_list.append(char_list.pop())
            return ''.join(alter_list)



# check to see if there are the same number of digits as characters, if not return ''
# if there are the same number, split them into two lists
# alternate between popping from one list then the other until it ends.

   




# print(reformat("a0b1c2"))
# print(reformat("leetcode"))
print(reformat("1229857369"))
print(reformat("covid2019"))
print(reformat("ab123"))