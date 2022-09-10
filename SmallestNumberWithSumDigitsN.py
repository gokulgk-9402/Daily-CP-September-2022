#User function Template for python3

class Solution:
	def digitsNum(self, N):
		# Code here
		ans = "0" * N
		if N < 9:
		    return str(N) + ans
		    
		q = N//9
		r = N%9
		
		if r:
		    return str(r) + ("9" * q) + ans
		else:
		    return ("9" * q) + ans