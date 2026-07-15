def greedy_knapsack(X,V,W,M):
    n=len(X)
    items = []
    for i in range(n):
        ratio = V[i]/W[i]
        items.append((ratio,X[i],V[i],W[i]))
    items.sort(reverse=True)
    s=[]
    sw=0
    sp=0
    i=0
    while i<n:
        ratio,x,p,w=items[i]
        if sw+w <= M:
            s.append(x)
            sw += w
            sp+=p
        else:
            frac = (M- sw) / w 
            s.append((x,frac))
            sw += w*frac
            sp += p*frac
            break
        i=i+1
    return s,sw,sp



X=['X1','X2','X3','X4','X5','X6','X7']
V=[9,5,2,7,6,16,3]
W=[2,5,6,11,1,9,1]
M=28
s,sw,sp=greedy_knapsack(X,V,W,M)
print("Selected Items (S):", s)
print("Total Weight (SW):", sw)
print("Total Profit (SP):", sp)


