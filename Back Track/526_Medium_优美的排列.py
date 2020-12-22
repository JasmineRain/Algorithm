class Solution:
    def countArrangement(self, N: int) -> int:
        # 将搜寻过程视为填数字的过程
        # 需要传递的状态仅有1个，为当前填到第几个空
        flag = [False] * (N + 1)
        total = 0

        def backtrack(index):

            if index == N + 1:
                nonlocal total
                total += 1
                return

            for i in range(1, N + 1):
                if not flag[i] and (i % index == 0 or index % i == 0):
                    flag[i] = True
                    backtrack(index + 1)
                    flag[i] = False

        backtrack(1)
        return total


if __name__ == "__main__":
    S = Solution()
    print(S.countArrangement(N=2))
