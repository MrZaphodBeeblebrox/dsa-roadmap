class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        result_dict = {}

        for word in strs:
            hashable_key = tuple(sorted(word))
            if result_dict.get(hashable_key) is None:
                result_dict[hashable_key] = [word]
            else:
                result_dict[hashable_key].append(word)

        return list(result_dict.values())


def main():
    sol = Solution()
    result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(result)

if __name__ == '__main__':
    main()
