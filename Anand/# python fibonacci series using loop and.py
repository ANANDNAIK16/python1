# python fibonacci series using loop and recurstion
nNum=10

num=num
num1=0
num2=1
count=0
while(count<nNum):
    print(num1)
    num=num1+num2
    num1=num2
    num2=num
    count+1
    nterms=10
    if nterms<=0:
        (print("enter a positive integer"))
    else:
        print("fibonacci sequence:")
        for i in range(nterms):
            print("recue_fibo(i)")
            def recur_fibo(n):
                if n<=1:
                    return n
                else:
                    return(recur_fibo(n-1))+recur_fibo(n-2)
                
        