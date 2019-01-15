#IMPORTATION DES LIBRARIES
import hashlib
import time 

tmps1=time.time()

#fichier = open("shadow", "r")
data = open("combinaisons", "w")
password = open("password", "a")


#empruntes = fichier.readlines()
#fichier.close()

liste = 'barzcdefghijklmno' # Liste de caractères

#FONCTION POUR LES COMBINAISONS
def product(*args, repeat=6):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

#FONCTION HASHAGE MD5
def hashmd5(chaine):
    m = hashlib.md5()
    m.update(chaine.encode('utf-8'))
    hash = m.hexdigest()
    return hash



for item in product(liste) :
    chaine = ''.join(item)   #On transforme la liste en chaine de caractère (ex "a,c,e" en "ace")
    hash = hashmd5(chaine)   #Hashage de la chaine
    data.write(chaine+"\n")  #Ecriture dans le fichier combinaison
    data.write(hash+"\n")    #Ecriture dans le fichier combinaison
    if hash == '6e5fa4d9c48ca921c0a2ce1e64c9ae6f': #On test si la chaine qu'on hash correspond à la chaine hashé que l'on possède
        print('Mot de passe trouvé !!')
        print(hash)
        print(chaine)
        break;

tmps2=time.time()-tmps1
data.write("Temps d'exécution = %f secondes" %tmps2)
print("Temps d'exécution = %f secondes" %tmps2)

password.write("Attaque par force brute \n")
password.write(hash + "\n")
password.write(chaine + "\n")
password.write("Temps d'execution = %f secondes \n ---------- \n" %tmps2)

password.close()
data.close()