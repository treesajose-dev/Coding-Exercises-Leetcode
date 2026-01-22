'''
Write a program to check if the given password is strong. Return 1 if the password is strong and 0 if the password is weak.

A strong password is one which satisfies the following conditions:

It contains a mix of capital letters, small letters and digits.
It contains minimum 8 characters.
It contains atleast one non alphanumeric character.
It should not contain any space.
Example:

Input:
myname123

Output:
0

Input:
Myname123$

Output:
1

'''


def function(text):
    hasUpper=0
    hasLower=0
    hasDigit=0
    hasSpecial=0
    count=0
    
    for s in text:
        if(s == ' '):
            return 0
        elif(s>='0' and s<='9'):
            hasDigit=1
        elif(s>='A' and s<='Z'):
            hasUpper=1
        elif(s>='a' and s<='z'):
            hasLower=1
        else:
            hasSpecial=1
        count=count+1
        
            
    if hasDigit==1 and hasUpper==1 and hasLower==1 and hasSpecial==1 and count>8 :
        return 1
    else:
        return 0
        


text = input()
out = function(text)
print(out)
