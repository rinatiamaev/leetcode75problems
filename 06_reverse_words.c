/*
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
*/

#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char* reverseWords(char* s) {
    int len = strlen(s);
    char *res = (char *)malloc(len + 1);
    if (!res) return NULL;

    int i = len - 1;
    int j = 0;

    while (i >= 0) {
        while (i >= 0 && isspace(s[i])) i--; // Пропустить пробелы
        int end = i;
        if (i < 0) break;
        while (i >= 0 && !isspace(s[i])) i--; // Найти начало слова
        int start = i + 1;

        for (int k = start; k <= end; k++) {
            res[j++] = s[k];
        }
        if (j < len) {
            res[j++] = ' ';
        }
    }

    if (j > 0 && res[j - 1] == ' ') {
        res[j - 1] = '\0'; 
    } else {
        res[j] = '\0';
    }

    return res;
}