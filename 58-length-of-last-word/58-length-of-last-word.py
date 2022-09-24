class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        li = list(s.split(" "))
        li = li[-1]
        li = len(li)
        return li
        