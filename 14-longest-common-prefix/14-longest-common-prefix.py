class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = "" #prefix is null
        if len(strs) == 0: #if the list is empty it should return empty
            return " "
        elif len(strs) == 1:#if the list is 1 it should return the first word in the list
            return strs[0]
        for i in xrange(len(min(strs))):
                c = strs[0][i]
                if all(a[i]==c for a in strs):
                    prefix+=c
                else:
                    break
        return prefix
                    
        """
        :type strs: List[str]
        :rtype: str
        """
        