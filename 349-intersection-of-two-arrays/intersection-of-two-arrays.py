class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)

        res = []

        for number in n1:
            if number in n2:
                res.append(number)

        return res 