#python program to check number is palindram or not
#palindram eg :dad,mom,madam,121,1120211
num=int(input("enter a number"))
temp=num
rev=0
while num>0:
    remain=0%10
    rev=(rev*10+remain)
    num=num//10
    if temp==rev:
        print("number is a palindram")
    else:
        print("number  not a palindram")
    
