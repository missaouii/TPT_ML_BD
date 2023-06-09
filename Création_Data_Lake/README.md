## Import des fichiers
Vous avez tout dabord besoin d'importer les fichiers présents dans ce lien afin d'executer les commandes de création du lac de données: 
1. Télécharger le dossier `fichiers_data`:
  ```
  https://drive.google.com/drive/folders/1_J78fTeA8-aiY4k1yL94_S3BTqYq0JzP?usp=sharing
  ```
2. Coller le dossier `fichiers_data` dans le dossier de la machine:
  ```bash
  cd TPT_ML_BD/VM
  ```

## Architecture du Data Lake:
Comme on peut le voir dans la figure notre lac de données est constitué de:
1. HDFS : `Catalogue.csv,Clients_12.csv,CO2.csv` .
2. MongoDB : `Marketing.csv` .
3. OracleNOSQL : `Immatriculations.csv` .
4. Hive : `Clients_11.csv` .

Hive est notre point d'entré de notre Lac de données, il va donc contenir des tables externes qui vont pointer sur les données physique citées précedement mis à part la table qui est dans Hive.  
On va par la suite faire de la manipulation sur ces données grace à PySpark qui va importer les données à partir des tables externes de hive.  
![Architecture](https://github.com/missaouii/TPT_ML_BD/blob/main/Cr%C3%A9ation_Data_Lake/Architecture%20du%20lac%20de%20donn%C3%A9es.PNG)


## Création du Data Lake:
### Partie MongoDB:
1.Connexion à Mongo Shell :
  ```bash
  mongosh
  ```
2.Création et connexion à la base :
  ```
  use project
  ```
3.Création de la collection marketing :
 ```
  db.createCollection("marketing")
  ```
4.Import du fichier dans la collection marketing :
 ```
  mongoimport --port 27017 --host localhost --db project --collection marketing --type csv --file "/vagrant/fichiers_data/Marketing.csv" --headerline
  ```  
  
### Partie ORACLE NoSQL:  
1.Lancer KVStore :
  ```bash
  nohup java -Xmx64m -Xms64m -jar $KVHOME/lib/kvstore.jar kvlite -secure-config disable -root $KVROOT &
  ```
2.Lancer KVStoreAdminClient :
  ```bash
  java -jar $KVHOME/lib/kvstore.jar runadmin -port 5000 -host localhost
  ```
3.Connexion à KVStore :
  ```bash
  connect store -name kvstore
  ```
4.Création de la table :
  ```
  execute 'Create table immatriculations (immatriculation string,marque string, nom string, puissance integer, longueur string, nbPlaces integer,nbPortes integer, couleur string, occasion string, prix integer, id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1 ), primary key(id))'
  ```
5.Charger le fichier Immatriculations.json dans la table :
  ```
  put table -name immatriculations -file /vagrant/fichiers_data/Immatriculations.json
  ```  
  
### Partie HDFS:  
1.Lancer Hadoop :
  ```bash
  start-dfs.sh
  start-yarn.sh
  ```  
2.Creation de dossier pour le projet :
  ```bash
  hdfs dfs -mkdir /project
  hdfs dfs -mkdir /project/catalogue
  hdfs dfs -mkdir /project/Clients_12
  hdfs dfs -mkdir /project/CO2
  ```  
3.Import des fichiers :
  ```bash
  hadoop fs -put /vagrant/fichiers_data/Clients_12.csv /project/Clients_12
  hadoop fs -put /vagrant/fichiers_data/catalogue.csv /project/catalogue
  hadoop fs -put /vagrant/fichiers_data/CO2.csv /project/CO2
  ```  
  
### Partie Hive :  
#### Création de tables externes :
1.TABLE Immatriculations_hive_ext :
  ```
	CREATE EXTERNAL TABLE  Immatriculations_hive_ext(immatriculation STRING,  
	marque STRING,
	nom STRING,
	puissance  int,
	longueur string,
	nbPlaces int,
	nbPortes int,
	couleur string,
	occasion string,
	prix int, 
	id int)
	ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
	WITH SERDEPROPERTIES (
	  'serialization.format' = '1'
	)
	STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
	TBLPROPERTIES (
	  "oracle.kv.kvstore" = "kvstore",
	  "oracle.kv.hosts" = "localhost:5000",
	  "oracle.kv.hadoop.hosts" = "localhost/127.0.0.1",
	  "oracle.kv.tableName" = "immatriculations"
	);	
  ```  
2.TABLE catalogue_hive_ext :
  ```
	CREATE EXTERNAL TABLE  catalogue_hive_ext(marque STRING,  nom STRING, puissance  int, longueur string, nbPlaces int,nbPortes int, couleur string, occasion string, prix int)
	ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
	STORED AS TEXTFILE LOCATION 'hdfs:/project/catalogue'
	tblproperties("skip.header.line.count"="1");
  ```  
3.TABLE  Clients_12_hive_ext :
  ```
	CREATE EXTERNAL TABLE  Clients_12_hive_ext(age int,sexe string,taux int,situationFamiliale string,nbEnfantsAcharge int,deuxieme_voiture string,immatriculation string)
	ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
	STORED AS TEXTFILE LOCATION 'hdfs:/project/Clients_12'
	tblproperties("skip.header.line.count"="1");
  ```   
4.TABLE CO2_hive_ext :
  ```
	CREATE EXTERNAL TABLE IF NOT EXISTS CO2_hive_ext (
	  id int,
	  Marque_Modele String,
	  Bonus_Malus String,
	  Rejets_CO2_g_km String,
	  Cout_enerie String
	)
	ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
	STORED AS TEXTFILE LOCATION 'hdfs:/project/CO2'
	tblproperties("skip.header.line.count"="1");
  ```   
5.Table Marketing_hive_ext :
  ```
	CREATE EXTERNAL TABLE IF NOT EXISTS Marketing_hive_ext (
	  age int,
	  sexe String,
	  taux int,
	  situationFamiliale String,
	  nbEnfantsAcharge int,
	  deuxieme_voiture string
	)
	STORED BY 'com.mongodb.hadoop.hive.MongoStorageHandler'
	WITH SERDEPROPERTIES(
	  'mongo.columns.mapping'='{"age":"age","sexe":"sexe","taux":"taux","situationFamiliale":"situationFamiliale","nbEnfantsAcharge":"nbEnfantsAcharge","deuxieme_voiture":"2eme voiture"}',
	  'mongo.input.format'='com.mongodb.hadoop.mapred.BSONFileInputFormat',
	  'mongo.output.format'='com.mongodb.hadoop.mapred.BSONFileOutputFormat'
	)
	TBLPROPERTIES (
	  'mongo.uri'='mongodb://localhost:27017/project.marketing',
	  'mongo.input.format'='com.mongodb.hadoop.hive.BSONFileInputFormat',
	  'mongo.output.format'='com.mongodb.hadoop.hive.BSONFileOutputFormat',
	  'mongo.job.input.format'='com.mongodb.hadoop.mapred.BSONFileInputFormat',
	  'mongo.job.output.format'='com.mongodb.hadoop.mapred.BSONFileOutputFormat',
	  'mongo.input.query'='{}'
	);
  ```   
   
#### Création de tables internes :  
1.Table Clients_11_hive_int :  
  ```
	CREATE TABLE Clients_11_hive_int (
	  age INT,
	  sexe STRING,
	  taux int,
	  situationFamiliale string,
	  nbEnfantsAcharge int,
	  deuxieme_voiture string,
	  immatriculation string
	)
	ROW FORMAT DELIMITED
	FIELDS TERMINATED BY ','
	LINES TERMINATED BY '\n'
	STORED AS TEXTFILE;


	LOAD DATA LOCAL INPATH '/vagrant/fichiers_data/Clients_11.csv' OVERWRITE INTO TABLE Clients_11_hive_int;
  ```     

