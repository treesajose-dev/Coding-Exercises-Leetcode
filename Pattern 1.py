"""
Print the pattern
       A
     B A B
   C B A B C
 D C B A B C D
 
 """
 
 
n=int(input("Enter the n value: "))

for i in range(1,n+1):
    ascii_val=64+i
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("%c"%ascii_val,end=" ")
        if j<i:
            ascii_val-=1
        else:
            ascii_val+=1
        
    print()
