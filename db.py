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
        self.choose = " "
        self.mytransaction = " "
        self.withdrawmoney = ""
        self.balance = " "
        self.menu()

    def menu(self):
        print("""YOU ARE WELCOME TO PAULOW BANK\n1. Registration\n2. Transaction\n3. Quit""")
        self.choose = input("Enter any number of your choose>>>>")
        if self.choose.strip()=="1":
            self.registration()
        elif self.choose == "2":
            # self.transaction()
            # self.myusername()
            self.findusername()
        else:
            sys.exit() 
    def myusername(self):
        query ="INSERT INTO  transactiongoing (user_name,withdraw,balance) VALUES(%s, %s, %s)"
        value =(self.userUsername,self.withdrawmoney,self.balance)
        mycursor.execute(query,value)
        mysql.commit()        
        
    ############# THIS SHOWS THE REGISTRATION FUNCTION #######################
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
        self.myusername()

    ################ SHOW ACCOUNT NUMBER AND PIN BEFORE PERFORMING TRANSACTION ######################        
    def findusername(self):
        self.checkuseraccountnumber = input("Enter your account number>>")
        self.checkPin = input("Enter your Pin here>>")
        query = "SELECT  * FROM userinfo WHERE account_number=%s AND pin=%s "
        value = (self.checkuseraccountnumber,self.checkPin)
        mycursor.execute(query, value)
        myreg= mycursor.fetchall()
        print(myreg)
        if myreg != []:  
            print("""WELCOME TO PAUL BANK\n1. Withdraw\n2. check your account balance\n3. Transfer""")
            self.mytransaction = input("Enter any number to perform your transaction>> ") 
            if self.mytransaction == "1":
                self.withdrawing()
            elif self.mytransaction == "2":
                self.balancing()
            elif self.mytransaction == "3":
                self.tranfermoney()
            else:
                pass
        else:
            print("you don't have an account, you have to register ")
            self.dontHaveAccRegister()
            

    def dontHaveAccRegister(self):
        didYouwantreg = input("Did you want to do registration?  ")  
        if didYouwantreg.lower().strip() == "yes":
            self.registration()
        else:
            sys.exit()
    

    def tranfermoney(self):
        self.iwantotranfermoney =int(input("How much did you want to tranfer?>> "))
        query = ("UPDATE transactiongoing  SET  balance =%s WHERE balance =%s")
        # query = ("INSERT INTO transactiongoing WHERE balance =%s")
        value =(self.iwantotranfermoney,self.iwantotranfermoney)
        mycursor.execute(query,value)
        mysql.commit()
            

   
    ################ TRANSACTION FUNCTION STAT FROM HERE######################
    
    # def transaction(self):
    #     # self.findusername() 
    #     if myreg != "":  
    #         print("""WELCOME TO PAUL BANK\n1. Withdraw\n2. check your account balance\n3. Transfer""")
    #         self.mytransaction = input("Enter any number to perform your transaction>> ") 
    #         if self.mytransaction == "1":
    #             pass
    #         elif self.mytransaction == "2":
    #             pass
    #         elif self.mytransaction == "3":
    #             pass
    #         else:
    #             pass
    #     else:
    #         print("you don't have an account ")
    
    def withdrawing(self):
        self.withdrawmoney = float(input("Enter the amount you want to withdraw>> "))
        query = ("UPDATE transactiongoing SET balance = %s WHERE balance = %s")
        value = (self.withdrawmoney,self.withdrawmoney)
        mycursor.execute(query, value)
        mysql.commit()
        print(self.withdrawmoney )
        print(mycursor.rowcount, 'record updated successfuly')
    

    def balancing(self):
        query = "SELECT balance =%s FROM transactiongoing WHERE balance=%s"
        value = (self.balance,self.balance)
        mycursor.execute(query,value)
        myreg = mycursor.fetchone()
        print(self.balance)
        




app = Bankapp()
# app.registration()
# app.admin()
# app.menu()




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
    # sql = "DROP TABLE userinfo"
    # mycursor.execute(sql)


    

# menu()

