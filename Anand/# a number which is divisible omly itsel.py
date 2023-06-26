# a number which is divisible omly itself is called prime number
# 0&1 is not a prime number

num=int(input("entr a number"))
if num>0:
    for i in range(2,num):
      if (num%i==0):
          print("is a prime number")
          break
      else:
          print("not  a prime numbewr")
          