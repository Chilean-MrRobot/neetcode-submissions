import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuencies = {}
        for num in nums:
            if num in frecuencies.keys():
                frecuencies[num] += 1
            else:
                frecuencies[num] = 1

        heap = []
        heapq.heapify(heap) 
        # adding values to heap
        for key, value in frecuencies.items():
            # swith biggest to lowest (*-1)
            heapq.heappush(heap, (-value, key))

        # extract negative top 2 values
        return_list = []
        for i in range(k):
            (_, key) = heapq.heappop(heap)
            return_list.append(key)

        return return_list
        