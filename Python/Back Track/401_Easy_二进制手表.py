from typing import List
import numpy as np


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        nums = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        flag = [False] * 10
        ans = []

        def get_time():
            h = 0
            m = 0
            for i in range(len(nums)):
                if not flag[i]:
                    continue
                else:
                    if i <= 5:
                        m += nums[i]
                    else:
                        h += nums[i]
            return "%d:%02d" % (h, m)

        def check_time():
            h = 0
            m = 0
            for i in range(len(nums)):
                if not flag[i]:
                    continue
                else:
                    if i <= 5:
                        m += nums[i]
                    else:
                        h += nums[i]
            return 0 <= h <= 11 and 0 <= m <= 59

        def backtrack(used, start):
            if used == num:
                ans.append(get_time())
                return

            for i in range(start, len(nums)):
                flag[i] = True
                start = i + 1
                used += 1
                if not check_time():
                    flag[i] = False
                    start -= 1
                    used -= 1
                    continue
                else:
                    backtrack(used, start)
                    flag[i] = False
                    start -= 1
                    used -= 1

        backtrack(0, 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    A = ["0:03","0:05","0:09","0:17","0:33","1:01","2:01","4:01","8:01","0:06","0:10","0:18","0:34","1:02","2:02","4:02","8:02","0:12","0:20","0:36","1:04","2:04","4:04","8:04","0:24","0:40","1:08","2:08","4:08","8:08","0:48","1:16","2:16","4:16","8:16","1:32","2:32","4:32","8:32","3:00","5:00","9:00","6:00","10:00","12:00"]
    B = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
    print(np.setdiff1d(np.array(S.readBinaryWatch(num=2)), np.array(B)))
    print(np.setdiff1d((B), np.array(S.readBinaryWatch(num=2))))
    print(S.readBinaryWatch(num=2))
