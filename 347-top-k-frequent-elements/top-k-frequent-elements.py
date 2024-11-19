class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        only_elements = [i[0] for i in count.most_common(k)]
        return (only_elements)