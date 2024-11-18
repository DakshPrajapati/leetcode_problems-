class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1) , len(nums2) 
        i = j = 0
        count = 0
        t1, t2 = ((n + m) // 2) - 1, ((n + m) // 2)  
        v1, v2 = 0, 0
        while True:
            n1 = nums1[i] if i < n else float('inf') 
            n2 = nums2[j] if j < m else float('inf')
            if n1 <= n2:
                i += 1
            else:
                j += 1
            if count == t1:
                v1 = min(n1, n2)
            elif count == t2:
                v2 = min(n1,n2)
                break
            count += 1
        if (m+n)%2 == 0:
            return (v1+v2)/2
        else:
            return v2    
        
            