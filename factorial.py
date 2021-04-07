def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

factorialOf = int(input("Enter the number which you seek to find it factorial \n"))
print("Factorial of %s :" % factorialOf,fact(factorialOf))
