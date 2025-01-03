/*

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

*/

int isVowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int maxVowels(char* s, int k) {
    int max = 0;
    int cur = 0;
    int n = strlen(s);
    for (int i = 0; i < k; i++)
    {
        if (isVowel(s[i]))
            cur++;
    }
    if (cur > max)
        max = cur;
    for (int i = k; i < n; i++)
    {
        if (isVowel(s[i - k]))
            cur--;
        if (isVowel(s[i]))
            cur++;
        if (cur > max)
            max = cur;
    }
    return (max);
}