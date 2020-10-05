import mysql.connector
import os
import platform
import datetime           
print('''                                                               
,---.          |             ,---.|                   
|---|,---.,---.|    ,---.    `---.|--- ,---.,---.,---.
|   ||   ||   ||    |---'        ||    |   ||    |---'
`   '|---'|---'`---'`---'    `---'`---'`---'`    `---'
     |    |                                                                                                                                                                                                                      
''')                                                                                            
print("AVAILABLE PRODUCTS:")
def display():
    print('''                                                                  
1.
         __________________________________________________________                       
       .'                                                          '.                      
     | |      ________________________________________________      | |                   
     | |    .:________________________________________________:.    | |             Apple iMac 21.5-inch(2019)      
     | |    |                                                  |    | |             CPU:3.0GHZ Intel Core i5-8500(six-core,     
     | |    |                                                  |    | |             9MB cache, upto 4.1 GHz with Turbo Boost)     
     | |    |                                                  |    | |             Graphics:AMD Radeon Pro 560x    
     | |    |                                                  |    | |             RAM:8GB DDR4(2,666MHz)
     | |    |                                                  |    | |             Storage:1TB Fusion Drive(32GB SSD plus  
     | |    |                                                  |    | |             1TB hard disk) 
     | |    |                                                  |    | |             Warranty: 1 year
     | |    |                                                  |    | |             INR:1,69,900
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |                                                  |    | |
     | |    |            __________________________            |    | |
     | |    |           |  |  |  |  |  |  |  |  |  |           |    | |
     | |    '.__________|__|__|__|__|__|__|__|__|__|__________.'    | |
     | |                                                            | |
     | |                            iMac                            | |
     : '.__________________________________________________________.' :
      ".____________________________\__/____________________________."
                                     ||
                                     ||
                                     ||
                                  ___||___
                            _.--""   ""   ""--._
                         .'"       .-L-.        "'.
                       .'          : _ (           '.
                     .'             " "              '.
                    .'                                '.
                    :         ________________         :
                   .'       .'                '.       '.
                   :        '.________________.'        :
                   |----......______    ______......----|
                   :                """"                :
                   '.                                  .'
                     "-.____. . . . . . . . . . ____.-"                                      
                            """"""--------""""""        
2.

                 ]]]/@@@@@@/@/`.[@@@@@@@@@\.                         
               =@@@@@@@@\@@@^     =@@@@@@@@@`                                   Apple Watch Series 5
             ./@@@@\@@/\@@@`.       \@@@@@@@`                                   Colour: Space Grey        
            ,@@/@@@@@^O@@@^           \@@@@@@`                                  Specifications: 40/44mm,50m Water Resistance,
           /@@@@@@@@,/@@/.             \@@@@@@`                                 Dual Core S5 Processor
         ,@@@@@@@@//\@@^               .@@@@@@@                                 Warranty:1 year
        =@@@@@@@@`O\@O`                 =@@@@@@`                                INR:53,000
       =@@@@@@@@]@@@/.                  .@@@@@@^ 
       .oooooooO@@O`                    .@@@@@@^ 
        .@]]]]]]O                      .]/[*@[,@`
        ,@@@@@@@                       =@. `\ .@^
        =@@@@@@^                       .*[[[[[=^.
        =@@@@@@                                  
        @@@@@@^                                  
        @@@@@@^

''')
display()    
CustomerName=input("Enter name:")
CustomerMobileNumber=int(input("Enter mobile number:"))  
n=int(input("How many products do you want to purchase?"))
i=0
while i<n:
    cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    cursor=cnx.cursor()    
    No=input("Enter the number of the product to purchase:")
    query=("SELECT Model,INR FROM aps where No = %s ")
    rec_srch=(No,)
    cursor.execute(query,rec_srch)
    Rec_count=0
    for (Model,INR) in cursor:
        Rec_count+=1
        print("Product:",Model)
        print("Price:",INR)
        q=int(input("How many do you want?:"))
        Total=INR*q
        print("Total amount:",Total)
        DateOfPurchase=datetime.date.today()
        cursor=cnx.cursor()
        cursor.execute("SELECT count(*) FROM bill")
        count=cursor.fetchone()[0]
        count+=1       
    #cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    #cursor=cnx.cursor()      
    cursor.execute('insert into bill values(%s,"%s","%s",%s,%s)'%(count,Model,DateOfPurchase,q,Total))
    cursor.execute('insert into cinfo values("%s",%s,"%s","%s")'%(CustomerName,CustomerMobileNumber,Model,DateOfPurchase))
    cnx.commit()
    #cursor.close()
    #cnx.close()
    print("Bill created and inserted")   
    i+=1
    #cnx=mysql.connector.connect(user='root',password='rani',host='localhost',database='applestore')
    #cursor=cnx.cursor()
    #billno=("SELECT count(*) FROM bill")
    print("Your Bill number is:",count)    
    BillNo=input("Enter Billno to view bill:")
    query=("SELECT * FROM bill where BillNo = %s ")
    rec_srch=(BillNo,)
    cursor.execute(query,rec_srch)
    print("BILL:")
    for(BillNo,Product,DateOfPurchase,q,Total) in cursor:
        print("************************************")
        print("Bill No:",count)
        print("Product:",Product)
        print("Date of purchase:",DateOfPurchase)
        print("Quantity:",q)
        print("Total:",Total)
        print("************************************")
        print('''                                                                              
--.--|              |                           ,---.          
  |  |---.,---.,---.|__/     ,   .,---..   .    |__. ,---.,---.
  |  |   |,---||   ||  \     |   ||   ||   |    |    |   ||    
  `  `   '`---^`   '`   `    `---|`---'`---'    `    `---'`    
                             `---'                             
                                                                 
                                            |                    
,   .,---..   .,---.    ,---..   .,---.,---.|---.,---.,---.,---. 
|   ||   ||   ||        |   ||   ||    |    |   |,---|`---.|---' 
`---|`---'`---'`        |---'`---'`    `---'`   '`---^`---'`---'o
`---'                   |                                                                                              
                                                   ''')
   
    cursor.close()
    cnx.close()
