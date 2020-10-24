from typing import List


# 基本回溯算法，注意这里有先后顺序，枚举数目为全排列的 1/(n!)，因此回溯时需要传入下标以示顺序
class Solution:
    res = []
    track = []
    dictionary = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        # leetcode对所有测试用例仅创建一个S，不清空会导致所有用例结果堆叠，可以通过注释下面这行获取leetcode测试用例。。。这算不合理设计？
        self.res = []
        if not digits:
            return []
        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits, i):

        if len(self.track) == len(digits):
            self.res.append("".join(self.track))
        else:
            digit = digits[i]
            chars = self.dictionary[digit]
            for c in chars:
                self.track.append(c)
                self.backtrack(digits, i + 1)
                self.track.pop()


if __name__ == "__main__":
    S = Solution()
    print(S.letterCombinations(""))



