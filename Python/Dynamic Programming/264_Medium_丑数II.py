class Solution:
    def __init__(self):
        self.nums = [0, 1]
        i2 = i3 = i5 = 1
        for i in range(1, 1690):
            cur = min(self.nums[i2] * 2, self.nums[i3] * 3, self.nums[i5] * 5)
            self.nums.append(cur)
            if cur == self.nums[i2] * 2:
                i2 += 1
            if cur == self.nums[i3] * 3:
                i3 += 1
            if cur == self.nums[i5] * 5:
                i5 += 1

    def nthUglyNumber(self, n: int) -> int:
        return self.nums[n]


if __name__ == "__main__":
    S = Solution()
    print(S.nthUglyNumber(n=10))
