'''Longest Substring Without Repeating Characters — Given string s, return length of longest substring with all unique characters.
Example:
If s = "abcabcbb", the longest substring without repeating characters is "abc", and its length is 3.
If s = "bbbbb", the longest substring without repeating characters is "b", and its length is 1.
If s = "pwwkew", the longest substring without repeating characters is "wke", and its length is 3. Note that "pwke" is a subsequence, not a substring.
Substring = a contiguous squence of string'''





# Brute force technique

def lengthOfLongestSubstringBrute(s: str):
    n = len(s)
    max_len = 0

    # for i in range(0,n):
    #     for j in range(i+1,n):

