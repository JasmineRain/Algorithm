from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        pocket = {
            5: 0,
            10: 0
        }
        for i in range(len(bills)):
            if bills[i] == 5:
                pocket[5] += 1
                continue
            elif bills[i] == 10:
                if pocket[5] == 0:
                    return False
                pocket[10] += 1
                pocket[5] -= 1
            elif bills[i] == 20:
                if pocket[10] > 0 and pocket[5] > 0:
                    pocket[10] -= 1
                    pocket[5] -= 1
                elif pocket[5] >= 3:
                    pocket[5] -= 3
                else:
                    return False

        return True


if __name__ == "__main__":
    S = Solution()
    print(S.lemonadeChange([5,5,5,5,20,20,5,5,20,5]))
