class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map={}
        for i in range(0,len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for i in hash_map:
            if hash_map[i] >=2:
                return True
        return False
        