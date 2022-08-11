# Bolormaa Munkhzaya
# Susan Furtney
# Assignemnt 3
# 02/20/2022
addCalled = 0
subCalled = 0
mulCalled = 0
divCalled = 0
absCalled = 0


def add(num1, num2):
    total = num1 + num2
    global addCalled
    addCalled += 1
    return total


def sub(num1, num2):
    sub = num1 - num2
    global subCalled
    subCalled += 1
    return sub


def mul(num1, num2):
    mult = num1 * num2
    global mulCalled
    mulCalled += 1
    return mult


def div(num1, num2):
    division = num1 / num2
    global divCalled
    divCalled += 1
    return division


def abso(num):
    if num >= 0:
        ans = num
    else:
        ans = num * (-1)
    global absCalled
    absCalled += 1
    return ans


def quit():
    print("Function usage count")
    print("add function:", addCalled,
          "\nsub function:", subCalled,
          "\nmul function:", mulCalled,
          "\ndiv function:", divCalled,
          "\nabs function:", absCalled)


def main():
    print("Welcome to iCalculator.")
    print("\nUse these keywords to calculate: add, sub, mul, div, abs, and quit")
    print("Example: add 5 6")
    while True:
        problem = input(">")
        tokens = problem.split(" ")
        operator = tokens[0]
        if operator == 'abs':
            num = float(tokens[1])

        elif operator != 'quit':
            num1 = float(tokens[1])
            num2 = float(tokens[2])
        else:
            num1 = 0
        if operator == 'add':
            ans = add(num1, num2)

        elif operator == 'sub':
            ans = sub(num1, num2)

        elif operator == 'mul':
            ans = mul(num1, num2)

        elif operator == 'div':
            if num2 == 0:
                num2 = float(input("Invalid! Denominator should not be zero please enter different denominator: "))
            else:
                num2 = num2
            ans = div(num1, num2)

        elif operator == 'quit':
            quit()
            break
        elif operator == 'abs':
            ans = abso(num)
        else:
            operator = input("Please enter valid operator: ")
        print(ans)


main()

for i in range(3):
    for j in range(3):
        if i != j:
            print("O")
        else:
            print("X")






