class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        hashmap = defaultdict()

        for i in range(len(s)):
            if s[i] in hashmap.keys() and hashmap[s[i]] != t[i]:
                return False
            else:
                hashmap[s[i]] = t[i]
    
        hashmap = defaultdict()

        for i in range(len(s)):
            if t[i] in hashmap.keys() and hashmap[t[i]] != s[i]:
                return False
            else:
                hashmap[t[i]] = s[i]
    
        return True