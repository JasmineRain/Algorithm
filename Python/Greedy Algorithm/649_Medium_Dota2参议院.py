from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = deque()
        dire = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + len(senate))
            else:
                dire.append(dire[0] + len(senate))
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"


if __name__ == "__main__":
    S = Solution()
    print(S.predictPartyVictory("RD"))
    print(S.predictPartyVictory("RDD"))
    print(S.predictPartyVictory("DDDRRRR"))
    print(S.predictPartyVictory("RRDDD"))
    print(S.predictPartyVictory("RDRDD"))
    print(S.predictPartyVictory("DRRDRDRDRDDRDRDR"))
