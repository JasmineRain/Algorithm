from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def divide_conquer(start, end):

            if str.isdigit(input[start: end + 1]):
                return [int(input[start: end + 1])]

            res = []
            for i in range(start, end + 1):
                op = input[i]
                if op in ['+', '-', '*']:
                    left = divide_conquer(start, i - 1)
                    right = divide_conquer(i + 1, end)

                    for l in left:
                        for r in right:
                            if op == "+":
                                res.append(l + r)
                            elif op == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)
            return res

        return divide_conquer(0, len(input) - 1)


if __name__ == "__main__":
    S = Solution()
    print(S.diffWaysToCompute("2-1-1"))
    print(S.diffWaysToCompute("2*3-4*5"))
    print(S.diffWaysToCompute("3"))
