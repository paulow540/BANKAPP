# from random import seed
import random 
# import numpy
import mysql.connector as sql

mysql = sql.connect(host = '127.0.0.1', user= 'root', passwd = '', database='paul_db')

mycursor = mysql.cursor()


class Bankapp:
    def __init__(self):
        self.name = "paul"
       


    def registration(self):
        self.userfirstName = input("What is your first Name? ")
        self.usersecondName = input("What is your second Name? ")
        self.userUsername = self.userfirstName+ " "+ self.usersecondName
        self.userPin = int(input("Enter your pin "))
        self.accountNumber = random.randint(6470351928,8271490653)
        print(self.accountNumber)
        query ="INSERT INTO userinfo (first_name,second_name,user_name,pin,account_number) VALUES(%s, %s, %s, %s,%s)"
        # self.accountNumber= " "
        value =(self.userfirstName,self.usersecondName,self.userUsername,self.userPin,self.accountNumber)
        mycursor.execute(query,value)
        mysql.commit()
        print(mycursor.rowcount, "records inserted successfully")
        # admin()
       
      
        
    def admin(self):
        query =  "SELECT * FROM userinfo WHERE account_number=%s ,user_name=%s "
        value =(self.accountNumber,self.userUsername)
        mycursor.execute(query, value)
        print(mycursor)
        # myreg = mycursor.fetchall()
        # print(myreg)

        




app = Bankapp()
app.registration()
app.admin()
        
    

