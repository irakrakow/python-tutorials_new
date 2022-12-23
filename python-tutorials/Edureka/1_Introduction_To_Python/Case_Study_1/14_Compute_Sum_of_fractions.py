def compute_sum(n):
    return sum([i / (i + 1) for i in range(1, n + 1)])


num = int(input(("n: ")))  # input returns a string...must convert to int
# compute_sum returns float...need to convert to int to get answer
print(compute_sum(num))  
