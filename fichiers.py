import os
import shutil
import zipfile

from dossiers import deplacer_dossier
from Projet import repondreYN

###################################################################################
#---------------------------------FICHIERS----------------------------------------#
###################################################################################


#Marche
# 1 : Création d'un fichier
def creer_fichier(file_path):
    try:
      file = open(file_path, "x")  #file path ou nom du fichier?
      file.close()
      print("Le fichier à été créé avec succès")
    except PermissionError:
      print("Permission denied.")
    except EnvironmentError as e:
      print(f"Impossible de créer le fichier, erreur : {e}")
    except:
      print('Une erreur est survenue lors de la création du fichier')


#autre propostition : (c'est plus joli mais renvoie une erreur, à vérifier dans la phase de finition)
# def creer_fichier(file_path):
#   try:
#     with open(file_path) as file:
#       print(file.read())
#   except NameError as e:
#       print(f"l'erreur {e} s'est produite")

###################################################################################
###################################################################################


#Marche
# 2 : Copier un fichier
def copie_fichier(file_path):  #A Re-vérifier: def copie_fichier(file_path, new_file_path):
    new_file_path = input("Entrer le nouveau chemin du fichier:")
    try:
        shutil.copy(file_path, new_file_path)
        print("Le fichier a ete copie avec succes")
    except shutil.SameFileError:
        print("Il existe deja un fichier portant ce nom dans ce dossier")
    except PermissionError:
        print("Permission denied.")
    except:
        print("Une erreur s'est produite lors de la copie du fichier")


###################################################################################
###################################################################################


#Marche
# 3 :Renommage d'un fichier
def renommer_fichier(file_path):
    try:
      nom_fichier = file_path
      nouveau_nom_fichier = input("quel est le nouveau chemin du fichier? ")
      os.rename(nom_fichier, nouveau_nom_fichier)
      print("le fichier a ete renomme avec succes")
    except PermissionError:
      print("Permission denied.")
    except EnvironmentError as e:
      print(f"Le fichier est introuvable ou le nouveau nom n\'est pas valide : {e}")
    except:
      print('Une erreur est survenue lors du renommage du fichier')


###################################################################################
###################################################################################


#Marche
# 4 : Suppression d'un fichier
def supprimer_fichier(file_path):
    try:
      os.remove(file_path)
      print("le fichier a ete supprime avec succes")
    except PermissionError:
      print("Permission denied.")
    except EnvironmentError as e:
      print(f"erreur lors de la suppression du fichier : {e}")
    except:
      print("Une erreur est survenue lors de la suppression du fichier")


###################################################################################
###################################################################################


#Marche
# 5: Déplacement d'un fichier
def deplacer_fichier(file_path):
    new_file_path = input("Entrer le nouveau chemin du fichier:")
    try:
      os.replace(file_path, new_file_path)
      print("le fichier a bien ete deplace")
    except PermissionError:
      print("Permission denied.")
    except:
      print("l'adresse de depart ou d'arrive n'est pas valide")


###################################################################################
###################################################################################


#Marche
#6 : Verification de  l'existence d'un fichier
def existe_fichier(file_path):
  try:
    exist = os.path.exists(file_path)  #return True si le fichier existe
    if exist:
      print("le fichier existe")
    else:
      print("le fichier n'existe pas")
    return exist
  except PermissionError:
      print("Permission denied.")
  except:
      print("Une erreur s'est produite lors de la vérification de l'existence du fichier")


###################################################################################
###################################################################################


#  (marche que pour les fichiers textes, il y a des problèmes d'encodage)
#  à modifier pour vérifier que le fichier est un fichier texte, ou
#    le modifier pour qu'il lise plus de format de fichiers
# 7 : Lecture d'un fichier
def lire_fichier_texte(file_path):
  # with open(file_path, 'r', encoding="utf-8") as file:
  #   print(file.read())

  try:
    with open(file_path, 'r') as file:
      print(file.read())
  except PermissionError:
    print("Permission denied.")
  except EnvironmentError as e:
    print(f"Impossible de lire le fichier, erreur : {e}")
  except:
    print("Une erreur s'est produite lors de la lecture du fichier, est-ce un fichier texte?")


