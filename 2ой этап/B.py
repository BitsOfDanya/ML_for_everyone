import numpy as np

def create_equation_system(first_matrix, third_matrix, n, m):
    size = n - m + 1
    A = np.zeros((m*m, size*size))
    b = np.zeros(m*m)

    for i in range(m):
        for j in range(m):
            b[i*m + j] = third_matrix[i][j]
            for x in range(size):
                for y in range(size):
                    A[i*m + j, x*size + y] = first_matrix[i + x][j + y]

    return A, b

n, m = map(int, input().split())

first = []
for _ in range(n):
    first.append(list(map(int, input().split())))

third = []
for _ in range(m):
    third.append(list(map(int, input().split())))

first_matrix = np.array(first)
third_matrix = np.array(third)

A, b = create_equation_system(first_matrix, third_matrix, n, m)

x = np.linalg.lstsq(A, b, rcond=None)[0]
x = x.reshape((n-m+1, n-m+1))

for i in range(n-m+1):
    print(*x[i])
