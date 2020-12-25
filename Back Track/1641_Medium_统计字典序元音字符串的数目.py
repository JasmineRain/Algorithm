import math

class Solution:
    # def countVowelStrings(self, n: int) -> int:
    #     chars = ['a', 'e', 'i', 'o', 'u']
    #     ans = 0
    #
    #     def backtrack(index, trace):
    #
    #         if len(trace) == n:
    #             nonlocal ans
    #             ans += 1
    #             return
    #         for i in range(index, 5):
    #             backtrack(i, trace + chars[i])
    #
    #     backtrack(0, "")
    #     return ans

    # 隔板法   4个隔板放置在n+1个位置   将位置分成5份  用于放置5个字符
    # python >= 3.8
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)


if __name__ == "__main__":
    S = Solution()
    print(S.countVowelStrings(n=33))
