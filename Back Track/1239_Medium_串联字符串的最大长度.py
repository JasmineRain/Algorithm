from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0

        def backtrack(start, trace):
            nonlocal ans
            ans = max(ans, len(trace))

            for i in range(start, len(arr)):
                temp = list(trace)
                word = arr[i]
                usable = True
                for s in word:
                    if s in temp:
                        usable = False
                        break
                    else:
                        temp.append(s)
                if usable:
                    backtrack(i + 1, trace + word)

        backtrack(0, "")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
