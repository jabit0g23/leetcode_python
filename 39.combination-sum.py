class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target)]
        for num in candidates:
            if target - num < 0:
                continue

            dp[num - 1].append([num])
            for i in range(target - num):
                for comb in dp[i]:
                    dp[i + num].append(comb + [num])

        return dp[-1]
