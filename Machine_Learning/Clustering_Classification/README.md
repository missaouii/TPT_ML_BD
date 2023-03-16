## Clustering :  

Dans cette partie on a :  
1. Importer le fichier `Catalogue.csv`.  
2. Exploration du comportement, nettoyage et manipulation (Feature engineering) des données .  
3. Appliquer des méthodes pour prédire le nombre potentiel de cluster :   
	3.1 Elbow Method :  
	![Elbow_Method](https://github.com/missaouii/TPT_ML_BD/blob/main/Machine_Learning/Clustering_Classification/Elbow_method.png)  
	3.2 Silhouette  Method :  
	![Silhouette_Method](https://github.com/missaouii/TPT_ML_BD/blob/main/Machine_Learning/Clustering_Classification/Silhouette_method.png)  
	3.3 dendrogram Method :  
	![dendrogram_Method](https://github.com/missaouii/TPT_ML_BD/blob/main/Machine_Learning/Clustering_Classification/dendrogram_method.png)  
  
4. Application De K-means avec 4 clusters :  
	![K-means](https://github.com/missaouii/TPT_ML_BD/blob/main/Machine_Learning/Clustering_Classification/Kmeans_Diagramme.png)  
	![PCA_K-means](https://github.com/missaouii/TPT_ML_BD/blob/main/Machine_Learning/Clustering_Classification/PCA_K-means.png)  
	
5. Etude approfondi des données pour dégager les 4 catégories de voitures

## Classification :  
Dans cette partie on a :  
1. Ajoutern la colonne catégorie dans le fichier Client grace à quelques jointures  
2. nettoyage de données .  
3. Manipulation des données comme par exemple :  
	3.1 Standardisation des données numérique.  
	3.2 Transformer les données catégorielles en vecteurs numérique.  
	3.3 Equilibrer les classes etc...  
4. Appliquer plusieurs algorithmes de classification avec une optimisation de leur hyperparamètres.  
5. Mettre le Dataframe dans un fichier pickle pour l'utiliser dans MLFLOW pour comparer nos modèles.  
6. Mettre le meilleur dans un fichier pickle pour l'utiliser dans l'API.  
 