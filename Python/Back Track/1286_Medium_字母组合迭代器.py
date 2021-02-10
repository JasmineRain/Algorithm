class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.seq = -1
        self.ans = []
        flag = [False] * len(characters)

        def backtrack(index, trace):
            if len(trace) == combinationLength:
                self.ans.append(trace)
                return
            for i in range(index, len(characters)):
                if flag[i]:
                    continue
                else:
                    flag[i] = True
                    backtrack(i + 1, trace + characters[i])
                    flag[i] = False

        backtrack(0, "")
        # print(self.ans)

    def next(self) -> str:
        self.seq += 1
        return self.ans[self.seq]

    def hasNext(self) -> bool:
        return self.seq < len(self.ans) - 1


if __name__ == "__main__":
    iterator = CombinationIterator("abc", 2)
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
