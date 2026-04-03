class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            signature = tuple(sorted(s))
            if signature in groups:
                groups[signature].append(s)
            else:
                groups[signature] = [s]
        return list(groups.values()) 
