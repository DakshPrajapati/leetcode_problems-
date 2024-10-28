class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        firstlen = m
        if firstlen > 0 and n > 0:
            while True:
                if i>=firstlen or not nums2:
                    break
                elif nums1[i] <= nums2[0]:
                    i = i + 1
                elif nums2[0] < nums1[i]:
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
                    nums1.pop()
                    firstlen = firstlen + 1 
        if nums2:
            for i in range(m+n-len(nums2), len(nums1)):
                nums1[i] = nums2[0]
                nums2.pop(0)
       
            