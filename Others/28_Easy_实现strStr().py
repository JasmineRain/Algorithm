class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0
        sidx = pidx = 0
        while sidx < len(haystack) - len(needle) + 1:
            while sidx < len(haystack) and haystack[sidx] != needle[0]:
                sidx += 1

            while sidx < len(haystack) and pidx < len(needle) and haystack[sidx] == needle[pidx]:
                sidx += 1
                pidx += 1

            if pidx == len(needle):
                return sidx - pidx

            sidx = sidx - pidx + 1
            pidx = 0

        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.strStr(haystack="a", needle='a'))