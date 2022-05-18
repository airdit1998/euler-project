import time

a = time.time()
ex_list = []
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        pol = str(a * b)
        if pol == pol[::-1]:
            ex_list.append(int(pol))
print(max(ex_list))
