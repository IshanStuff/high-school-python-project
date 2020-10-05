import mysql.connector
import os
import platform
def deleteData():    
        cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
        cursor=cnx.cursor()
        Customername=input("Enter the Customer name to be deleted:")
        Qry=("DELETE FROM cinfo WHERE CustomerName = %s")
        del_rec=(Customername,)
        cursor.execute(Qry,del_rec)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,"Customer data deleted successfully")
while True:
        deleteData()

