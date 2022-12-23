def generate_array(X, Y):
    array = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        array.append(row)
    return array


# Read input values
print("Enter 2 digits, separated by a space (example: 3 5)")
X, Y = map(int, input().split())
array = generate_array(X, Y)
print(array)
