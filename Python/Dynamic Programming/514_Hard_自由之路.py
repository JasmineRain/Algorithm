from collections import Counter


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        # pre-processing
        pos = Counter()
        for idx, c in enumerate(ring):
            if c in pos:
                pos[c] = pos[c] + [idx]
            else:
                pos[c] = [idx]

        # 定义dp[i][j]为：拼出key[i]，且ring[j]对齐12点方向需要移动最少的步数
        # 无穷大表示不可能完成，因为只有ring[j]为key[i]时，才算是拼出了key[i]
        # 初始状态12点方向为ring[0]
        dp = [[float("inf") for _ in range(len(ring))] for _ in range(len(key))]

        for i in pos[key[0]]:
            dp[0][i] = min(i, len(ring) - i) + 1
        n = len(ring)
        for i in range(len(key)):
            for j in pos[key[i]]:
                for k in pos[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j - k), n - abs(j - k)) + 1)

        return min(dp[-1])


if __name__ == "__main__":
    S = Solution()
    print(S.findRotateSteps(ring="godding", key="gd"))
