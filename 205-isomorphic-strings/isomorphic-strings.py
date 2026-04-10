class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        hashmap = defaultdict()
        hashmap2 = defaultdict()

        for i in range(len(s)):
            if s[i] in hashmap.keys() and hashmap[s[i]] != t[i]:
                return False
            if t[i] in hashmap2.keys() and hashmap2[t[i]] != s[i]:
                return False
            else:
                hashmap[s[i]] = t[i]
                hashmap2[t[i]] = s[i]
    

        return True