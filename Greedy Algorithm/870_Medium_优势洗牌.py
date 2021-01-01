from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        remain = []
        assigned = {}
        sorted_A = sorted(A)
        sorted_B = sorted(B)
        slow = fast = 0
        ans = []

        while slow < len(sorted_B) and fast < len(sorted_A):
            if sorted_A[fast] <= sorted_B[slow]:
                remain.append(sorted_A[fast])
                fast += 1
            else:
                if sorted_B[slow] in assigned:
                    assigned[sorted_B[slow]] += [sorted_A[fast]]
                else:
                    assigned[sorted_B[slow]] = [sorted_A[fast]]
                slow += 1
                fast += 1

        for i in range(len(B)):
            if B[i] in assigned and assigned[B[i]]:
                ans.append(assigned[B[i]].pop())
            else:
                ans.append(remain.pop())

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.advantageCount(A=[2, 7, 11, 15], B=[1, 10, 4, 11]))
    print(S.advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]))
    print(S.advantageCount(A=[2, 0, 4, 1, 2], B=[1, 3, 0, 0, 2]))
