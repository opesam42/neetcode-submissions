class Solution:
    def topKFrequentNaive(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            else:
                count[num] += 1
        
        sorted_group = sorted(count.items(), key=lambda item: item[1], reverse=True)
        result = [item[0] for item in sorted_group[:k]]

        return result
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        print(f"Count {count}")
        
        buckets = []
        # as bucket takes freq from 0 to n (as we can have same no through our the list)
        for i in range(len(nums) + 1):
            bucket = []
            buckets.append(bucket)

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                
                # stopping condition
                if len(result) == k:
                    return result