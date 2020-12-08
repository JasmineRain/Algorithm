from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # 考虑移位操作的本质，对于奇数，右移一位后相当于去掉最后一个二进制位1，偶数则是去掉最后一个0
        # 因此十进制 N 对应二进制位1的个数相当于 N/2 对应1的个数，如果N为奇数，则需+1
        dp = [0] * (num + 1)
        for i in range(0, num + 1):
            dp[i] = dp[i//2] + i % 2
        return dp


if __name__ == "__main__":
    S = Solution()
    print(S.countBits(num=0))
