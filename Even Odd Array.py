'''
Write a program to get N, the size of the array in first line of input. Then get N elements from user as input.

Rearrange the elements of the array such that all even elements comes in the front of the array and then all the odd elements after it.

Input
5
10 20 35 40 15

Output
10 20 40 35 15
'''

n=int(input())

arr=list(map(int,input().split()))

evenodd=[]


for item in arr:
    if item %2==0:
        evenodd.append(item)
        
for item in arr:
    if item %2!=0:
        evenodd.append(item)

        
for num in evenodd:
    print(num, end=" ")
