import math
n = 100
def sum_of_square(n):
    return((n*(n+1)*(2*n+1))/6)
def square_sum(n):
    return((n*(n+1))**2)/4
print(int(square_sum(n)-sum_of_square(n)))