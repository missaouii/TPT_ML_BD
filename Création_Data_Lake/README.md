### Import des fichiers
Vous avez tout dabord besoin d'importer les fichiers présents dans ce lien afin d'executer les commandes de création du lac de données: 
1. Télécharger le dossier `fichiers_data`:
  ```
  https://drive.google.com/drive/folders/1_J78fTeA8-aiY4k1yL94_S3BTqYq0JzP?usp=sharing
  ```
2. Coller le dossier `fichiers_data` dans le dossier de la machine:
  ```bash
  cd TPT_ML_BD/VM
  ```

### Architecture du Data Lake:
Comme on peut le voir dans la figure notre lac de données est constitué de:
1. HDFS : `Catalogue.csv,Clients_12.csv,CO2.csv` .
2. MongoDB : `Marketing.csv` .
3. OracleNOSQL : `Immatriculations.csv` .
4. Hive : `Clients_11.csv` .

Hive est notre point d'entré de notre Lac de données, il va donc contenir des tables externes qui vont pointer sur les données physique citées précedement mis à part la table qui est dans Hive.  
On va par la suite faire de la manipulation sur ces données grace à PySpark qui va importer les données à partir des tables externes de hive.  
![Architecture](https://github.com/missaouii/TPT_ML_BD/blob/main/Cr%C3%A9ation_Data_Lake/Architecture%20du%20lac%20de%20donn%C3%A9es.PNG)


