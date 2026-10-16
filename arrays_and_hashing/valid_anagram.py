class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            list_of_alphabets = [0] * 26
            for i, j in zip(s, t):
                list_of_alphabets[ ord(i) - ord('a')] += 1
                list_of_alphabets[ ord(j) - ord('a')] -= 1

            return all(count == 0 for count in list_of_alphabets)

def main():
    sol = Solution()
    sol.isAnagram("car", 'rat')


if __name__ == '__main__':
    main()