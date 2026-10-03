#two sum

from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        dict_of_target_and_index = {nums[i]:i for i in range(len(nums))}

        for i in range(len(nums)):
            trial_diff = nums[i] - target
            diff = trial_diff if trial_diff + nums[i] == target else target - nums[i]
            if diff in dict_of_target_and_index and dict_of_target_and_index[diff] != i:
                return [i, dict_of_target_and_index[diff]]
        return None

def main():
    nums = [2, 7, 4, 6]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()