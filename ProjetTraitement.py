import math
import random




def generate_vertex(n):
    graph_point = list()
    for _ in range(n):
         x = random.randint(0,190)
         y = random.randint(0,190)
         graph_point.append([x,y])
    return graph_point



n= 20
degreMax = n - 1
degreMin = math.ceil(n / 2)

graph = [[0 for i in range(n)] for j in range(n)]
cctl = generate_vertex(n)


for x in range(n):
        for y1 in range(n):
                    degre = random.randint(degreMin, degreMax)
                    degr_parcour = degre
                    while (degr_parcour > 0):
                        graph[x][y1] = 1
                        degr_parcour = degr_parcour - 1

                        if (sum(graph[y1]) > degre):
                            graph[y1][x] = 0
                    degr_parcour = degre


print(cctl)
print(graph)






















