class Solution:
    # def minAddToMakeValid(self, S: str) -> int:
    #     exist = 0
    #     left = right = 0
    #
    #     for i in range(len(S)):
    #         if S[i] =="(":
    #             exist += 1
    #         elif exist == 0:
    #             left += 1
    #         else:
    #             exist -= 1
    #     exist = 0
    #     for i in range(len(S) - 1, -1, -1):
    #         if S[i] == ")":
    #             exist += 1
    #         elif exist == 0:
    #             right += 1
    #         else:
    #             exist -= 1
    #
    #     return left + right
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


if __name__ == "__main__":
    S = Solution()
    print(S.minAddToMakeValid("())"))
    print(S.minAddToMakeValid("((("))
    print(S.minAddToMakeValid("()))(("))
