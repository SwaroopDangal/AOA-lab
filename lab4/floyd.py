def Floyd_Warshall(W,n):
    D=[]
    for i in range(n+1):

        row = []
        for j in range(n+1):
            row.append(W[i][j])
        D.append(row)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if D[i][j]> D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D



INF = float('inf')
n=4
W= [[INF,INF,INF,INF,INF],
    [INF,0,3,10,INF],
    [INF,INF,0,4,9],
    [INF,INF,INF,0,2],
    [INF,1,8,INF,0],
    ]
distance = Floyd_Warshall(W,n)
for i in range (1,n+1):
    for j in range(1,n+1):
        print(distance[i][j], end="\t")
    print()