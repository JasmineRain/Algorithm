from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
        if carry:
            digits = [1] + digits
        return digits


if __name__ == "__main__":
    S = Solution()
    print(S.plusOne([4, 3, 2, 1]))
    print(S.plusOne([9, 9, 9]))
    print(S.plusOne([0]))
