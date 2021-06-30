import math
import random
from pprint import pprint
import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from cffi.backend_ctypes import xrange
from pymongo import MongoClient
import itertools

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
graph1 = [[0 for i in range(n)] for j in range(n)]
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




    return graph


def create_complete_graph(graph):

    for i in range(n):
        for j in range(n):
            if(j!=i):
                graph[i][j] = 1
                val = calculate_distance(point[i][0],point[j][0],point[i][1],point[j][1])
                graph1[i][j] = val


    return graph





pprint((Draw_graph(create_complete_graph(graph))))
# print(point)
pprint(graph)
pprint(graph1)
#save_to_mongo(n,graph)





def generate_solution():
        sommets = [i for i in range(n)]
        solution = []
        for i in range(len(graph)):
             s = sommets[random.randrange(0, len(sommets))]
             solution.append(s)
             sommets.remove(s)
        print("solution",solution)
        return solution







def calculate_distance_solution(solution):
    distance =0
    counter = 0
    for i in solution :
        if(counter <= n-2):
             # print("silutin next",solution[counter+1])
             # print("here diii",graph1[i][solution[counter+1]])
             distance = distance + graph1[i][solution[counter+1]]
             # print("dis here",distance)
             counter += 1

    return distance





def voisinage(solution):

            voisins = []
            for i in range(len(solution)-1):
                for j in range(i+1,len(solution)):
                    voisin = solution.copy()
                    voisin[i] = solution[j]
                    voisin[j]=solution[i]
                    voisins.append(voisin)
            print("len of voisisn",len(voisin))
            return voisins












def best_solution_distance(list):
    distance_list = []

    best_solution = 0
    best_sol_cycle = []
    best_sol_cycle_dict = dict()
    for k in list:
        distance = calculate_distance_solution(k)
        distance_list.append(distance)
        if(best_solution ==0):
            best_solution = distance
        if(distance < best_solution):
            best_solution = distance
            if(len(best_sol_cycle)>0):
             del best_sol_cycle[-1]
             del list[-1]

            best_sol_cycle.append(k)
    print("Meileur solution local & cycle",best_solution,best_sol_cycle)
    return best_sol_cycle,best_solution



def generate_lot_of_solution(iterations):
    list_of_voisins = []
    solution_courant = 0
    distance = 0
    best_solution = 0
    list_object = []
    for m in range(n):
        object = random.randint(0,n-1)
        collect_position = random.randint(0,n-1)
        list_object.append({"object_id" : object,"collect_position":collect_position})
    tabou_list = []
    for i in range(iterations):

        sommets = [i for i in range(n)]
        solution = []
        for i in range(n):
            s = sommets[random.randrange(0, len(sommets))]
            solution.append(s)
            sommets.remove(s)
        print("solution s", solution)
        if (len(tabou_list) == 0):
            tabou_list.append(solution)
        if (solution not in tabou_list):
            print("not in")
            tabou_list.append(solution)
            list_of_voisins = voisinage(solution)
            solution_courant, distance1 = best_solution_distance(list_of_voisins)
            if (distance == 0):
                print("distancec1", distance1)
                distance = distance1

            if (distance1 < distance):
                best_solution = solution_courant
                distance = distance1



        else:
            if(i>0):
                 i -=1
            continue

        # solution = generate_solution()



    print("bes solution",distance)
    print("list_object",list_object)
    print("tabou_list",len(tabou_list),tabou_list)
    return best_solution,distance





best_solution,distance = generate_lot_of_solution(1000)
print("Meilleurs solution global & distance in all iteration",best_solution,distance)





# a = [a for a in itertools.permutations([0,1,2,3,4,5])]
# print(len(a))
