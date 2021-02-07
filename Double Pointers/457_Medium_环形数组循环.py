from collections import Counter
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 0:
            return False
        for i in range(length):
            flag = nums[i]
            slow = fast = i
            while nums[slow] * nums[fast] > 0 and nums[(fast + nums[fast]) % length] * flag > 0:
                slow = (slow + nums[slow]) % length
                fast = (fast + nums[fast]) % length
                fast = (fast + nums[fast]) % length
                if slow == fast:
                    if slow == (slow + nums[slow]) % length:
                        break
                    return True
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.circularArrayLoop([1, 1, 1, 1, 1, 1, 1, 1, 1, -5]))
    print(S.circularArrayLoop([-1, -1, -1]))
    print(S.circularArrayLoop([2, -1, 1, 2, 2]))
    print(S.circularArrayLoop([-1, 2]))
    print(S.circularArrayLoop([-2, 1, -1, -2, -2]))
    print(S.circularArrayLoop([3, 1, 2]))
    print(S.circularArrayLoop([3, 2, 1]))
