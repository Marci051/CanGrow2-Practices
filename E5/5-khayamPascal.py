n = int(input())

triangle = []

for i in range(n):

    row = [1]  
    if i > 0:

        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])

        row.append(1)
    triangle.append(row)


for row in triangle:
    print(" ".join(map(str, row)))
