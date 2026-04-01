class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        def listToMap(l):
            res = {}
            for idx, word in enumerate(l):
                res[word] = idx
            return res
        
        map1, map2 = listToMap(list1), listToMap(list2)

        ans = []
        curMin = float('inf')

        for key in map1.keys():
            if key in map2.keys():
                curSum = map1[key] + map2[key]
                if curSum == curMin:
                    ans.append(key)
                elif curSum < curMin:
                    curMin = curSum
                    ans = []
                    ans.append(key)
            
        return (ans)