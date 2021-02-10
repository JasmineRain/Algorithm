from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        most_task = max(count.values())
        most_task_num = sum(1 for item in count.values() if item == most_task)

        return max(len(tasks), (most_task - 1) * (n + 1) + most_task_num)


if __name__ == "__main__":
    S = Solution()
    print(S.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
    print(S.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))
    print(S.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
