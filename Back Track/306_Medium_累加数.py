class Solution:
    def isAdditiveNumber(self, num):

        def backtrack(i, j, k):
            # 判断是否是01这种情况
            # i, j, k分别表示连续3个数的起始下标
            if num[i] == '0' and j - i > 1 or num[j] == '0' and k - j > 1:
                return False
            a = num[i:j]
            b = num[j:k]
            c = str(int(a) + int(b))
            size = len(c)
            if c != num[k:k + size]:
                return False
            if k + size == len(num):
                return True
            return backtrack(j, k, k + size)

        for j in range(1, len(num)):
            for k in range(j + 1, len(num)):
                if backtrack(0, j, k):
                    return True
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.isAdditiveNumber("112358"))
    print(S.isAdditiveNumber("199100199"))
    print(S.isAdditiveNumber("1991001991"))
