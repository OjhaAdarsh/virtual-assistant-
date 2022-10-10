def NumGen(n):
	
	
	for j in range(0, n+1):

		
		if j % 5 == 0 and j % 7 == 0:
			yield j

# Driver code
if __name__ == "__main__":
	
	N=int(input("Enter The Number"))
	

	
	for j in NumGen(N):
		print(j, end = ",")
