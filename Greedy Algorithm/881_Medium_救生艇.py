from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        left, right = 0, len(people) - 1
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.numRescueBoats(people=[3, 5, 3, 4], limit=5))
    print(S.numRescueBoats(people=[3, 2, 2, 1], limit=3))
