import math
import random
from pprint import pprint

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



n= 6
degreMax = n - 1
degreMin = math.ceil(n / 2)

graph = [[0 for i in range(n)] for j in range(n)]
point = generate_vertex(n)

def calculate_distance(x1,x2,y1,y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),4)


def checksuper_than_0(list):
    counter = 0
    for i in list:
        if i > 0 :
            counter = counter + 1
    return counter


def Draw_graph(graph):
    x = list()
    y = list()
    for i in point:
        x.append(i[0])
        y.append(i[1])
    # print("yanis ", x, y)
    # plt.plot(x,y,"ro")
    # for i in range(n):
    #     for j in range(n):
    #         if(graph[i][j]!=0):
    #             plt.plot([x[i],x[j]],[y[i],y[j]])
    # plt.show()

    G = nx.from_numpy_matrix(np.array(graph))
    nx.draw(G, with_labels=True)
    plt.show()








def save_to_mongo(n,graph):
    sommet = dict()
    new_db = client["Data_analysis"]


    for i in  range(n):
        object = dict()
        for z in range(n):
            if z == i:
                continue
            # print(graph[i][z])
            object["city" + str(i) + " => " + "city"+str(z)] =  {"distance" : graph[i][z], "x":point[z][0],"y":point[z][1] }

        sommet[str("city" + str(i))] = object



    # print("sommet",sommet)
    new_db["Data_analysis"].insert_one(sommet)

    return



def Create_graph(n):
    for x in range(n):
        degre = random.randint(degreMin, degreMax)
        degr_parcour = degre
        degr_parcour = degr_parcour - sum(graph[x])
        for y1 in range(n):
                        if (degr_parcour > 0 ):

                            if (x != y1):
                             graph[x][y1] = 1
                             graph[y1][x] = 1
                             degr_parcour = degr_parcour - 1


    return graph


pprint((Draw_graph(Create_graph(n))))
print(point)
pprint(graph)
save_to_mongo(n,graph)




