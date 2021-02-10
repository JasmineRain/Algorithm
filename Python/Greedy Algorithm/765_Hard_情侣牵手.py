from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        info = [0] * len(row)
        ans = 0

        # 创建索引数组，info[0]表示0号同学所在的位置
        for i in range(len(row)):
            info[(row[i] // 2) * 2 + row[i] % 2] = i

        # 贪心，从头开始，给坐在偶数位置且旁边不是各自情侣的人配对
        # 合理性在于，从后面找出当前同学的情侣进行换座，一定不会增加换位次数
        # 例如 0 6 2 4 3 5 1 7  其中2 4 3 5只需要一次交换，那么在给0找情侣时，不可能会从这4个人里找到
        # 因为一次交换满足2对情侣配对的情况，说明这4人一定能组成2对情侣
        # 判断两人是否为情侣，可以使用异或运算
        for i in range(0, len(row), 2):
            if row[i] ^ row[i + 1] != 1:
                cp = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
                move = row[i + 1]
                row[i + 1], row[info[cp]] = cp, row[i + 1]
                info[move] = info[cp]
                info[cp] = i + 1
                ans += 1
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.minSwapsCouples(row=[0, 2, 4, 6, 7, 1, 3, 5]))
    print(S.minSwapsCouples(row=[2, 0, 5, 4, 3, 1]))
    print(S.minSwapsCouples(row=[0, 2, 1, 3]))
    print(S.minSwapsCouples(row=[3, 2, 0, 1]))
