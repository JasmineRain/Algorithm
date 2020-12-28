from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # 首先将数组排序，按照身高降序、前人数升序排序
        # 然后依次向队伍中插入，如果队伍中人数大于将要插入的元素的前人数，那么根据该元素的前人数插入相应位置，否则加到队伍末尾
        # 合理性在于，因为事先已经按身高排序，后处理的人必是身高更矮的，即使插入到已经排好的身高更高的人前面，也不影响身高更高元素的正确性
        # 只需要保证自己插入位置的正确性即可，贪心策略在于只需要考虑自己，其它元素的正确性已由事先排序保证

        res = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for i in range(len(people)):
            if res and len(res) > people[i][1]:
                res.insert(people[i][1], people[i])
            else:
                res.append(people[i])

        return res


if __name__ == "__main__":
    S = Solution()
    print(S.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(S.reconstructQueue(people=[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
