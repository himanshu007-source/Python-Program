def add(a,b):
    r=a+b
    print(a, "+", b, "=", r)
def sub(a,b):
    r=a-b
    print(a, "-", b, "=", r)
def mult(a,b):
    r=a*b
    print(a, "*", b, "=", r)
def div(a,b):
    r=a/b
    print(a, "/", b, "=", r)

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    while True:
        print("1. for Add")
        print("2. for Subtract")
        print("3. for Multiply")
        print("4. for Divide")
        print("5. for Exit")

        c=int(input("Choose operator: "))
        if c==1:
            add(a,b)
        elif c==2:
            sub(a,b)
        elif c==3:
            mult(a,b)
        elif c==4:
            div(a,b)
        elif c==5:
            break
        else:
            print("Invalid Choice")

main()