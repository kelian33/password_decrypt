import time 
import hashlib

tmps1=time.time()

def hashmd5(chaine):
    m = hashlib.md5()
    m.update(chaine.encode('utf-8'))
    hash = m.hexdigest()
    return hash

fichier = open("dico_mini_fr", "r")
password = open("password", "a")

dico = fichier.readlines()

for ligne in dico:
    ligne=ligne[:-1]
    hash = hashmd5(ligne)
    if hash == '934b4a210c17493f68bf6bfe74bff77a':
        print('Mot de passe trouvé !!')
        print(hash)
        print(ligne)
        break;

tmps2=time.time()-tmps1
print("Temps d'exécution = %f secondes" %tmps2)

password.write("Attaque par dictionnaire \n")
password.write(hash + "\n")
password.write(ligne + "\n")
password.write("Temps d'exé
cution = %f secondes \n ---------- \n" %tmps2)

password.close()
fichier.close()