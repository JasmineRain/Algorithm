from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        if len(s) > 12:
            return []

        def backtrack(index, trace):

            if len(trace) == 4 and index == len(s):
                ans.append(".".join(trace))
                return

            if index == len(s):
                return

            for i in range(index, min(index + 3, len(s))):
                subs = s[index: i + 1]
                if len(str(int(subs))) != len(subs) or int(subs) > 255:
                    continue
                else:
                    trace.append(subs)
                    backtrack(i + 1, trace)
                    trace.pop()

        backtrack(0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.restoreIpAddresses(s="25525511135"))
