while True:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the first number: "))
    op = input("Enter the operator as +,-,/ or *: ")
    if op in ['+', '-', '*', '/']:
        if op == '+':
            print(f"{n1} + {n2} =", n1+n2)
        elif op == '-':
            print(f"{n1} - {n2} =", n1-n2) 
        elif op == '*':
            print(f"{n1} * {n2} =", n1*n2)
        elif op == '/':
            print(f"{n1} / {n2} =", n1/n2)
    else:
        print("Invalid symbol")
        #print("Enter the correct operator i.e +,-,*,/")
