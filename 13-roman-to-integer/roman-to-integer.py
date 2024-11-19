class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        lenn = len(s)
        val = 0
        i = 0
        lastInt = float(inf)
        while i < lenn:
            if lastInt < vals.get(s[i]):
                val += (vals.get(s[i]) - 2*lastInt)
            else:
                val += vals.get(s[i])
                lastInt = vals.get(s[i])
            print(s[i], vals.get(s[i]), val) 
            i += 1
        return val