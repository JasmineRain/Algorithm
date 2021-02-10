from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Hash  = {0: -1}
        residual = 0
        for j in range(len(nums)):
            residual += nums[j]
            if k != 0:
                residual = residual % k
            if Hash.get(residual) is not None:
                if j - Hash[residual] > 1:
                    return True
            else:
                Hash[residual] = j
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.checkSubarraySum(nums=[2, 4], k=6))
