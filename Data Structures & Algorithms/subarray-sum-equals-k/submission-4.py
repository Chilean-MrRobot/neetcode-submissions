class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum created
        ps = [0 for i in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            ps[i+1] = ps[i] + nums[i]

        count_sa = 0
        df = {}
        for psj in ps:
            if psj - k in df:
                count_sa += df[psj - k]
            df[psj] = df.get(psj, 0) + 1
                
        return count_sa
