'''
Self powers
   
Problem 48

	The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
	Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

NUM_MAX = 1000
sum = 0

for i in range(1, NUM_MAX):
	sum += pow(i, i)
	
sum = str(sum)
print(sum[-10:]) # 9110846700