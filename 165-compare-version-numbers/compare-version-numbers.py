class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) < len(v2):
            for _ in range(0,len(v2) - len(v1)):
                v1.append('0')
        elif len(v2) < len(v1):
            for _ in range(0,len(v1) - len(v2)):
                v2.append('0')
        for i in range(0,len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v2[i]) > int(v1[i]):
                return -1
        return 0