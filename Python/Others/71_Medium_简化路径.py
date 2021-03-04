class Solution:
    def simplifyPath(self, path: str) -> str:
        content = path.split("/")
        ans = []
        for item in content:
            if not item or item == ".":
                continue
            elif item == "..":
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append(item)
        return "/" + "/".join(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.simplifyPath(path="/a/./b/../../c/"))
    print(S.simplifyPath(path="/home//foo/"))
    print(S.simplifyPath(path="/../"))
