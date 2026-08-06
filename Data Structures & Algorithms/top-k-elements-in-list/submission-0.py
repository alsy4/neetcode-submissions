class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = defaultdict()

        for num in nums:
            count_num[num] = count_num.get(num, 0) + 1

        count_num = dict(sorted(count_num.items(), key=lambda item:item[1], reverse=True))

        return list(count_num.keys())[:k]