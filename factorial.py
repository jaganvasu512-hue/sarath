def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 4   # input given directly
print(f"Factorial of {num} is {factorial(num)}")
