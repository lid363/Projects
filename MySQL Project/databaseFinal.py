"""
Author:      Danhong Li
DATE:        Dec,13,2020
Description: MYSQL Database and Python
"""

import mysql.connector
from mysql.connector import errorcode


def get_db():
    try:
        myconnection = mysql.connector.connect(
            host="localhost",
            user="GAME_ADMIN",
            password="ABCD1234",
            database="farm_game"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
    return myconnection


def displayAll():
    db = get_db()
    mycursor = db.cursor()
    player_query = (
        "SELECT P.Player_FirstN, P.Player_LastN,P.Enroll_Time,P.Coin,B.Crop_Num,C.CropName,C.Buy_Price,C.Sell_Price "
        "FROM Player P INNER JOIN Bag B ON P.PlayerID = B.PlayerID "
        "INNER JOIN Crop C ON B.CropID = C.CropID "
        "GROUP BY B.BagID;"
    )

    mycursor.execute(player_query)
    records = mycursor.fetchall()
    for r in records:
        print("{:<15} {:<15} {:>20} {: >10} {: >10} {: >10} {: >10} {: >10}".format(r[0], r[1],
                                                                                    r[2].strftime("%m-%d-%Y %H:%M:%S"),
                                                                                    r[3], r[4], r[5], r[6], r[7]))
    mycursor.close()


def search_by_playerName():
    db = get_db()
    mycursor = db.cursor()
    print("\n\n***** Search by Player Name")
    f_name = input("Enter player first name: ")
    l_name = input("Enter player last name: ")
    player_query = (
        'SELECT P.Player_FirstN,P.Player_LastN,B.BagID,B.Crop_Num,C.CropName, C.Buy_Price,C.Sell_Price '
        'FROM Bag B '
        'INNER JOIN Crop C ON B.CropID = C.CropID '
        'INNER JOIN Player P ON B.PlayerID = P.PlayerID '
        'WHERE B.PlayerID = (SELECT PlayerID FROM Player WHERE(Player_FirstN = "{}" AND  Player_LastN= "{}" ))'.format(
            f_name, l_name)

    )

    mycursor.execute(player_query)
    playerInfo = mycursor.fetchall()
    if playerInfo is None:
        print("\nPlayer not exist!")
    else:
        print("\n{} {} has".format(f_name, l_name))
        for p in playerInfo:
            print("\tBag {} contains {} {} buying price is {}/lb selling price is {}/lb.".format(p[2], p[3], p[4], p[5],
                                                                                                 p[6]))
    mycursor.close()


def add_player():
    db = get_db()
    mycursor = db.cursor()
    print("\n\n***** Add new Player")
    f_name = input("Enter player first name: ")
    l_name = input("Enter player last name: ")
    coin = input("Enter player owned coin: ")
    playerData = (f_name, l_name, coin)
    addSql = (
        'INSERT INTO Player(Player_FirstN,Player_LastN,Coin)'
        'VALUES (%s,%s,%s)'
    )
    mycursor.execute(addSql, playerData)
    db.commit()


def delete_player():
    db = get_db()
    mycursor = db.cursor()
    print("\n\n***** Delete a Player's all data")
    f_name = input("Enter player first name: ")
    l_name = input("Enter player last name: ")
    player = (f_name, l_name)

    delSql = "DELETE FROM Player WHERE (Player_FirstN=\"%s\"AND Player_LastN=\"%s\")"
    mycursor.execute(delSql, player)
    db.commit()


def update_data():
    db = get_db()
    mycursor = db.cursor()
    print("\n\n***** Update the number of crop")
    bagId = input("Enter bag id want to update: ")
    cropNum = input("Enter num of the crop: ")
    data = (cropNum, bagId)
    updateSql = "UPDATE Bag SET Crop_Num = %s WHERE BagID = %s"
    mycursor.execute(updateSql, data)
    db.commit()


displayAll()
search_by_playerName()
add_player()
delete_player()
update_data()
