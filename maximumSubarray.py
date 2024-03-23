'''

Given an integer array nums, find the subarray
with the largest sum, and return its sum.

---

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

---

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104


'''

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:

		def solve(arr, left, right):
			if left > right:
				return -inf
			mid = (left+right) // 2
			left_sum = 0
			right_sum = 0
			curr_sum = 0

			for i in range(mid-1, left-1, -1):
				curr_sum = curr_sum + arr[i]
				left_sum = max(left_sum, curr_sum)
			curr_sum = 0
			for i in range(mid+1, right+1):
				curr_sum = curr_sum + arr[i]
				right_sum = max(right_sum, curr_sum)
			return max(solve(arr,left,mid-1), solve(arr, mid+1, right), left_sum + arr[mid] + right_sum)

		return solve(nums,0,len(nums)-1)