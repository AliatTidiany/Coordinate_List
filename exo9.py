#ch="Ce beau pays Un pays que je veux remttre sur pied"
#remplacer ds cette chaine: question A
#ch1=ch.replace("je veux", "Assim veut")
##Mettre la chaine de caractere en liste: question B
#liste_mots=ch.split()
#print(liste_mots)
##deuxieme mehode à faire à la maison
##C.
#A partir de liste_mots:
#- créer un dictionnaire qui contiendra:
#- comme clés, chaque mot,
#- comme valeurs, le nombre d'occurence de chaque mot
#Vous proposerez deux manières de faire.
dict_mots={}
#for i in liste_mots:
 #   if i not in dict_mots.keys():
  #      dict_mots[i]=1
   # else:
    #    dict_mots[i] +=1
#print(dict_mots)
###Avec la boucle while 
#i=0
#while i<=len(liste_mots):
 #   if i not in dict_mots.keys():
  #      dict_mots[i]=1
   # else:
    #    dict_mots[i] +=1
#print(dict_mots)


####Faites, A, B, et C à l'aide de fonctions dont vous définirez:
#- paramètres
#- valeurs retournées
### -A
def A(ch):
    
    ch1=ch.replace("je veux", "ALIOUNE veut")
    return (ch1)
#print (A("je veux manger"))

### -B

def B (ch):
    liste_mots= ch.split()
    return (liste_mots)
print (B("FB Barcelona le plus grand club du monde"))



