class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 
        count_of_items: dict = {}

        for item in nums:
            count_of_items[item] = count_of_items.get(item, 0) + 1

        result: list = k*[None]
        _keys = list(count_of_items.keys())


        for elem in _keys: 
            ctr = 0
            while ctr < k and result[ctr] != None and count_of_items[elem] < count_of_items[result[ctr]]:
                ctr += 1
                
            if ctr < k:
                result = self.helper_ka_helper(result, elem, index= ctr, k= k)
            
        return result

    def helper_ka_helper(self, result: list, elem: int,* , index: int, k: int):
        temp = result[index]
        result[index] = elem
        while index < k-1: 
            temp2 = result[index + 1]
            result[index + 1] = temp
            temp = temp2
            index += 1

        return result




def main():
    sol = Solution()
    result = sol.topKFrequent(nums= [1,1,1,2,2,3], k = 2)
    print(result)


if __name__ == '__main__':
    main()