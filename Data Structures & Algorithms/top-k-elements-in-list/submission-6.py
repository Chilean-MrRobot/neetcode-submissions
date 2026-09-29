import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm_freqs = {}
        list_heap = []
        heapq.heapify(list_heap)

        for num in nums:
            if num in hm_freqs.keys():
                hm_freqs[num] += 1
            else:
                hm_freqs[num] = 1

        for num, freq in hm_freqs.items():
            heapq.heappush(list_heap, (freq, num))
            if len(list_heap) > k:
                heapq.heappop(list_heap)

        return [heap_el[1] for heap_el in list_heap]
            
        