'''

Given a string s, return the longest palindromic
substring in s.

---

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

---

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

class Solution:
	def longestPalindrome(self, s: str) -> str:
		if len(s) == 1:
			return s

		def expand_from_center(left, right):
			while left >= 0 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			return s[left + 1:right]

		longest = ""
		for i in range(len(s) -1):
			odds = expand_from_center(i,i)
			evens = expand_from_center(i, i+1)

			if len(odds) > len(longest):
				longest = odds
			if len(evens) > len(longest):
				longest = evens

		return longest