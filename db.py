# from random import seed
import random 
import os
import sys
# import numpy
import mysql.connector as sql

mysql = sql.connect(host = '127.0.0.1', user= 'root', passwd = '', database='paul_db')

mycursor = mysql.cursor()


class Bankapp:
    def __init__(self):
        self.name = "paul" 
        # menu()   

    def menu(self):
        print("""YOU ARE WELCOME TO PAULOW BANK\n1. Registration\n2. Transaction\n3. Quit""")
        self.choose = input("Enter any number of your choose>>>>")
        if self.choose.strip()=="1":
            self.registration()
        elif self.choose ==2:
            pass
        else:
            sys.exit()         
        
    def registration(self):
        self.userfirstName = input("What is your first Name? ")
        self.usersecondName = input("What is your second Name? ")
        self.userUsername = self.userfirstName+ " "+ self.usersecondName
        self.userPin = int(input("Enter your pin "))
        self.account = str(random.random())
        self.accountNumber =self.account[8:]
        print(self.accountNumber)
        query ="INSERT INTO userinfo (first_name,second_name,user_name,pin,account_number) VALUES(%s, %s, %s, %s,%s)"
        # self.accountNumber= " "
        value =(self.userfirstName,self.usersecondName,self.userUsername,self.userPin,self.accountNumber)
        mycursor.execute(query,value)
        mysql.commit()
        print(mycursor.rowcount, "records inserted successfully")
        self.admin()
       
      
        
    def admin(self):
        query =  "SELECT * FROM userinfo WHERE account_number=%s ,user_name=%s "
        value =(self.accountNumber,self.userUsername)
        mycursor.execute(query, value)
        print(mycursor)
        myreg = mycursor.fetchall()
        print(myreg)

        




app = Bankapp()
# app.registration()
# app.admin()
app.menu()




# ##################################################################################
        
# def menu():
#     print("""YOU ARE WELCOME TO PAULOW BANK\n1. Registration\n2. Transaction\n3. Quit""")
#     choose = input("Enter any number of your choose>>>>")
#     if choose.strip()=="1":
#         registration()
#     elif choose =="2":
#         admin()
#     else:
#         sys.exit()         
        
# def registration():
#     userfirstName = input("What is your first Name? ")
#     usersecondName = input("What is your second Name? ")
#     userUsername = userfirstName+ " "+ usersecondName
#     userPin = int(input("Enter your pin "))
#     account = str(random.random())
#     accountNumber =account[8:]
#     print(accountNumber)
#     query ="INSERT INTO userinfo (first_name,second_name,user_name,pin,account_number) VALUES(%s, %s, %s, %s,%s)"
#     # accountNumber= " "
#     value =(userfirstName,usersecondName,userUsername,userPin,accountNumber)
#     mycursor.execute(query,value)
#     mysql.commit()
#     print(mycursor.rowcount, "records inserted successfully")
#     # admin()
    
    
    
# def admin():
#     # query =  "SELECT * FROM userinfo WHERE account_number=%s ,user_name=%s "
#     # value =(accountNumber,userUsername)
#     # mycursor.execute(query, value)
#     # print(mycursor)
#     # myreg = mycursor.fetchall()
#     # print(myreg)
#     sql = "DROP TABLE userinfo"
#     mycursor.execute(sql)


    

# menu()

