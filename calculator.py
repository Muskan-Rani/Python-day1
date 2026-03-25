
Num_1 = int(input("Enter First number: "))
Num_2 = int(input("Enter Second number: "))
ops = input("Choose operation (+ , -, *, /): ")

if ops == '+':
    print(Num_1 + Num_2)

elif ops == '-':
    print(Num_1-Num_2)

elif ops == '*':
    print(Num_1 * Num_2)

elif ops == '/':
    if Num_2 != 0:
        print(Num_1 / Num_2)
    else:
        print("Can't divide by zero!")

else:
    print("Invalid operation!")

