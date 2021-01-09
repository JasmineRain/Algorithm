from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return
        ans = []
        res = self.merge(num, 0, len(num) - 1)
        for summary, exp in res:
            if summary == target:
                ans.append(exp)
        return ans

    def merge(self, string, left, right):
        if left == right:
            return [[int(string[left]), string[left]]]
        idx = left + (right - left) // 2
        l1 = self.merge(string, left, idx)
        l2 = self.merge(string, idx + 1, right)
        return self.merge_two_lists(l1, l2)

    def merge_two_lists(self, l1, l2):
        res = []
        for e1 in l1:
            for e2 in l2:
                # print(e1, e2)
                res.append([e1[0] + e2[0], e1[1] + "+" + e2[1]])
                res.append([e1[0] - e2[0], e1[1] + "-" + e2[1]])
                res.append([e1[0] * e2[0], e1[1] + "*" + e2[1]])
        return res


if __name__ == "__main__":
    S = Solution()
    # print(S.addOperators(num="123", target=6))
    print(S.addOperators(num="232", target=8))
    # print(S.addOperators(num="105", target=5))
    # print(S.addOperators(num="00", target=0))
    # print(S.addOperators(num="3456237490", target=9191))
