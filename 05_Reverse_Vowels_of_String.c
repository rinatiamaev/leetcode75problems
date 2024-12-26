/*
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
*/

#include <string.h>
#include <stdbool.h>

bool is_vowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' 
        || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

char* reverseVowels(char* s) {
    int i = 0;
   
    int slen = strlen(s);
    int j = slen - 1;
    char temp;
    while (i < j)
    {
        if (!is_vowel(s[i]))
        {
            i++;
            continue;
        }
        if (!is_vowel(s[j]))
        {
            j--;
            continue;
        }
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
    return s;
}