import os
import shutil

#importer les fonctions de fichiers.py et dossiers.py
from fichiers import *
from dossiers import *

#Partie du projet pour la gestion de fichiers/dossiers
#Il y a ainsi de multiples fonctions, dont une qui permet de toutes les appeler
    

###################################################################################
#-----------------------------Autres fonctions------------------------------------#
###################################################################################



# fonction pour demander à l'utilisateur le chemin d'un fichier
def demander_chemin_fichier():
    #demande le chemin du fichier et met le resultat dans la variable path
    file_path = input("Quel est le chemin du fichier? ")
    #retourne le chemin du fichier
    return file_path

# fonction pour demander à l'utilisateur le chemin d'un dossier
def demander_chemin_dossier():
    #demande le chemin du dossier et met le resultat dans la variable path
    directory_path = input("Quel est le chemin du dossier? ")
    #retourne le chemin du dossier
    return directory_path

#affichage menu principale: (dossiers, fichier, quitter)
def Affichage_Menu_Principal():
    print("d. Dossier\n"
        "f. Fichier\n"
        "q. Quitter\n")
    
#demander à l'utilisateur s'il veut travailler dans un dossier ou fichier
def Choix_Dossier_Fichier():
    Affichage_Menu_Principal()
    choix_dossier_fichier = input("Quel operation souhaitez vous faire?")
    return choix_dossier_fichier
  
#affiche menu dossier (Si l'utilisateur à fait le choix "d")
def Affichage_Menu_Dossiers():
    print("choisissez votre action\n"
        "  1) Creer un dossier\n"                   #Creation (fait)
        "  2) Copier un dossier\n"                  #Copie
        "  3) Renommer un dossier\n"                #Renommage
        "  4) Supprimer un dossier\n"               #Suppression (fait)
        "  5) Deplacer un dossier\n"                #Deplacement 
        "  6) Verifier l'existence d'un dossier\n"  #Existence
        "  7) Lister les dossiers\n"                #Lister
        "  8) Compresser un dossier\n"              #Zip (compresser)
        "  9) Afficher le contenu d'un dossier\n"   #Afficher contenu
        "  q) quitter la fonction\n")               # quitter le menu  NON REALISER

#affiche menu fichier  (Si l'utilisateur à fait le choix "f")
def Affichage_Menu_Fichiers():
    print("choisissez votre action :\n"
        "  1) Creer un fichier\n"                    #Creation (fait)
        "  2) Copier un fichier\n"                   #Copie  (fait)
        "  3) Renommer un fichier\n"                 #Renommage (fait)
        "  4) Supprimer un fichier\n"                #Suppression (fait)
        "  5) Deplacer un fichier\n"                 #Deplacement (fait)
        "  6) Verifier l'existence d'un fichier\n"   #Existence (fait)
        "  7) Lire un fichier\n"                     #Lecture 
        "  8) Compresser un fichier\n"               #Zip (compresser)
        "  9) Ecrire dans un fichier\n"              #Ecriture
        "  q) quitter la fonction\n")                # quiter le menu NON REALISER

#demander à l'utilisateur son choix (menu dossier):
def demander_menu_dossier():
    Affichage_Menu_Dossiers()
    choix = input ("Quel est votre choix ?")
    return choix

#demander à l'utilisateur son choix (menu fichier):
def demander_menu_fichier():
    Affichage_Menu_Fichiers()
    choix = input ("Quel est votre choix ?")
    return choix

# reponse True pour Y ou False pour N
def repondreYN(question):
    try :
        response=input(question)
        if(response=="Y" or response=="Y"):       # si la reponse est positive alors retour true
            return True
        elif(response=="n" or response=="N"):     # si la reponse est négative alors retour False
            return False
        else:
            print ("la réponse doit etre Y ou N")   # si la reponse n'est pas correctre alors retour à la question
            repondreYN(question)
    except NameError as e:
        print(f"l'erreur {e} s'est produite")

#En fonction du choix, fait appel à la bonne fonction:

##########################----Routine_dossiers----############################

