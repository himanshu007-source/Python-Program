a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=input("choose operator(+,-,*,/): ")
if c=="+":
    print(a,"+",b,"=",a+b)
elif c=="-":
    print(a,"-",b,"=",a-b)
elif c=="*":
    print(a,"*",b,"=",a*b)
elif c=="/":
    print(a,"/",b,"=",a/b)
else:
    print("Invaild operator")