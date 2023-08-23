import os
import shutil
from fichiers import *

###################################################################################
#---------------------------------DOSSIERS----------------------------------------#
###################################################################################


# 1 : Création d'un dossier
def creer_dossier(directory_path):
  try:
    os.mkdir(directory_path)  #os.makedirs
  except:
    print('Le dossier est déja créé')


###################################################################################
###################################################################################


# 2 : Copie d'un dossier
def copier_dossier(directory_path, copy_directory_path):  #A Re-vérifier: (OldNomDossier, NewNomDossier)
    try:
      ancien_dossier = "path_ancien-dossier"
      nouveau_dossier = "path_nouveau-dossier"
      shutil.copytree(directory_path, copy_directory_path)
    except:
      print("Une erreur s'est produite")


###################################################################################
###################################################################################


# 3 : Renommage d'un dossier
def renommer_dossier(directory_path, new_name_directory):  #A Re-vérifier
    old_name_dossier = directory_path
    # new_name_directory = input("Entrer le nouveau nom du fichier: ")
    try:
      os.rename(old_name_dossier, new_name_directory)
    except:
      print("erreur")


###################################################################################
###################################################################################


# 4 : Suppression d'un dossier
def supprimer_dossier(directory_path):
  try:
    os.rmdir(directory_path)
  except:
    print('le dossier n\'existe pas ou n\'est pas vide')


###################################################################################
###################################################################################


# 5 : Déplacement d'un dossier
def deplacer_dossier(directory_path):  #A Re-vérifier: (directory_path, new_directory_path)
  new_directory_path = input("Entrer le nouveau chemin du dossier:")
  try:
    shutil.move(directory_path, new_directory_path)
  except:
    print("l\'adresse de depart ou d\'arrive n\'est pas valide")


###################################################################################
###################################################################################


# 6 : Vérifier l'existance d'un dossier
def existe_dossier(directory_path):
  if os.path.exists(directory_path):
    print("le dossier existe bien à cette adresse")
  else:
    print("le dossier n'existe pas")


###################################################################################
###################################################################################


# 7 :  Lister les dossiers
def lister_dossier(directory_path):
  try:
    list = os.listdir(directory_path)
    print(f"--------- {directory_path} ----------")
    for element in list:
      print(element)
    print(f"-------------------------------------------------")
  except:
    print("Le dossier n'existe pas")


###################################################################################
###################################################################################

# 8 :  Compresser dossiers
#compresser_dossiers_fichiers(list_element_path, zip_path)
# cette fonction est dans fichiers.py

###################################################################################
###################################################################################


# 9 :  Afficher dossiers
def Afficher_dossier(directory_path):
  return 0


# fonctions pour se positionner
