import datetime

boite= 0
boite_max= int(input ("Saisir argent max : "))

date= [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
date_max= input ("Saisir date max (AAAA-MM-JJ) : ")
date_max= [int(part) for part in date_max.split("-")]

tps_test= True
while tps_test:
    tps_restant= [date_max[0] - date[0], date_max[1] - date[1], date_max[2] - date[2]]
    print (f"V1: {tps_restant}")
    if tps_restant[2]< 0:
        tps_restant[1]-= 1
        tps_restant[2]+= 31
    elif tps_restant[1]< 0:
        tps_restant[0]-= 1
        tps_restant[1]+= 12
    if tps_restant[0]< 0:
        print ("date incorrect !")
        date_max= input ("Saisir date max (AAAA-MM-JJ) : ")
        date_max= [int(part) for part in date_max.split("-")]
    else:
        break
print (f"V2: {tps_restant}")