
CREATE DATABASE Farm_Game;
 
CREATE USER GAME_ADMIN IDENTIFIED BY "ABCD1234";
GRANT SELECT, INSERT, UPDATE, DELETE ON Farm_Game.* to GAME_ADMIN;

 CREATE TABLE Player(
 PlayerID INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 Player_FirstN VARCHAR(80) NOT NULL,
 Player_LastN VARCHAR(80) NOT NULL,
 Enroll_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 Coin INT(60)
 );

 
CREATE TABLE Bag(
 BagID INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 CropID INT(8),
 Crop_Num INT(60),
 PlayerID INT(8),
 FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID) ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY(CropID) REFERENCES Crop(CropID) ON DELETE CASCADE ON UPDATE CASCADE
 );
 
 
 CREATE TABLE Crop(
 CropID INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 CropName VARCHAR (80) NOT NULL,
 Buy_Price INT(30),
 Sell_Price INT(30)
 );
 

 
 INSERT INTO Crop(CropName,Buy_Price,Sell_Price)
 VALUES("Oat",10,20),
		("Barley",12,21),
		("Corn",8,13),
		("Rye",7,15);
		
INSERT INTO Crop(CropName,Buy_Price,Sell_Price)
 VALUES("Apple",15,35),
		("Banana",6,22),
		("Soybean",3,8),
		("Flax",23,42),
		("Peanut",11,22),
		("Millet",40,46),
		("Sorghum",56,69),
		("Potato",6,9),
		("Tomato",10,17),
		("Strawberry",16,26);
 
 
 INSERT INTO Bag(CropID,Crop_Num,PlayerID)
 VALUES(3,12,2),
	   (13,5,5),
	   (8,4,2),
	   (11,9,3),
	   (14,6,4),
	   (9,14,5),
	   (14,2,5);
	   
INSERT INTO Bag(CropID,Crop_Num,PlayerID)
VALUES (1,12,1),
	   (6,5,2),
	   (2,4,2),
	   (4,9,3),
	   (5,6,2),
	   (7,14,6),
	   (10,15,5),
	   (12,30,4),
	   (10,1,6);
  
 
 INSERT INTO Player(Player_FirstN,Player_LastN,Coin)
 VALUES ("Aneesa","Potts",1500),
		("Liana ","Macleod",950),
		("Cathal","Randolph",600),
		("Inez","Ward",1843),
		("Jolie","Holcomb",1785),
		("Piper","Tierney",2689);
		
		
CREATE VIEW Num_Player_CropView AS
SELECT C.CropName, COUNT("Number of player has")
FROM Crop C
JOIN Bag B on B.CropID = C.CropID
GROUP BY C.CropID;



CREATE INDEX Name ON Player (Player_FirstN);




