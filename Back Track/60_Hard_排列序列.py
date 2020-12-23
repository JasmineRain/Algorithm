import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        seq = 0
        ans = ""
        flag = [False] * (n + 1)

        def backtrack(num, trace):

            if num == n:
                nonlocal seq
                nonlocal ans
                seq += 1
                if seq == target:
                    ans = trace
                    return True
                else:
                    return False

            for i in range(1, n + 1):
                if not flag[i]:
                    flag[i] = True
                    if backtrack(num + 1, trace + str(i)):
                        return True
                    flag[i] = False

        branch = math.factorial(n - 1)
        skip = (k - 1) // branch
        target = (k - 1) % branch + 1
        flag[skip + 1] = True
        backtrack(1, str(skip + 1))
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.getPermutation(n=3, k=3))
