/*
For two strings s and t, we say "t divides s" 
if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
*/

#include <stdio.h>
#include <string.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

char *gcdOfStrings(char *str1, char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char concat1[len1 + len2 + 1];
    char concat2[len1 + len2 + 1];
    strcpy(concat1, str1);
    strcat(concat1, str2);
    strcpy(concat2, str2);
    strcat(concat2, str1);
    
    if (strcmp(concat1, concat2) != 0) 
        return "";

    int gcdLen = gcd(len1, len2);

    static char result[1001];
    strncpy(result, str1, gcdLen);
    result[gcdLen] = '\0';

    return result;
}