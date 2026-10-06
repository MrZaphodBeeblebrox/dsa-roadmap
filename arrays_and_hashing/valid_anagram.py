class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            no_of_letters = {}

            ctr = 0
            while ctr < len(s):
                no_of_letters[s[ctr]] = no_of_letters.get(s[ctr], 0) + 1
                no_of_letters[t[ctr]] = no_of_letters.get(t[ctr], 0) - 1
                ctr += 1

            return all(count == 0 for count in no_of_letters.values())

def main():
    sol = Solution()
    sol.isAnagram("anagram", 'anagram')


if __name__ == '__main__':
    main()