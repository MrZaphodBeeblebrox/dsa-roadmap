class Solution:
    def isPalindrome(self, s: str) -> bool:

        is_a_palindrome = True
        l = ''
        for _char in s.lower():
            ascii_val = ord(_char)
            if ascii_val < 123 and ascii_val > 96 or ascii_val in range(48, 58):
                l += _char

        i = 0
        j = len(l) - 1

        while i <= j:
            if l[i] != l[j]:
                is_a_palindrome = False

            i += 1
            j -= 1
        
        return is_a_palindrome