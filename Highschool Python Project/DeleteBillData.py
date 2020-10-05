import mysql.connector
import os
import platform
def deleteData():
        cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
        cursor=cnx.cursor()
        BillNo=input("Enter the Bill number to be deleted:")
        Qry=("DELETE FROM bill WHERE BillNo = %s")
        del_rec=(BillNo,)
        cursor.execute(Qry,del_rec)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,"Bill data deleted successfully")
while True:
        deleteData()
