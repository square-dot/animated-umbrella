t = int(input())

def degree(link, h, l):
    p = [x[0] for x in link]
    p.sort(reverse=True)
    v_1 = 0
    for i, val in enumerate(p):
        v_1 += val * (h+1)**(l - i)
    return v_1

    
for s in range(t):
    nr_m = int(input())
    fun_factors = list(map(int, input().split()))
    pointers = list(map(int, input().split()))
    links = list(zip(fun_factors, list(range(1, nr_m + 1))))
    h = max(fun_factors)
    initiators = [x for x in links if x[1] not in pointers]

    mm = min(initiators, key=lambda x: degree(x, h, nr_m))
    