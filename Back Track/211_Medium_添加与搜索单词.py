class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        # def backtrack(item, num):
        #     if num == len(word):
        #         return True
        #     if word[num] != "." and word[num] != item[num]:
        #         return False
        #     return backtrack(item, num + 1)

        def check_match(pattern, target):
            for i in range(len(pattern)):
                if pattern[i] != target[i] and pattern[i] != ".":
                    return False
            return True

        for item in self.words:
            if len(item) != len(word):
                continue
            # if backtrack(item, 0):
            #     return True
            if check_match(word, item):
                return True

        return False


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("at")
    wordDictionary.addWord("and")
    wordDictionary.addWord("an")
    wordDictionary.addWord("add")
    # print(wordDictionary.search("a"))     # F
    # print(wordDictionary.search(".at"))   # F
    wordDictionary.addWord("bat")
    print(wordDictionary.search(".at"))   # T
    print(wordDictionary.search("an."))   # T
    print(wordDictionary.search("a.d."))  # F
    print(wordDictionary.search("b."))    # F
    print(wordDictionary.search("a.d"))   # T
    print(wordDictionary.search("."))     # F
