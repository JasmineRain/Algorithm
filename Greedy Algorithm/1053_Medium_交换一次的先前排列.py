from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        max_num_idx = 0
        max_num = 0

        # 从后往前，找到第一个下标i，使得arr[i-1]的值大于arr[i]的值
        # 然后从[i, 结尾]中找出 排在最高位的 且  比arr[i-1]小的最大数 进行替换
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                for j in range(i, len(arr)):
                    if arr[i - 1] > arr[j] > max_num:
                        max_num = arr[j]
                        max_num_idx = j
                arr[max_num_idx] = arr[i - 1]
                arr[i - 1] = max_num
                return arr

        return arr


if __name__ == "__main__":
    S = Solution()
    print(S.prevPermOpt1(arr=[1, 9, 4, 6, 7]))
    print(S.prevPermOpt1(arr=[3, 2, 1]))
    print(S.prevPermOpt1(arr=[1, 1, 5]))
    print(S.prevPermOpt1(arr=[3, 1, 1, 3]))
