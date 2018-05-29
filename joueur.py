import os
import pickle

#Récupration des données depuis le fichier "tas" :
from random import choice
from tas import *



 #Une fonction qui récupére les scores des deux joueurs:
def recup_scores():

    
    if os.path.exists(nom_fichier_scores): 
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: 
        scores = {}
    return scores




# La fonction qui enregistre les scores dans un fichier text scores:
def enregistrer_scores(scores):
  

    fichier_scores = open(nom_fichier_scores, "wb") 
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()





# La fonction qui enregistre les noms des deux joueures:
def recup_nom_joueur1():
	nom_joueur1 = input("Tapez votre nom:\n ")
	nom_joueur1 = nom_joueur1.capitalize()
	#return recup_nom_joueur1()
    

