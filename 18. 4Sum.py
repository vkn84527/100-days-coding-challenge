class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(y, x = 0):
            while x < y:
                low, high = x + 1, y - 1
                base_sum = nums[x] + nums[y]

                while low < high:
                    val = base_sum + nums[low] + nums[high]
                    if val == target:
                        res.add((nums[x], nums[low], nums[high], nums[y]))
                        low += 1
                    elif val > target: high -= 1
                    elif val < target: low += 1
                x += 1

        nums.sort()
        res = set()
        for y in range(len(nums)-1, -1, -1): helper(y)

        return [list(x) for x in res]
