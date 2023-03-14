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
1. 3 fichiers dans ```<span style="color:blue">HDFS</span>``` ,``` "hi"```, `<font color="red">Texte en rouge</font>` `**a**` qui sont `Catalogue.csv,Clients_12.csv,CO2.csv` et puis une collection dans MongoDB qui est `Marketing.csv`, une table dans OracleNOSQL qui est `Immatriculations.csv` et finalement notre point d'entré de notre Data Lake qui est Hive ce dernier va contenir des tables externes qui vont pointer sur les données physique citées précedement et une table interne `Clients_11.csv` qui va contenir des données sur les clients.
On va par la suite faire de la manipulation sur ces données grace à PySpark qui va importer les données à partir des tables externes de hive.  
![Architecture](https://github.com/missaouii/TPT_ML_BD/blob/main/Cr%C3%A9ation_Data_Lake/Architecture%20du%20lac%20de%20donn%C3%A9es.PNG)