###################################################################################
###################################################################################


#Marche
# 8 : Compression d'un fichier
def compresser_dossiers_fichiers(list_element_path, zip_path):
  # on selectionne le bon mode de compresssion: mode ZIP_DEFLATED
  compression = zipfile.ZIP_DEFLATED
  #on affiche la liste des fichiers que l'on compresse
  print(f" *** liste des elements a compresser - {list_element_path}")
  #on affiche le nom du dossier zip et on cree le dossier
  print(f' *** nom du dossier compresse - {zip_path}')
  zipf = zipfile.ZipFile(zip_path, mode="w")

  #on parcourt la liste des fichiers, et on les ajoute un a un dans le zip
  try:
    for element_to_write in list_element_path:
      #on affiche quel fichier est ajouté
      if os.path.isfile(element_to_write):  #on regarde si l'element a ajouter est un fichier
        print(f' *** Processing file {element_to_write}')
        #on ajoute le fichier dans le zip
        zipf.write(element_to_write,element_to_write,compress_type=compression)
      elif os.path.isdir(
        element_to_write):  #on regarde si l'element a ajouter est un dossier
        print(f' *** Processing directory {element_to_write}')
        #on ajoute le dossier et son contenu dans le zip
        #os.walk sert à parcourrir les dossiers et leurs contenus
        #on demande pour le dossier en question, chaque élément du dossier (files)
        for directory_root, _, files in os.walk(element_to_write):
        #pour chaque élément dans l'élément du dossier de la liste des éléments à compresser
          for file in files:
            #le chemin de l'élément
            file_path = os.path.join(directory_root, file)
            #relpath renvoie le chemin relatif à partir du dossier root (celui de la liste donc)
            arcname = os.path.relpath(file_path, element_to_write)
            #on l'écrit dans le fichier, avec le dossier de la liste
            zipf.write(file_path,arcname=os.path.join(os.path.basename(element_to_write),arcname))
            print(f"{file_path} ajouté au fichier zip.")
  except FileNotFoundError as e:
    print(f' *** Exception occurred during zip process - {e}')
  finally:
    #on ferme le fichier zip
    zipf.close()


# fonction pour définir les fichiers à compresser
def liste_dossiers_fichiers_compresses():
  add_file = True  #pour savoir si on continue à ajouter des fichiers à compresser
  list_of_files = []  #liste des fichiers à compresser
  print("Veuillez entrer les noms (pas les chemins) des fichiers à compresser:")
  #cette boucle demande d'ajouter un fichier dans une liste
  #on teste si le nom du fichier existe, si oui on teste s'il n'est pas déjà dans la liste
  #on ajoute le fichier, puis on demande si on en ajoute d'autres
  while add_file == True:
    file_path = input("Quel est le nom du fichier? ")
    if existe_fichier(file_path):
      if file_path not in list_of_files:
        list_of_files.append(file_path)
        choix_valide = False  #pour demander si on ajoute d'autres fichiers à compresser
      else:
        print("ce fichier est déjà dans la liste des fichiers a compresser")
        choix_valide = False
    else:
      print("le fichier n'existe pas, veuillez entrer un autre nom de fichier")
      choix_valide = True  #on ne demande par si on ajoute d'autres fichiers à compresser
      add_file = True  #on continue à ajouter des fichiers

    #on demande si on ajoute d'autres fichiers à compresser, sauf erreur
    # ask_add_file = ""
    # while choix_valide == False:
    #   ask_add_file = input(
    #       "Voulez-vous ajouter un autre fichier a compresser? (y/n) ")
    #   if ask_add_file == "n":
    #     add_file = False  #on termine la création de la liste de fichiers
    #     choix_valide = True
    #   elif ask_add_file == "y":
    #     choix_valide = True
    #     # add_file reste True, on continue d'ajouter des fichiers dans la liste
    #   else:
    #     print("vous devez repondre par y ou n"
    #           )  #on continue si reponse != (y or n)

    add_file=repondreYN("Voulez-vous ajouter un autre fichier a compresser? (y/n) ")

  return list_of_files


###################################################################################
###################################################################################


# 9 : Ecriture dans un fichier
def ecrire_fichier(file_path):
  return 0
