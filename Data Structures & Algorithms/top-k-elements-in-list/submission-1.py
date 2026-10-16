class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary??? 
        #edge case
        #bucket sort
        if not nums:
            return []
        count = defaultdict(int)
        #count frequencies 0 -> n hence n+1 spaces
        freq = [[] for i in range(len(nums) + 1)]
        #result list
        res = []
        for i in nums:
            count[i] = count[i] + 1
        for i in count:
            idx = count.get(i)
            freq[idx].append(i)
        for i in freq[::-1]:
            if i:
                for num in i:
                    if len(res) < k:
                        res.append(num)
                    else:
                        return res
        
        return res
        

