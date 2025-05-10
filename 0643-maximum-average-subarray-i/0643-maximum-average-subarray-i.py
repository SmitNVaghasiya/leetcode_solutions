class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        maxAvg = 0
        for i in range(k):
            maxSum += nums[i]
        maxAvg = maxSum / k
        for right in range(k, len(nums)):
            maxSum = (maxSum + nums[right]) - nums[right - k]
            # maxAvg = max(maxAvg, (maxSum / k))
            if((maxSum / k) > maxAvg):
                maxAvg = maxSum / k
        return maxAvg