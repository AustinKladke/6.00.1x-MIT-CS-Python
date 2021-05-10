# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:37:20 2021

@author: akladke
"""

import string

# letter_lst = []
# num_lst = []
# count_lower = 1
# for i in string.ascii_lowercase:
#     print(ord(i))
#     letter_lst.append(i)
#     num_lst.append(count_lower)
#     count_lower += 1
    
# print(letter_lst)
# print(num_lst)

original_dict = {}
count_lower = 1
for i in string.ascii_lowercase:
    original_dict[i] = count_lower
    original_dict[i] = ord(i)
    count_lower += 1
    
print(original_dict)

original_dict_2 = {}
count_upper = 1
for i in string.ascii_uppercase:
    original_dict_2[i] = count_upper
    original_dict_2[i] = ord(i)
    count_upper += 1

print(original_dict_2)

# Practice shifting dictionary key values by certain amounts
# Need to shift each letter by certain amount, making sure that
# it circles back to 0 (or 97) if goes beyond end of alphabet. Can
# then use chr to convert the number back into the right letter so
# can end up with example: {A:C, B:D}, etc.
# ord range for lowercase letters => 97 - 122

shift = 3
for i in original_dict:
    if original_dict[i] + shift > 122:
        x = (122 - original_dict[i])
        x2 = abs(shift - x)
        original_dict[i] = chr(97 + x2 - 1)
    else:
        original_dict[i] += shift
        original_dict[i] = chr(original_dict[i])

print(original_dict)

#for i in original_dict:
    #original_dict[i] = chr(original_dict[i])

#print(original_dict)

# for i in original_dict:
    # original_dict[i] = original_dict[i].upper()
    # original_dict[i] = original_dict.pop(i.upper())

# print(original_dict)

# ord range for uppercase letters => 65 - 90
shift = 3
for i in original_dict_2:
    if original_dict_2[i] + shift > 90:
        x = (90 - original_dict_2[i])
        x2 = abs(shift - x)
        original_dict_2[i] = chr(65 + x2 - 1)
    else:
        original_dict_2[i] += shift
        original_dict_2[i] = chr(original_dict_2[i])

print(original_dict_2)

final_combined_dict = {}
final_combined_dict.update(original_dict)
final_combined_dict.update(original_dict_2)
print(final_combined_dict)

# Use cipher to translate word
word = 'abc jkl. Ok 123!'
new_dict = final_combined_dict
new_word = ""
for i in word:
    try:
        new_word += new_dict[i]
    except:
        new_word += i
print(new_word)
