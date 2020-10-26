class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        inputs = list(s)
        pre = 0
        for i in range(len(inputs)):
            if i == 0:
                continue
            if dictionary[inputs[pre]] < dictionary[inputs[i]]:
                ans -= dictionary[inputs[pre]]
            else:
                ans += dictionary[inputs[pre]]
            pre = i
        ans += dictionary[inputs[pre]]
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.romanToInt(s="XXXX"))