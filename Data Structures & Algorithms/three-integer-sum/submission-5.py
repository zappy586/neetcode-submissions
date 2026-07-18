class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(len(nums)-1):
            compli = 0 - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == compli:
                    list_add = [nums[i], nums[j], nums[k]]
                    if list_add not in result:
                        result.append(list_add)
                    j+= 1
                    k-= 1
                elif nums[j] + nums[k] > compli:
                    k -= 1
                else:
                    j += 1
        return result


# [-4, -1, -1, 0, 1, 2]
# seen = {}, result = []
# i = -4, compli = +4
# j = i + 1, k = n - 1
# if j + k == compli, then we put [n[i], n[j], n[k]] into result
# else, if j + k > 0 -> k--, or if j + k < 0 -> j++
# if j == k, stop the loop and proceed to next i.  