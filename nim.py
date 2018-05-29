#Récupration des données depuis le fichier "tas" et "joueur":
from tas import *
from joueur import *


#Récuperer les scores:
scores = recup_scores()



# Récuperation le nom des deux joueurs:
joueur1 = recup_nom_joueur1()
joueur2 = recup_nom_joueur1()



# Si les joueurs n'ont pas encore de score, on les ajoute:
if joueur1 not in scores.keys():
    scores[joueur1] = 0 
elif joueur2 not in scores.keys():
    scores[joueur2] = 0 



#Début du jeu:
print("\n\n")
l3=[ '*','*','*']
l4=[ '*','*','*','*']
l5=[ '*','*','*','*','*']
l6=[ '*','*','*','*','*','*']
l7=[ '*','*','*','*','*','*','*']
print("Voilà les piéres et les tas:")
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
nb_coup1=0
nb_coup2=0
somme_piere=0
continuer_partie ='o'
while continuer_partie !='n':

	print("\n\n")
	print("Le tour du 1er joueur: \n \n")
	num_tas=int(input("Donnez SVP un tas ENTRE 3 et 7: \n"))
	piere=int(input("Donnnez nbr de piere a retirer qui soit possible SVP\n"))
	
	if num_tas==3:
		l3=l3[piere:]
	if num_tas==4:
		l4=l4[piere:]
	if num_tas==5:
		l5=l5[piere:]
	if num_tas==6:
		l6=l6[piere:]
	if num_tas==7:
		l7=l7[piere:]
	print(l3)
	print(l4)
	print(l5)
	print(l6)
	print(l7)

	somme_piere=somme_piere+piere
	nb_coup1 = nb_coup1+1
	scores[joueur1] = scores[joueur1] + nb_coup1*10**nb_coup1
	print("Scores du 1er joueur est:")
	print(scores[joueur1])
	if somme_piere==24:
		print("joueur 1 a ganger")
		continuer_partie='n'
	else:

		print("\n\n")
		print("Le tour du 2eme joueur: \n \n")
		num_tas=int(input("Donnez SVP un tas ENTRE 3 et 7: \n"))
		piere=int(input("Donnnez nbr de piere a retirer qui soit possible SVP\n"))
		if num_tas==3:
			l3=l3[piere:]
		if num_tas==4:
			l4=l4[piere:]
		if num_tas==5:
			l5=l5[piere:]
		if num_tas==6:
			l6=l6[piere:]
		if num_tas==7:
			l7=l7[piere:]
		print(l3)
		print(l4)
		print(l5)
		print(l6)
		print(l7)

		somme_piere=somme_piere+piere
		nb_coup2 = nb_coup2+1
		scores[joueur2] = scores[joueur2] + nb_coup2*(10**nb_coup2)
		print("Scores du 2eme joueur est:")
		print(scores[joueur2])
	
		print("\n\n")
		
		
		if somme_piere==24:
			print("joueur 2 a ganger")
			continuer_partie='n'

	

# La partie est finie, on enregistre les scores
enregistrer_scores(scores)

#Affichage des scores:

print("1er joueur: Vous finissez la partie avec :\n")
print(scores[joueur1])
print("\n\n")
print("2eme joueur: Vous finissez la partie avec:\n")
print(scores[joueur2])
