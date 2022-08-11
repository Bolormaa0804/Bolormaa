# Bolormaa Munkhzaya
# CSC 115
# Lab3
# Using function

def read_name():
    name = input("Enter your name: ")
    return name


def read_gross_pay():
    grossPay = float(input("Enter your gross pay: "))
    return grossPay


def read_dependents():
    dependents = int(input("Enter number of dependents: "))
    return dependents


def compute_tax_rate(dependents):
    if dependents >= 4:
        taxRate = 0.1
    elif dependents >= 2:
        taxRate = 0.15
    elif dependents >= 0:
        taxRate = 0.2
    else:
        dependents = int(input("Input is unvalid, negative. Please enter again"))
    return taxRate


def compute_net_pay(grossPay, taxRate):
    tax = grossPay * taxRate
    netPay = grossPay - tax
    return netPay


def main():
    name = read_name()
    grossPay = read_gross_pay()
    dependents = read_dependents()
    taxRate = compute_tax_rate(dependents)
    netPay = compute_net_pay(grossPay, taxRate)
    print("\nName:       ", name)
    print("Gross pay:   $", grossPay)
    print("Dependents: ", dependents)
    print("Tax Rate:   ", taxRate * 100, "%")
    print("NetPay:      $", netPay)


main()
