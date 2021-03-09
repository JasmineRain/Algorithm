import sys


T = int(sys.stdin.readline().strip())

for i in range(T):
    n, k = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))
    pre = nums[0] - 1
    count = 0
    flag = False
    for j in range(len(nums)):
        cur = nums[j]
        if flag:
            break
        if cur - pre - 1 + count < k:
            count += cur - pre - 1
            pre = nums[j]
            continue
        while cur - pre > 1:
            count += 1
            cur -= 1
            if count == k:
                print(pre + nums[j] - cur)
                flag = True
                break
        pre = nums[j]
    if not flag:
        print(nums[-1] + k - count)

# import sys
# T = int(sys.stdin.readline().strip())
#
# for i in range(T):
#     m, n, p = list(map(int, sys.stdin.readline().split()))
#     a = list(map(int, sys.stdin.readline().split()))
#     b = list(map(int, sys.stdin.readline().split()))
#     if n < min(a) or p > sum(b):
#         print(0)
#         continue
#     ans = 0
#     for j in range(0, m):
#         for k in range(j + 1, m):
#             if sum(a[j:k]) <= n and sum(b[j:k]) >= p:
#                 ans += 1
#     print(ans)







# class Solution:
#     def longestConsecutive(self, nums):
#         longest_streak = 0
#         num_set = set(nums)
#
#         for num in num_set:
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1
#
#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1
#
#                 longest_streak = max(longest_streak, current_streak)
#
#         return longest_streak

