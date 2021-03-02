# class Solution:
#     def calc(self, x, patience):
#         left, right = 0., x
#         while left < right:
#             mid = (left + right) / 2
#             temp = mid * mid
#             if abs(temp - x) <= patience:
#                 return mid
#             elif temp < x:
#                 left = mid
#             else:
#                 right = mid

class Solution:
    def trace(self, m):
        ans = []
        flag = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
        length = float("inf")
        def backtrack(route, row, col):
            if m[row][col] == 1 or flag[row][col]:
                return
            if m[row][col] == 2:
                route.append([row, col])
                ans.append(route.copy())
                return
            route.append([row, col])
            flag[row][col] = True
            if row + 1 < len(m):
                backtrack(route, row + 1, col)
            if row - 1 >= 0:
                backtrack(route, row - 1, col)
            if col + 1 < len(m[0]):
                backtrack(route, row, col + 1)
            if col - 1 >= 0:
                backtrack(route, row, col - 1)
            flag[row][col] = False
            route.pop()

        backtrack([], 0, 0)
        for r in ans:
            length = min(length, len(r))
        return length


if __name__ == "__main__":
    S = Solution()
    print(S.trace())
