class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(nums) == 0:
            return 0
        max_len = 1
        for num in num_set:
            left_nbr = num-1
            if left_nbr not in num_set:
                right_nbr = num+1
                counter = 1
                if right_nbr not in num_set:
                    continue
                else:
                    while right_nbr in num_set:
                        counter += 1
                        right_nbr += 1
                if counter > max_len:
                    max_len = counter
        return max_len
            