from collections import defaultdict, deque
from typing import List


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     situations = []
    #     ans = []
    #     min_length = len(wordList)
    #     flag = [False] * len(wordList)
    #
    #     def backtrack(num, trace):
    #         nonlocal min_length
    #         if trace[-1] == endWord:
    #             situation = [beginWord] + trace
    #             min_length = min(min_length, len(situation))
    #             situations.append([beginWord] + trace)
    #             return
    #
    #         if num == min_length:
    #             return
    #
    #         for i in range(0, len(wordList)):
    #             if not flag[i] and sum(1 for s1, s2 in zip(trace[-1], wordList[i]) if s1 != s2) == 1:
    #                 flag[i] = True
    #                 backtrack(num + 1, trace + [wordList[i]])
    #                 flag[i] = False
    #
    #     # early return
    #     if endWord not in wordList:
    #         return []
    #
    #     # main process
    #     # search for the first transformable word
    #     for i in range(len(wordList)):
    #         if sum(1 for s1, s2 in zip(beginWord, wordList[i]) if s1 != s2) <= 1:
    #             flag[i] = True
    #             backtrack(1, [wordList[i]])
    #             flag[i] = False
    #
    #     # select the shortest answers
    #     for i in range(len(situations)):
    #         if len(situations[i]) == min_length:
    #             ans.append(situations[i])
    #
    #     return ans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        ### 构建具有邻接关系的桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i + 1:]
                buckets[match].append(word)
        ##### BFS遍历
        preWords = defaultdict(list)  # 前溯词列表
        toSeen = deque([(beginWord, 1)])  # 待遍历词及深度
        beFound = {beginWord: 1}  # 已探测词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i + 1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level + 1
                        toSeen.append((word, level + 1))
                    if beFound[word] == level + 1:  # 当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            if endWord in beFound and level + 1 > beFound[endWord]:  # 已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]]
            return res
        else:
            return []


if __name__ == "__main__":
    S = Solution()
    print(S.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    print(S.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
