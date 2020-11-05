from typing import List
from collections import Counter


class Solution:
    def findSubstring_Iterate(self, s: str, words: List[str]) -> List[int]:
        words_map = Counter(words)
        # for word in words:
        #     words_map.setdefault(word, 0)
        #     words_map[word] += 1
        ans = []
        length = len(s)
        word_len = len(words[0])
        word_num = len(words)
        for i in range(0, length - word_len * word_num + 1):

            cur_words = {}
            cur_word_num = 0
            substr = s[i: i + word_len * word_num]

            while cur_word_num < word_num:
                cur_word = substr[cur_word_num * word_len: (cur_word_num + 1) * word_len]
                if cur_word in words_map.keys():
                    cur_words.setdefault(cur_word, 0)
                    cur_words[cur_word] += 1
                    if cur_words[cur_word] > words_map[cur_word]:
                        break
                else:
                    break
                cur_word_num += 1
            if cur_word_num == word_num:
                ans.append(i)
        return ans

    def findSubstring_IterateByWord(self, s: str, words: List[str]) -> List[int]:
        words_map = Counter(words)
        ans = []
        length = len(s)
        word_len = len(words[0])
        word_num = len(words)
        for i in range(word_len):
            cur_words = {}
            cur_word_num = 0
            left = right = i
            while right + word_len <= length:
                cur_word = s[right: right + word_len]
                right += word_len
                cur_words.setdefault(cur_word, 0)
                cur_words[cur_word] += 1
                cur_word_num += 1
                while cur_words[cur_word] > words_map[cur_word]:
                    drop = s[left: left + word_len]
                    left += word_len

                    cur_words[drop] -= 1
                    cur_word_num -= 1
                if cur_word_num == word_num:
                    ans.append(left)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.findSubstring_IterateByWord(s="barfoothefoobarman", words=["foo", "bar"]))
