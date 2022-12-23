def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# compute 8 factorial
result = factorial(8)
print(result)
