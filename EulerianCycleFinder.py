from pathfinding import finder

matrixZoneA = [
    [0,1,0,0,0,0,0,0,0,1,0],
    [1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,1,0],
    [0,0,1,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,1,0,0,0],
    [0,0,1,0,0,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,1,0],
    [1,0,1,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,1,0],
]

def cycleEulerien(matrice):
    n = len(matrice)

    cycle = list()
    stack = list()
    cur = 0


    while (stack != [] or sum(matrice[cur]) != 0):
            print("sum here",sum(matrice[0]))
            print(matrice[0])
            if (sum(matrice[cur]) == 0):
                cycle.append(cur+1)
                cur = stack[-1]
                del stack[-1]



            else:
                for i in range(n):
                    if (matrice[cur][i] == 1):
                        stack.append(cur)
                        matrice[cur][i] = 0
                        matrice[i][cur] = 0
                        cur = i
                        break
    for ele in cycle:
        print(ele, end=" -> ")



cycleEulerien(matrixZoneA)


