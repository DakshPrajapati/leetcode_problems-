class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        '''
        a -> a,e
        e -> e, i
        i -> i, o
        o -> o, u
        u -> u
        if order breaks 

        aeiaaioaaaaeiiiiouuuooaauuaeiu

        lastAdded = 'a'
        {
            a:1
        }

        for r in range(0..n):
            mapp[r] += 1
            if word[r] not in target[lastAdded]:
                while l < r:
                    mapp[l] -= 1
                    l += 1
                    if mapp[l] == 0:
                        map.remove(l)
            else:
                if len(map) == 5:
                    curLen = r - l + 1
                    max = maxCurLen
                lastAdded = word[r]
        
        return maxCurLen
        '''

        hashMap = defaultdict(int)
        lastAdded = 'a'
        valid = {
            'a': ['a', 'e'],
            'e': ['e','i'],
            'i': ['i','o'],
            'o': ['o', 'u'],
            'u': ['u']
        }
        maxLen = 0

        l = 0
        for r in range(len(word)):
            hashMap[word[r]] += 1
            if word[r] not in valid[lastAdded]:
                while l < r:
                    hashMap[word[l]] -= 1
                    if hashMap[word[l]] == 0:
                        hashMap.pop(word[l])
                    l += 1
            else:
                if len(hashMap.keys()) == 5:
                    curLen = r - l + 1
                    maxLen = max(maxLen, curLen)
            lastAdded = word[r]

        return (maxLen)    