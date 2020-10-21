class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        flag = -1
        i = 0
        for c in s:
            res[i] += c
            if i == 0 or i == (numRows - 1):
                flag = -flag
            i += flag

        return "".join(res)


if __name__ == "__main__":
    S = Solution()
    print(S.convert(s="LEETCODEISHIRING", numRows=4))