from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        def check(x):
            up = down = 0
            for i in range(len(A)):
                if A[i] == x and B[i] == x:
                    continue
                elif A[i] != x and B[i] != x:
                    return -1
                elif A[i] == x:
                    down += 1
                else:
                    up += 1
            # print(up, down)
            return min(up, down)

        res = check(A[0])

        # 注意  不需要考虑A[0]和B[0]均能匹配上的情况  因为这种情况已经在A[0]中考虑到
        if res != -1 or A[0] == B[0]:
            return res
        else:
            return check(B[0])


if __name__ == "__main__":
    S = Solution()
    print(S.minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))
    print(S.minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]))
