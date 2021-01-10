from typing import List


# 回溯解法
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index, track, value, last):
            if index == len(num):
                if value == target:
                    res.append(track)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                candidate = num[index: i + 1]
                if index == 0:
                    backtrack(i + 1, track + candidate, value + int(candidate), int(candidate))
                else:
                    backtrack(i + 1, track + "+" + candidate, value + int(candidate), int(candidate))
                    backtrack(i + 1, track + "-" + candidate, value - int(candidate), -int(candidate))
                    backtrack(i + 1, track + "*" + candidate, value - last + last * int(candidate),
                              last * int(candidate))

        backtrack(0, "", 0, 0)
        return res


if __name__ == "__main__":
    S = Solution()
    print(S.addOperators(num="105", target=5))
    print(S.addOperators(num="123", target=6))
    print(S.addOperators(num="232", target=8))
    print(S.addOperators(num="00", target=0))
    print(S.addOperators(num="3456237490", target=9191))
