## Objectif :  

Cette partie consiste à importer le modèle randomforest sous forme d'un fichier `.pkl` pour ne pas le relancer à chaque utilisation de l'API.  
Ensuite, l'utilisateur peut mettre ces données en entrée sous forme de POST dans l'API, et cette dernière va lui afficher la catégorie de voiture qui lui va le mieux.  
Il y aura evidement un controle sur les données en entrée.

## Telecharger l'image :  
Executer dans le CMD la commande suivante :  
  ```bash
  docker pull ramzimissaoui/tpt_api_randomforest:1.0
  ```  
## Lancer le serveur :  
Executer dans le CMD la commande suivante :  
  ```bash
  docker run -p 8000:8000 $image_id
  ```
Se connecter sous cette adresse :  
  ```
  http://localhost:8000/docs
  ```




