class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key=k
        num_dict = {}
        for num in nums:
            if num_dict.get(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        return sorted(num_dict, key=lambda x: num_dict[x], reverse=True)[:k] 
        