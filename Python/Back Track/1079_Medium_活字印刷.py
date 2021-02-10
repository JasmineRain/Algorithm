class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        flag = [False] * len(tiles)
        ans = 0
        tiles = "".join(sorted(list(tiles)))

        def backtrack(trace):
            if len(trace):
                nonlocal ans
                ans += 1
            for i in range(len(tiles)):
                if flag[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i - 1] and not flag[i - 1]:
                    continue
                flag[i] = True
                backtrack(trace + [tiles[i]])
                flag[i] = False

        backtrack([])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.numTilePossibilities("AAABBC"))
