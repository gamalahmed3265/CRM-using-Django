import mysql.connector

database=mysql.connector.connect(
       
)

cursorObject=database.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print("all done....")