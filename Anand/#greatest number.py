#greatest number

n1=int(input("please give first number n1:"))
n2=int(input("please give second numbern2:"))
n3=int(input("please give third numbern3:"))
if n1>=n2 and n1>=n3:
    print("n1 is greatest")
    if n2>n1 and n2>=n3:
            print("n2 is greatest")
            if n3>=n1 and n3>=n2:
                print("n3 is greatest")