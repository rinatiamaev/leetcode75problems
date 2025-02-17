# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = Counter(t) 
        required_chars = len(t_count)
        left, right = 0, 0
        formed = 0 
        window_counts = {}  
        min_len = float("inf")
        min_window = ""
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            while left <= right and formed == required_chars:
                char = s[left]
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                left += 1
            right += 1 
        
        return min_window
