class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        '''
        Step 1: Convert the list of string to dictionaries representing items from the original list strs
        Step 2: Traverse from the new dict and find the matching/similar representation and replace them with None once the match is found.
        '''

        if len(strs) == 1:
            return [strs]
        
        result_list_of_dict = []
        dict_of_strs = []
        for _str in strs:
            hash_of_str = {}
            for _let in _str:
                hash_of_str[_let] = hash_of_str.get(_let, 0) + 1

            dict_of_strs.append(hash_of_str)

        i, j = 0, 1
        
        while i < len(dict_of_strs):
            temp = []
            if dict_of_strs[i] is not None:
                temp.append(strs[i])

                while j < len(dict_of_strs):
                    if dict_of_strs[i] == dict_of_strs[j]:
                        temp.append(strs[j])
                        dict_of_strs[j] = None
                    j += 1

            i += 1
            j = i + 1
            if temp != []:
                result_list_of_dict.append(temp)

        return result_list_of_dict

def main():
    sol = Solution()
    result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(result)

if __name__ == '__main__':
    main()
