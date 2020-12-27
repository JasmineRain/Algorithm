from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        slow = fast = 0

        while slow < len(g) and fast < len(s):
            if g[slow] <= s[fast]:
                count += 1
                slow += 1

            fast += 1

        return count

    # 不止分一个饼干的解法
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     g.sort()
    #     s.sort()
    #     count = 0
    #     slow = fast = 0
    #     temp = 0
    #
    #     while slow < len(g) and fast < len(s):
    #         if g[slow] > temp + s[fast]:
    #             fast += 1
    #         else:
    #             slow += 1
    #             fast += 1
    #             temp = 0
    #             count += 1
    #     return count


if __name__ == "__main__":
    S = Solution()
    print(S.findContentChildren(g=[1, 2, 3], s=[1, 1, 1, 1, 1, 1]))
    print(S.findContentChildren(g=[7, 8, 9, 10], s=[5, 6, 7, 8]))
