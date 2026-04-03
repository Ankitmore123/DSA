class Solution(object):
    def isAnagram(self, s, t):
        freq_s= {}
        freq_T = {}
        for ch in s:
            freq_s[ch] = freq_s.get(ch,0)+1
        for ch in t:
            freq_T[ch] = freq_T.get(ch,0)+1
        if freq_s == freq_T:
            return True
        else:
            return False