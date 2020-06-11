"""
// Time Complexity : O(NK)
// Space Complexity : O(NK)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        Method1 - DP Tabulation with Number of eggs as rows and Number of floors as columns
        Idea is to figure out the minimum possible floors required to be certain about non breakage of the eggs-> So essentially we are minimizing the maximization of the all possible floors for K number of eggs
        Algo
        - Initial configuration dp[K+1][N+1]
        - For j = 1 to dp[0].length
            Fill the entire row considering 1 egg with values for min number of ways for n floors
        - For i = 1 to dp.length
            for j = 1 to dp[0].length # considering all the floors
                dp[i][j] = inf
                for l = 1 to j #considering K number of eggs for all floors uptill j
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][l-1],dp[i][j-l]) )
                    #maximum of ((dropping the egg,remaining floor left for dropping the remaining eggs),(not dropping the egg, remaining floor left to be considered for dropping))
        - Return dp[K][N]
        """
        
#         dp = [[0 for _ in range(N+1)]for _ in range(K+1)]
        
#         for j in range(1,len(dp[0])):
#             dp[1][j] = j
        
#         for i in range(2,len(dp)):
#             for j in range(1,len(dp[0])):
#                 dp[i][j] = float("inf")
#                 for l in range(1,j+1):
#                     dp[i][j] = min(dp[i][j] , 1 + max(dp[i-1][l-1],dp[i][j-l]))
#         return dp[K][N]
    
        """
        Method - Crazy DP Optimal solution
        Idea is to estimate the minimum number of attempts after which the egg dropped from the floor exceeds N
        
        Algo
        - Initial confi - attmepts = 0 , dp = [K+1][N+1], i = 1
        - Iterate while dp[attempts][i] < N
            attempts +=1
            for i = 1 to K
                #count the number of possible floors using the attempts and possibility to drop the egg or not the egg
                dp[attempts][i] = 1 + dp[i-1][K-1] + dp[i][K]
        - return attempts
        """
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        attempts = 0
        i = 1
        while dp[attempts][i] < N:
            attempts +=1
            for i in range(1,K+1):
                dp[attempts][i] = 1 + dp[attempts-1][i-1] + dp[attempts-1][i]
        
        return attempts