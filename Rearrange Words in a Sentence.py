# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:48:19 2020

@author: Sri
"""

Rearrange Words in a Sentence

Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

Example 1:

Input: text = "Leetcode is cool"
Output: "Is cool leetcode"

Solution1:
    
text = "Swxxmsh qjhcpm tlvmdbava usujd tyt zdn"
text = text.split()
val1 = text[0]
val1 = val1.replace(val1[0],val1[0].lower())
del text[0]
text.insert(0,val1)
lst2 = sorted(list(text), key=len) 
val =  lst2[0]
val = val.replace(val[0],val[0].upper(),1)
del lst2[0]
lst2.insert(0,val)
re_val = " ".join(str(x) for x in lst2)
print(re_val)

Solution2:
    
class Solution:
    def arrangeWords(self, text: str) -> str:
        text = chr(ord(text[0]) + 32) + text[1:]
        dicti = collections.defaultdict(list)
        for t in text.split(" "):
            dicti[len(t)].append(t)
        ans = " ".join(" ".join(dicti[d]) for d in sorted(dicti))
        return chr(ord(ans[0]) - 32) + ans[1:]