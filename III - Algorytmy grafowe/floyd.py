def floyd(wagi):
    V = len(wagi)
    dyst = wagi
    for k in range(V):
        nast_dyst = [list(r) for r in dyst]
        for i in range(V):
            for j in range(V):
                nast_dyst[i][j] = min(
                    dyst[i][j], dyst[i][k] + dyst[k][j]
                )
        dyst = nast_dyst
    return dyst


inf = 1e10
graf = [
        [0, inf, inf, -3],
        [inf, 0, inf, 8], 
        [inf, 4, 0, -2],
        [5, inf, 3, 0]
       ]

print(floyd(graf))
 