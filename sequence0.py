from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client['Prosit-db']
collection_trafic = db['Prosit']

# new_db = client["vehicules_stamped"]


def convert(hours, minuts):


        minuts = minuts - 60
        hours = hours + 1

        if (minuts > 59):
            convert(hours, minuts)
        else:
            print(minuts,hours)
            return minuts,hours



def insert(db,num_arete,num_jour,plage_horaire,num_periode,nb_vehicules,date):
    mydict = {"num_arete":num_arete , "num_jour": num_jour,"plage_horaire":plage_horaire,
              "num_periode":num_periode,"nb_vehicules":nb_vehicules,"date":date}


    return db["véhicules_stamped"].insert_one(mydict)
for x in db['Prosit'].find():

    date_number =1
    if int(x["num_jour"]) == 0:
        date_number = 1
    elif int(x["num_jour"]) == 1:
        date_number = 2
    elif int(x["num_jour"]) == 2:
        date_number = 3
    elif int(x["num_jour"]) == 3:
        date_number = 4
    elif int(x["num_jour"]) == 4:
        date_number = 5
    minuts = int(x["num_periode"])
    print("minuts = ", minuts)
    if x["plage_horaire"] == "m":
        hours = 7
        if minuts > 59:
            data = convert(7,minuts)

            hours = 7 + 1
            minuts = 0
            date = datetime.datetime(2020, 1, int(date_number), data[1], data[0])
            print(date)
            insert(collection_trafic,x["num_arete"],x["num_jour"],x["plage_horaire"],x["num_periode"],x["nb_vehicules"],date)
            continue
        date = datetime.datetime(2020, 1, int(date_number) , hours, int(x["num_periode"]))
        insert(collection_trafic, x["num_arete"], x["num_jour"], x["plage_horaire"], x["num_periode"],
               x["nb_vehicules"],  date.strftime('%Y:%M:%D:%H:%M'))



    else:
        hours = 17
        if minuts > 59:
            minuts,hours = convert(17,minuts)

            date = datetime.datetime(2020, 1, int(date_number), data[1], data[0])
            print(date)

            insert(collection_trafic,x["num_arete"],x["num_jour"],x["plage_horaire"],x["num_periode"],x["nb_vehicules"],date)

            continue
        date = datetime.datetime(2020, 1, int(date_number) , hours, int(x["num_periode"]))
        insert(collection_trafic, x["num_arete"], x["num_jour"], x["plage_horaire"], x["num_periode"],
               x["nb_vehicules"], date.strftime('%Y:%M:%D:%H:%M'))






