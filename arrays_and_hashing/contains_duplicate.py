class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

def main():
    sol = Solution()
    sol.containsDuplicate([2, 4, 7, 7])

if __name__ == '__main__':
    main()