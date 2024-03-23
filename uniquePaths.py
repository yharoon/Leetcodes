'''

There is a robot on an m x n grid. 
The robot is initially located at the 
top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The 
robot can only move either down or right 
at any point in time.

Given the two integers m and n, return 
the number of possible unique paths that 
the robot can take to reach the bottom-right 
corner.

The test cases are generated so that the 
answer will be less than or equal to 2 * 109.

---

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3

---

Constraints:

    1 <= m, n <= 100

'''

class Solution:
	def uniquePaths(self, m: int, n: int) -> int:

		dp = [[0 for i in range(m+1)] for j in range(n+1)]

		def solve(rows: int, cols: int):

			if (rows == 1) or (cols == 1):
				dp[rows][cols] = 1
				return 1

			if (dp[rows][cols] == 0):
				dp[rows][cols] = solve(rows-1, cols) + solve(rows, cols-1)

			return dp[rows][cols]

		return solve(n,m)