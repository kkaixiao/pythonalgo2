"""
Given a collection of candidate numbers (candidates) and a target number (target), find all
unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    def generate(self, comb, counter, target):
        if target == 0:
            comb_set = tuple(n for n in sorted(comb))
            if comb_set not in self.visited:
                self.res.append(comb[:])
                self.visited.add(comb_set)
            return
        for num in counter.keys():
            if counter[num] > 0 and target - num >= 0:
                counter[num] -= 1
                self.generate(comb + [num], counter, target - num)
                counter[num] += 1

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        counter = collections.Counter(self.nums)
        self.visited = set()
        self.res = []
        self.generate([], counter, target)
        return self.res