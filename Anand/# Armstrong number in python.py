# Armstrong number in python

Example:143=(1*1*1)+(4*4*4)+(3*3*3) 
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+digit**3
    temp//=10
    if sum == num:
        print("is a armstrong number")
    else:
        print("it is not a armstrong number")
