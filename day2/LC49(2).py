class Solution(object):
    def groupAnagrams(self, strs):
        prime_map = {
    'a': 2,  'b': 3,  'c': 5,  'd': 7,  'e': 11,
    'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
    'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
    'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
    'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,
    'z': 101
}   
        groups = {}
        for s in strs:
            prod =1 
            for ch in s:
                prod *= prime_map[ch]
            if prod in groups:
                groups[prod].append(s)
            else:
                groups[prod]= [s]
        return list(groups.values())
                