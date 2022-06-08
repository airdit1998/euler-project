# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_the_squares():
    i = 0
    summa = 0
    while i < 100:
        i += 1
        summa += i ** 2
    return summa


def square_of_the_sum():
    i = 0
    summa = 0
    while i < 100:
        i += 1
        summa += i
    return summa ** 2


print(square_of_the_sum() - sum_of_the_squares())  # 25164150
