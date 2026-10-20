from practice.max_heap import MaxHeap

class Solution:
    def __init__(self) -> None:
        self.heap = MaxHeap()

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 
        count_of_items: dict = {}

        for item in nums:
            count_of_items[item] = count_of_items.get(item, 0) + 1

        for key, value in count_of_items.items():
            self.heap.insert((key, value))

        result = []
        for _ in range(k):
            key_value_tuple = self.heap.extract_max()
            if key_value_tuple:
                result.append(key_value_tuple[0])

        return result

def main():
    sol = Solution()
    print(sol.topKFrequent([3,0,1,0], 1))

if __name__ == '__main__':
    main()