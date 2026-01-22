'''
Given an array of 1's and 0's. Return a positive number if the count of 1's are more than the count of 0's, 
return a negative number if the number of 1's are less than the number of 0's and return 0 if their counts are same. 
The first input is the number of elements of the binary array followed by the binary array.


INPUT                OUTPUT
7 1 0 1 0 1 1 0        1
4 0 1 0 0	            -1
'''

a=list(map(int,input().split()))

n=a[0]
ones=0
zeroes=0

for i in range(1,n+1):
    if(a[i]==1):
        ones+=1
    else:
        zeroes+=1
    
if(ones>zeroes):
    print(1)
elif(ones<zeroes):
    print(-1)
else:
    print(0)
