
def countsteps(n):
    s = 1
    while n > 1:
        s += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    return s

nput = input()

values = nput.split()

sol = 0

for n in range(int(values[0]), int(values[1]) + 1):
    cnt = countsteps(n)
    if sol <= cnt: 
        sol = cnt

print(values[0], values[1], sol, sep=' ')
