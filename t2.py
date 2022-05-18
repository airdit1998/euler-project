# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# \find the sum of the even-valued terms.

def find_even_fib():
    s = 0
    last = 0
    next = 1

    while last <= 4000000:
        last, next = next, last + next
        if last % 2 == 0:
            s += last
    return s

print(find_even_fib())




