coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
####On veut borner à 7 toutes les ordonnées y de la liste coordinates qui sont supérieures à 7
###Après votre traitement, affichez coordinates, qui devrait contenir :
#i=0
coordinates2=[]

#while i<len(coordinates):
 #   point=coordinates[i]
  #  y=point[1]
   # x=point[0]
    #if y>7:
     #   nouveau_point=(x,7)
    
    #else:
     #   nouveau_point=(x,y)
    #coordinates2.append(nouveau_point)
    #i=i+1
#print(coordinates2)
#avec la boucle for
for i in coordinates:
    y=i[1]
    x=i[0]
    if y>7:
        nouveau_point=(x,7)
    
    else:
        nouveau_point=(x,y)
    coordinates2.append(nouveau_point)
print(coordinates2)




ordinates = []
##Affichage des ordonnées de notre tuple
#for i in coordinates:
    #print (i[1])
   # ordinates.append(i[1])
#print(ordinates) 
#dict_coordinates={}
#for i in coordinates:
    #keys=i[0]
    #values=i[1]
    #dict_coordinates[values]=keys
#print(dict_coordinates)
##Avec la boucle while
#i=0
#tple=[]
#while i<len(coordinates):
   # tple=coordinates[i]
    #key=tple[0]
    #value=tple[1]
    #dict_coordinates[key]=value
    #i=i+1
#print(dict_coordinates)






