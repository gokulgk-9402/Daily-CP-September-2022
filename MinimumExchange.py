#User function Template for python3

class Solution:
	def MinimumExchange(self, matrix):
		# Code here
		a1 = 0
		a2 = 0
		rows = len(matrix)
		cols = len(matrix[0])
		
		for i in range(rows):
		    for j in range(cols):
		        if (i % 2 == 0 and j % 2 == 0) or (i%2 == 1 and j % 2 == 1):
		            if matrix[i][j] == 'A':
		                a1 += 1
		        else:
		            if matrix[i][j] == 'B':
		                a1 += 1
		                
		        if (i % 2 == 0 and j % 2 == 0) or (i%2 == 1 and j % 2 == 1):
		            if matrix[i][j] == 'B':
		                a2 += 1
		        else:
		            if matrix[i][j] == 'A':
		                a2 += 1
		                
	    return min(a1, a2)