## Problem Reference 
# Hackerearth: https://www.hackerearth.com/problem/algorithm/lexi-beads-d951567d/
# Lex: https://lex.infosysapps.com/en/viewer/iap/lex_auth_012876413524492288182?collectionId=lex_auth_012862798083506176336&collectionType=Course




n = int(input())
while n:
   n-=1
   k,s=input().split(' ')
   if int(k)>=2:
       print(''.join(sorted(s)))
   else:
       ans=s    
       for i in range(1,len(s)):
           temp=s[i:]+s[0:i]
           if temp<ans:
               ans=temp  
       print(ans)





# Python 3 program to find the new string
# after performing deletions and append
# operation in the string s

# Function to find the new string thus
# formed by removing characters
# def newString(s, k):
	
# 	# new string
# 	X = ""

# 	# Remove characters until
# 	# the string is empty
# 	while (len(s) > 0):
# 		temp = s[0]

# 		# Traverse to find the smallest
# 		# character in the first k characters
# 		i = 1
# 		while(i < k and i < len(s)):
# 			if (s[i] < temp):
# 				temp = s[i]

# 			i += 1
		
# 		# append the smallest character
# 		X = X + temp

# 		# removing the lexicographically
# 		# smallest character from the string
# 		for i in range(k):
# 			if (s[i] == temp):
# 				s = s[0:i] + s[i + 1:]
# 				break
		
# 	return X

# # Driver Code
# if __name__ == '__main__':
# 	s = "gaurang"
# 	k = 3
# 	print(newString(s, k))

# # This code is contributed by
# # Shashank_Sharma
