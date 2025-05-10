class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sum = 0
        min_length = sys.maxsize

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                if(i- left + 1 < min_length):
                    min_length = i - left + 1
                sum -= nums[left]
                left += 1
        return min_length if min_length != sys.maxsize else 0