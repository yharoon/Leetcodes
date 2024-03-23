'''

A message containing letters from A-Z can be encoded 
into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be 
grouped then mapped back into letters using the 
reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because 
"06" cannot be mapped into 'F' since "6" is different 
from "06".

Given a string s containing only digits, return the 
number of ways to decode it.

The test cases are generated so that the answer fits 
in a 32-bit integer.

---

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) 
or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), 
"VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the 
leading zero ("6" is different from "06").

---

Constraints:

    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).

'''

class Solution:
	def numDecodings(self, s: str) -> int:
		memo = set()

		mapping  = {
		"1":"a",
		"2":"b",
		"3":"c",
		"4":"d",
		"5":"e",
		"6":"f",
		"7":"g",
		"8":"h",
		"9":"i",
		"10":"j",
		"11":"k",
		"12":"l",
		"13":"m",
		"14":"n",
		"15":"o",
		"16":"p",
		"17":"q",
		"18":"r",
		"19":"s",
		"20":"t",
		"21":"u",
		"22":"v",
		"23":"w",
		"24":"x",
		"25":"y",
		"26":"z"
		}

		def dfs(string, path):
			if len(string) == 0:
				memo.add(path)
				return
			if string[0] == "0":
				return
			dfs(string[1:], path+mapping[string[0]])
			if len(string) > 1:
				if int(string[:2]) < 27:
					dfs(string[2:], path+mapping[string[:2]])
				if string[1] == "0":
					return
				dfs(string[2:], path+mapping[string[0]]+mapping[string[1]])
		
		dfs(s,"")
		print(memo)
		return len(memo)

---

class Solution:
	def numDecodings(self, s: str) -> int:
		if not s or s[0] == "0":
			return 0

		n = len(s)
		dp = [1] + [1] + ([0] * (n-1))

		for i in range(2, n+1):
			ones = int(s[i-1])
			twos = int(s[i-2:i])

			if ones != 0:
				dp[i] += dp[i-1]
			if 9 < twos < 27:
				dp[i] += dp[i-2]

		return dp[n]