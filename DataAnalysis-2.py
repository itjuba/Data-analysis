import math
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Prosit-db']
collection_trafic = db['Data_analysis']

def generate_vertex(n):
    graph_point = list()
    for _ in range(n):
         x = random.randint(0,190)
         y = random.randint(0,190)
         graph_point.append([x,y])
    return graph_point



n= 10
degreMax = n - 1
degreMin = math.ceil(n / 2)

graph = [[0 for i in range(n)] for j in range(n)]
point = generate_vertex(n)

def calculate_distance(x1,x2,y1,y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),4)

print(point)

def checksuper_than_0(list):
    counter = 0
    for i in list:
        if i > 0 :
            counter = counter + 1
    return counter


def Draw_graph(graph):
    G = nx.from_numpy_matrix(np.matrix(graph), create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout)
    nx.draw_networkx_edge_labels(G, pos=layout)
    plt.show()




def save_to_mongo(n,graph):
    sommet = dict()
    new_db = client["Data_analysis"]


    for i in  range(n):
        object = dict()
        for z in range(n):
            print(graph[i][z])
            object["city" + str(z)] =  {"distance" : graph[i][z], "x":point[z][0],"y":point[z][1] }

        sommet[str("city" + str(i))] = object



    print("sommet",sommet)
    new_db["Data_analysis"].insert_one(sommet)

    return




for x in range(n):
        for y1 in range(n):
                    degre = random.randint(degreMin, degreMax)
                    degr_parcour = degre

                    while (degr_parcour > 0 ):

                        if (x != y1):
                         graph[x][y1] = calculate_distance(point[x][0],point[y1][0],point[x][1],point[y1][1])
                         # graph[x][y1] = 1

                        else :
                            graph[x][y1] = 0
                        degr_parcour = degr_parcour - 1

                        if (checksuper_than_0(graph[y1]) > degre ):
                            graph[y1][x] = 0
                    degr_parcour = degre


Draw_graph(graph)


#save_to_mongo(n,graph)
print(point)
print(graph)




