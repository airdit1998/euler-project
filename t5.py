# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 2520
a = []
while len(a) != 17:
    a = []
    i += 10
    print(i)
    for k in range(3, 20):
        if i % k == 0:
            a.append(k)
print(i)  # 232792560
