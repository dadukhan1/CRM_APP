import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'passwordis$321'
)

cursorObject = database.cursor()

cursorObject.execute(" CREATE DATABASE firstpracticalsql")

print("ALL done!")