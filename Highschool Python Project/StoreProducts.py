from mysql.connector import errorcode
from datetime import  date,datetime,timedelta
import mysql.connector
import os
import platform
def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))
        
def display():    
    cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    cursor=cnx.cursor()
    query=("select * from aps")
    cursor.execute(query)
    for(No,Model,Warranty,Colour,Specs,INR) in cursor:
        print("======================================")
        print("Product No:",No)
        print("Model:",Model)
        print("Warranty duration:",Warranty)
        print("Colour:",Colour)
        print("Specifications:",Specs)
        print("Price",INR)
        print("======================================") 
        #cursor.close()
        #cnx.close()
        
def insertData():
        cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
        cursor=cnx.cursor()
        No=int(input("Enter no:"))
        Model=input("Enter model:")
        Warranty=input("Enter duration of warranty:")
        Colour=input("Enter colour:")
        Specs=input("Enter specifications of the product:")        
        INR=int(input("Enter Price:"))
        cursor.execute('insert into aps values(%s,"%s","%s","%s","%s",%s)'%(No,Model,Warranty,Colour,Specs,INR))
        cnx.commit()  
        cursor.close()
        cnx.close()
        print("Product Inserted")
        
def deleteData():    
        cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
        cursor=cnx.cursor()
        No=input("Enter the  product number to be deleted:")
        Qry=("DELETE FROM aps WHERE No = %s")
        del_rec=(No,)
        cursor.execute(Qry,del_rec)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,"Record(s)Deleted Successfully")

def SearchData():
    cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    cursor=cnx.cursor()
    No=input("Enter no to be searched from the Store:")
    query=("SELECT * FROM aps where No = %s ")
    rec_srch=(No,)
    cursor.execute(query,rec_srch)
    Rec_count=0
    for (No,Model,Warranty,Colour,Specs,INR) in cursor:
        Rec_count+=1
        print("======================================")
        print("Product No:",No)
        print("Model:",Model)
        print("Warranty duration:",Warranty)
        print("Colour:",Colour)
        print("Specifications:",Specs)
        print("Price",INR)
        print("======================================")
        if Rec_count%2==0:
            input("Press any key to continue")    
            clrscreen()
            print(Rec_count,"Record(s) found")                    
        #cnx.close()
                   
def updateData():
    cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    cursor=cnx.cursor()
    No=input("Enter no to be updated from the Store:")
    print("Enter '/', if you want the details to remain unchanged.")
    Model=input("Model:")
    if(Model=="/"):
        pass
    else:
        Qry=("update aps set Model=%s where No=%s")
        data=(Model,No)
        cursor.execute(Qry,data)  
        cnx.commit()
        print(cursor.rowcount,"New data updated successfully")
    Warranty=input("Warranty:")
    if(Warranty=="/"):
        pass
    else:
        Qry=("update aps set Warranty=%s where No=%s")
        data=(Warranty,No)
        cursor.execute(Qry,data)  
        cnx.commit()
        print(cursor.rowcount,"New data updated successfully")
    Colour=input("Colour:")
    if(Colour=="/"):
        pass
    else:
        Qry=("update aps set Colour=%s where No=%s")
        data=(Colour,No)
        cursor.execute(Qry,data)  
        cnx.commit()
        print(cursor.rowcount,"New data updated successfully")
    Specs=input("Specifications:")    
    if(Specs=="/"):
        pass
    else:
        Qry=("update aps set Specs=%s where No=%s")
        data=(Specs,No)
        cursor.execute(Qry,data)  
        cnx.commit()
        print(cursor.rowcount,"New data updated successfully")
    INR=input("INR:")    
    if(INR=="/"):
        pass
    else:
        Qry=("update aps set INR=%s where No=%s")
        data=(INR,No)
        cursor.execute(Qry,data)  
        cnx.commit()
        print(cursor.rowcount,"New data updated successfully")     
    cnx.close()
c="y"
while c=="y":
    print("Choose choice from the following:")
    print(" 1.Update Product \n 2.Display Product\n 3.Delete Product\n 4.Insert Product\n 5.Search Product")    
    ch=input("Enter choice:")
    if ch=="1":        
        updateData()
        c=input("Do you want to continue, type y/n:")    
    elif ch=="2":
        display()
        c=input("Do you want to continue, type y/n:")    
        
    elif ch=="3":
        deleteData()
        c=input("Do you want to continue, type y/n:")   
    elif ch=="4":
        insertData()
        c=input("Do you want to continue, type y/n:")    
    elif ch=="5":
        SearchData()
        c=input("Do you want to continue, type y/n:")    
else:    
    print("Thank for your time")
    #c=input("Do you want to continue, type y/n:")
    
   
                    
       
        
    
    
    
        
                  
                                       
            


        
            

    
            
