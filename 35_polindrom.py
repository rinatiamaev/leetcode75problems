class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for char in s:
            if char.isalnum():  
                a.append(char.lower())  
        return a == a[::-1]
s = "A man, a plan, a canal: Panama"
bool1 = isPalindrome(s)
print(bool1)
