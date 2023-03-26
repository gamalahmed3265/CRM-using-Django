import mysql.connector

database=mysql.connector.connect(
        #full your conv
)

cursorObject=database.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print("all done....")