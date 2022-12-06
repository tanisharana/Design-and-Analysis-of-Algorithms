INF = 9999999
N = 5
G = [[0, 8, 16, 0, 0],
     [8, 0, 16, 9, 4],
     [16, 16, 0, 7, 6],
     [0, 9, 7, 0, 7],
     [0, 4, 6, 7, 0]]

curr_node = [0, 0, 0, 0, 0]

without_edge = 0

curr_node[0] = True
print("\nEdge : Weight\n")
while (without_edge < N - 1):
    
    min = INF
    a = 0
    b = 0
    for m in range(N):
        if curr_node[m]:
            for n in range(N):
                if ((not curr_node[n]) and G[m][n]):  
                    if min > G[m][n]:
                        min = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    curr_node[b] = True
    without_edge += 1