def routine_dossiers(choix):
    choix = demander_menu_dossier()
    if choix == "1":
        print("Création d'un dossier")
        directory_path = input("Quel est le chemin du dossier ? ")
        creer_dossier(directory_path)

    elif choix == "2":
        print("copie d'un dossier")
        directory_path = input("Quel est le chemin du dossier à copier ? ")
        copy_directory_path = input("Quel est le chemin du dossier de destination ? ")
        copier_dossier(directory_path, copy_directory_path) #A Re-vérifier

    elif choix == "3":
        print("Renommage d'un dossier")
        old_name_directory = input("Quel est le chemin du dossier ? ")
        new_name_directory = input("Quel est le nouveau nom du dossier ? ")
        renommer_dossier(old_name_directory, new_name_directory)  #A Re-vérifier
    # Ajouter une fonction pour verifier le chemin, demander à l'utulisateur d'indiquer le bon chemin si 
    # c'est pas le cas proposer la liste des fichiers du meme nom
    elif choix == "4":
        print("Suppression d'un dossier")
        directory_path = input("Quel est le chemin du dossier ? ")
        supprimer_dossier(directory_path)
        
    elif choix == "5":
        print("Deplacement d'un dossier")
        directory_path = input("Quel est l'ancien chemin du dossier ? ")
        new_directory_path = input("Quel est le nouveau chemin du dossier ? ")
        deplacer_dossier(directory_path) #A Re-vérifier: (directory_path, new_directory_path)

    elif choix == "6":
        print("Existance d'un dossier")
        directory_path = input("Quel est le chemin du dossier ? ")
        existe_dossier(directory_path)
        
    elif choix == "7":
        print("Listage d'un dossier")
        directory_path = input("Quel est le chemin du dossier ? ")
        lister_dossier(directory_path)

    elif choix == "8":
        print("Zip de dossiers et fichiers")
        list_of_elements = liste_dossiers_fichiers_compresses()
        try:
        zip_path = input("Quel est le chemin du dossier compresse?")
        compresser_dossiers_fichiers(list_of_elements, zip_path) #Créée, marche
        except PermissionError:
        print("Permission denied.")
        except:
        print("une erreur est survenue")
    
    elif choix == "9":
        print("Affichage d'un dossier")
        directory_path = input("Quel est le chemin du dossier ? ")
        Afficher_dossier(directory_path)  # En cours

#proposition en fin de fonction
  else:
    print(f"votre choix :{choix} n'est pas correct")
  
  

##########################----Routine_fichiers----############################

def routine_fichiers(choix):
  choix = demander_menu_fichier()
  if choix == "1":
    print("Création d'un fichier")
    file_path = input("Quel est le chemin du fichier ? ")
    creer_fichier(file_path)

  elif choix == "2":
    print("copie d'un fichier")
    file_path = input("Quel est l'ancien chemin du fichier ? ")
    new_file_path= input("Quel est le nouveau chemin du fichier ? ")
    copie_fichier(file_path) #A Re-vérifier: copie_fichier(file_path, new_file_path)

  elif choix == "3":
    print("Renommage d'un fichier")
    ancien_nom_fichier = input("Quel est le chemin du fichier? ")
    nouveau_nom_fichier = input("Quel est le nouveau nom du fichier? ")
    renommer_fichier(file_path) #A Re-vérifier: renommer_fichier(file_path, new_file_path)
        
  elif choix == "4":
    print("Suppression d'un fichier")
    file_path = input("Quel est le chemin du fichier? ")
    supprimer_fichier(file_path)
    
  elif choix == "5":
    print("Deplacement d'un fichier")
    file_path = input("Quel est l'ancien chemin du fichier? ")
    new_file_path= input("Quel est le nouveau chemin du fichier? ")
    deplacer_fichier(file_path) #A Re-vérifier: (file_path, new_file_path)

  elif choix == "6":
    print("Existance d'un fichier")
    file_path = input("Quel est le chemin du fichier? ")
    existe_fichier(file_path)   

  elif choix == "7":
    print("Lecture dans un fichier")
    file_path = input("Quel est le chemin du fichier? ")
    lire_fichier(file_path)  # En cours
    
  elif choix == "8":
    print("Zip de dossiers et fichiers")
    list_of_files = liste_dossiers_fichiers_compresses()
    try:
      zip_path = input("Quel est le chemin du dossier compresse?")
      compresser_dossiers_fichiers(list_of_files, zip_path) #Créée, marche
    except PermissionError:
      print("Permission denied.")
    except:
      print("une erreur est survenue")
  elif choix == "9":
    print("Ecriture dans un fichier")
    file_path = input("Quel est le chemin du fichier? ")
    ecrire_fichier(file_path)  # En cours
  

###################################################################################
#---------------------------------------MAIN--------------------------------------#
###################################################################################


def main():


main()


