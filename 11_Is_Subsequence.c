/*
A subsequence of a string 
is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

*/

#include <stddef.h>
bool isSubsequence(char* s, char* t) {
    int i = 0;
    int j = 0;
    while (s[i])
    {
        while (t[j])
        {
            if (s[i] == t[j])
            {
                i++;
                j++;
                break;
            }
            j++;
        }
        if (t[j] == '\0')
            break;
    }
    if (s[i] == '\0')
        return (true);
    return (false);
}