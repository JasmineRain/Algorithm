from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        ans = [""] * len(S)
        count = Counter(S)
        index = 0
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(count)
        if 2 * count[0][1] - 1 > len(S):
            return ""

        for pair in count:
            item = list(pair)
            while item[1]:
                ans[index] = item[0]
                item[1] -= 1
                index += 2
                if index >= len(S):
                    index = 1

        return "".join(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.reorganizeString(S="abbabbaaab"))
