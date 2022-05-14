from time import time
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql
import mysql.connector
from PIL import ImageTk,Image
import re

from tkintermapview import TkinterMapView


def change_frame():
    regisframe.forget()
    loginframe.pack(expand=True,padx=30,pady=30)



def Add():
    first_name= firstnameEntry.get()
    last_name = lasttnameEntry.get()
    age = ageEntry.get()
    city = cityEntry.get()
    adde = addeEntry.get()
    phone = phoneEntry.get()
    mail = mailEntry.get()
    user_name = usernameEntry.get()
    password = passwordEntry.get()
    matched = re.match("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}",mailEntry.get())
    is_match = bool(matched)
    namematch = re.match("[A-Za-z]",firstnameEntry.get())
    is_namematch = bool(namematch)
    lastnamematch = re.match("[A-Za-z]",lasttnameEntry.get())
    is_lastnamematch = bool(lastnamematch)
    ageint = int(age)



    print(is_match)


    if(firstnameEntry.get() == "" or lasttnameEntry.get() == "" or ageEntry.get() == "" or cityEntry.get() == "" or addeEntry.get() == "" or phoneEntry.get() == "" or mailEntry.get() == "" or usernameEntry.get() == "" or passwordEntry.get() == ""):
        messagebox.showinfo("Information","Please fill in all the details!")
    elif(len(firstnameEntry.get()) < 2 or len(firstnameEntry.get()) > 15 or  is_namematch == False):
        messagebox.showinfo("Information","Please enter a valid first name")
    elif(len(lasttnameEntry.get()) < 1 or len(lasttnameEntry.get()) > 15 or is_lastnamematch == False):
        messagebox.showinfo("Information","Please enter a valid first name")
    elif(len(phoneEntry.get()) != 10):
        messagebox.showinfo("Information","Please enter a valid phone number")
    elif (is_match == False):
        messagebox.showinfo("Information","Please enter a valid E-mail ID")
    elif(ageint <  18):
        messagebox.showinfo("Information","Please enter a proper age")
    elif(len(usernameEntry.get()<6)):
        messagebox.showinfo("Information","Username must atleat 6 characters")
    elif(len(passwordEntry.get()) < 6):
        messagebox.showinfo("Information","Password must be atleast 6 characters long!")
    
    


    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="cabapp",auth_plugin='mysql_native_password')
        mycursor = mysqldb.cursor()


        try:
            sql = "INSERT INTO  user_information (first_name,last_name,age,city,adde,phone,user_name,password) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)"
            val = (first_name,last_name,age,city,adde,phone,user_name,password)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("Information", "User Registered successfully...")
            firstnameEntry.delete(0, END)
            lasttnameEntry.delete(0, END)
            ageEntry.delete(0, END)
            cityEntry.delete(0, END)
            addeEntry.delete(0 , END)
            phoneEntry.delete(0, END)
            mailEntry.delete(0,END)
            usernameEntry.delete(0,END)
            passwordEntry.delete(0,END)
            firstnameEntry.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

def driver_Add():
    first_name= driverfirstnameEntry.get()
    last_name = driverlasttnameEntry.get()
    age = driverageEntry.get()
    city = drivercityEntry.get()
    adde = driveraddeEntry.get()
    driver_phone = driverphoneEntry.get()
    car_type = drivercartypeentry.get()
    user_name = driverusernameEntry.get()
    password = driverpasswordEntry.get()

    status = "Offline"
    namematch = re.match("[A-Za-z]",driverfirstnameEntry.get())
    is_namematch = bool(namematch)
    lastnamematch = re.match("[A-Za-z]",driverlasttnameEntry.get())
    is_lastnamematch = bool(lastnamematch)
    ageint = int(age)
    str = "Micro,MICRO,micro,Sedan,SEDAN,sedan,SUV,suv,Suv"
    carmatch = (car_type in str)
    


    if(driverfirstnameEntry.get() == "" or driverlasttnameEntry.get() == "" or driverageEntry.get() == "" or drivercityEntry.get() == "" or driveraddeEntry.get() == "" or driverphoneEntry.get() == ""  or drivercartypeentry.get() == "" or driverusernameEntry.get() == "" or driverpasswordEntry.get() == ""):
        messagebox.showinfo("Information","Please enter all the details!")
    elif(len(first_name) < 2 or len(first_name) > 15 or is_namematch == False):
        messagebox.showinfo("Information","Please enter a proper first name")
    elif(len(last_name)<1 or len(last_name)>15 or is_lastnamematch == False):
        messagebox.showinfo("Information","Please enter a proper last name")
    elif(len(driverphoneEntry.get()) != 10 ):
        messagebox.showinfo("Information","Please enter a valid phone number")
    elif(ageint <  18):
        messagebox.showinfo("Information","Please enter a proper age")
    elif(carmatch == False):
        messagebox.showinfo("Information","Please enter a valid car type [Micro,Sedan,SUV]")
    elif(len(driverusernameEntry.get())<6):
        messagebox.showinfo("Information","Username must atleat 6 characters")
    elif(len(driverpasswordEntry.get()) < 6):
        messagebox.showinfo("Information","Password must be atleast 6 characters long!")



    else:

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="cabapp",auth_plugin='mysql_native_password')
        mycursor = mysqldb.cursor()

        try:
            sql = "INSERT INTO  driver_info (driver_first_name,driver_last_name,driver_age,driver_city,driver_adde,driver_phone,driver_car_type,driver_username,driver_password) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"
            val = (first_name,last_name,age,city,adde,driver_phone,car_type,user_name,password)
            sql1 = "INSERT INTO driver_status (driver_user_name,driver_car_type,driver_status_now) VALUES (%s,%s,%s)"
            val1 = (user_name,car_type,status)
            mycursor.execute(sql, val)
            mycursor.execute(sql1,val1)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Driver inserted successfully...")
            driverfirstnameEntry.delete(0, END)
            driverlasttnameEntry.delete(0, END)
            driverageEntry.delete(0, END)
            drivercityEntry.delete(0, END)
            driveraddeEntry.delete(0 , END)
            driverphoneEntry.delete(0, END)
            drivercartypeentry.delete(0,END)
            driverusernameEntry.delete(0,END)
            driverpasswordEntry.delete(0,END)
            firstnameEntry.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()


def error_to_login():
    dashboardframe.forget()



def on_invalid(self):
    self.show_message('Please enter a valid email', 'red')

def edit_userdetails():

    username = usernameloginEntry.get()
    global usernamename
    usernamename = username
    print("global")
    print(usernamename)
    
    newuserfirstname = StringVar()
    newuserlastname = StringVar()
    newuserage = StringVar()
    newusercity = StringVar()
    newuseradd = StringVar()
    newusermob = StringVar()
    newuserpass = StringVar()
    if (username == ""):
        messagebox.showerror("Error", "Enter User Name And Password", parent=useredit)
    else:

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("select * from user_information where user_name = %s and password = %s",(usernameloginEntry.get(), passwordloginEntry.get()))
            row_set = cur.fetchall()
            print("HI")
            print(row_set[0][0])
            if(len(row_set) != 0):
                newuserfirstname.set(row_set[0][0])
                newuserlastname.set(row_set[0][1])
                newuserage.set(row_set[0][2])
                newusercity.set(row_set[0][3])
                newuseradd.set(row_set[0][4])
                newusermob.set(row_set[0][7])
                newuserpass.set(row_set[0][6])
                changefirstnameEntry.insert(0,row_set[0][0])
                changelasttnameEntry.insert(0,row_set[0][1])
                changeageEntry.insert(0,row_set[0][2])
                changecityEntry.insert(0,row_set[0][3])
                changeaddeEntry.insert(0,row_set[0][4])
                changephoneEntry.insert(0,row_set[0][7])
                changepasswordEntry.insert(0,row_set[0][6])
            saveandbackbutton = Button(useredit,text="Save and Logout ",command=change_details)
            saveandbackbutton.grid(row=9,column=0,pady=10,padx=20)
                
            

            dashboardframe.forget()
            useredit.pack(expand=True,padx=30,pady=30)




        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)





def change_details():
    global usernamename
    username = usernamename
    print("before")
    print(username)
    first_name= changefirstnameEntry.get()
    last_name = changelasttnameEntry.get()
    age = changeageEntry.get()
    city = changecityEntry.get()
    adde = changeaddeEntry.get()
    phone = changephoneEntry.get()
    password = changepasswordEntry.get()
    print("lastnameentry")
    print(lasttnameEntry.get())
    print("last_name")
    print(last_name)

    if (username == ""):
        messagebox.showerror("Error", "Enter User Name And Password", parent = useredit)
    else:

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            print("Now ")
            print(username)
            sql1 = "UPDATE user_information set first_name = %s , last_name = %s , age = %s , city = %s  ,adde = %s , password = %s , phone = %s WHERE user_name = %s"
            val1 = (first_name,last_name,age,city,adde,phone,password,username)
            cur.execute(sql1,val1)
            cur.execute("UPDATE user_information set last_name = %s WHERE user_name = %s",(changelasttnameEntry.get(),username))
            messagebox.showinfo("information", "Details changed successfully...")
            con.commit()
            changefirstnameEntry.delete(0,END)
            changelasttnameEntry.delete(0,END)
            changeageEntry.delete(0,END)
            changecityEntry.delete(0,END)
            changeaddeEntry.delete(0,END)
            changephoneEntry.delete(0,END)
            changepasswordEntry.delete(0,END)
            useredit.forget()
            loginframe.pack(expand=True,padx=10,pady=10)

        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)
        


def change_to_dashboard():

    username = usernameloginEntry.get()
    password = passwordloginEntry.get()
    print(usernameloginEntry.get())
    print(passwordloginEntry.get())
    global globalname
    global globalusername
    userlastridesdriverusername = StringVar()
    userlastridespickuploc = StringVar()
    userlastridesdroploc = StringVar()
    userlastridesbookingid = StringVar()
    userlastridesbookingid.set("")
    print(userlastridesbookingid)
    userlastridesamount = StringVar()
    userlastridesbookingid1 = StringVar()
    userlastridesbookingid2 = StringVar()
    userlastridesbookingid3 = StringVar()
    userlastridesdriverusername1 = StringVar()
    userlastridesdriverusername2 = StringVar()
    userlastridesdriverusername3 = StringVar()
    userlastridespickuploc1 = StringVar()
    userlastridespickuploc2 = StringVar()
    userlastridespickuploc3 = StringVar()
    userlastridesdroploc1 = StringVar()
    userlastridesdroploc2 = StringVar()
    userlastridesdroploc3 = StringVar()
    userlastridesamount1 = StringVar()
    userlastridesamount2 = StringVar()
    userlastridesamount3 = StringVar()

    if (username == ""):
        messagebox.showerror("Error", "Enter User Name And Password", parent=driverdashboard)
    else:

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            sql12 = "select * from user_information where user_name = %s and password = %s"
            val12 = (username,password)
            cur.execute(sql12,val12)
            row_set = cur.fetchall()
            print("Here")
            print(username)
            print(password)
            print(row_set)
            
            if(len(row_set) != 0):
                userphone = row_set[0][5]
                print(userphone)
                cur.execute("select * from hired_cab where username = %s and userphone = %s order by booking_id desc limit 3",(usernameloginEntry.get(), userphone))
                row_set2 = cur.fetchall()
                print(len(row_set2))


                if (len(row_set2) == 3):
                    userlastridesbookingid.set("Booking ID")
                    print(userlastridesbookingid)
                    userlastridesbookingid.set("Booking ID")
                    print(userlastridesbookingid)
                    userlastridesdriverusername.set("User username")
                    userlastridespickuploc.set("Pickup")
                    userlastridesdroploc.set("Drop")
                    userlastridesamount.set("Amount")
                    userlastridesdriverusername1.set(row_set2[0][1])
                    userlastridesdriverusername2.set(row_set2[1][1])
                    userlastridesdriverusername3.set(row_set2[2][1])
                    userlastridespickuploc1.set(row_set2[0][3])
                    userlastridespickuploc2.set(row_set2[1][3])
                    userlastridespickuploc3.set(row_set2[2][3])
                    userlastridesdroploc1.set(row_set2[0][4])
                    userlastridesdroploc2.set(row_set2[1][4])
                    userlastridesdroploc3.set(row_set2[2][4])
                    userlastridesamount1.set(row_set2[0][7])
                    userlastridesamount2.set(row_set2[1][7])
                    userlastridesamount3.set(row_set2[2][7])
                    userlastridesbookingid1.set(row_set2[0][6])
                    userlastridesbookingid2.set(row_set2[1][6])
                    userlastridesbookingid3.set(row_set2[2][6])
                    print(123)

                else:
                    userlastridesbookingid.set("")
                    userlastridesdriverusername.set("")
                    userlastridespickuploc.set("")
                    userlastridesdroploc.set("")
                    userlastridesamount.set("")
                    userlastridesdriverusername1.set("")
                    userlastridesdriverusername2.set("")
                    userlastridesdriverusername3.set("")
                    userlastridespickuploc1.set("")
                    userlastridespickuploc2.set("")
                    userlastridespickuploc3.set("")
                    userlastridesdroploc1.set("")
                    userlastridesdroploc2.set("")
                    userlastridesdroploc3.set("")
                    userlastridesbookingid1.set("")
                    userlastridesbookingid2.set("")
                    userlastridesbookingid3.set("")
                    userlastridesamount1.set("")
                    userlastridesamount2.set("")
                    userlastridesamount3.set("")



                con.commit()
                print(userlastridesamount)

                globalusername = username
                globalname = row_set[0][0]
                print(456)
                user_namelabel = Label(dashboardframe, text="Name")
                user_namelabel.grid(row=1, column=0,pady=10,padx=20)
                user_namevalue = StringVar()
                user_namevalue.set(row_set[0][0])
                user_namevaluelabel = Label(dashboardframe, textvariable=user_namevalue)
                user_namevaluelabel.grid(row=1, column=1,pady=10,padx=20)
                user_usernamelabel = Label(dashboardframe, text="Username")
                user_usernamelabel.grid(row=2, column=0,pady=10,padx=20)
                user_usernamevalue = StringVar()
                user_usernamevalue.set(row_set[0][5])
                user_usernamevaluelabel = Label(dashboardframe, textvariable=user_usernamevalue)
                user_usernamevaluelabel.grid(row=2, column=1,pady=10,padx=20)
                testinglabel = Label(dashboardframe, text="Dashboard", padx=10, pady=10)
                testinglabel.grid(row=0, column=0,pady=10,padx=20)
                usercabhirebutton = Button(dashboardframe, text="Hire a cab", command=change_to_hire_a_cab)
                usercabhirebutton.grid(row=4, column=0,pady=10,padx=20)
                usercancelcurrentbooking = Button(dashboardframe, text="Cancel current Ride",
                                                    command=change_to_user_cancel_frame)
                usercancelcurrentbooking.grid(row=4, column=1,pady=10,padx=20)
                userdashboardlogoutbutton = Button(dashboardframe, text="Log Out",
                                                     command=userdashboard_to_main)
                userdashboardlogoutbutton.grid(row=4, column=2, pady=10, padx=20)
                userdetailseditbutton =  Button(dashboardframe,text="Edit Account",command=edit_userdetails)
                userdetailseditbutton.grid(row=4,column=3,padx=10,pady=10)

                userlastridesbookingidlabel = Label(dashboardframe, textvariable=userlastridesbookingid)
                userlastridesdriverusernamelabel = Label(dashboardframe, textvariable=userlastridesdriverusername)
                userlastridespickuploclabel = Label(dashboardframe, textvariable=userlastridespickuploc)
                userlastridesdroploclabel = Label(dashboardframe, textvariable=userlastridesdroploc)
                userlastridesamountlabel = Label(dashboardframe, textvariable=userlastridesamount)
                userlastridesbookingidlabel.grid(row=10, column=0)
                userlastridesdriverusernamelabel.grid(row=10, column=1)
                userlastridespickuploclabel.grid(row=10, column=2)
                userlastridesdroploclabel.grid(row=10, column=3)
                userlastridesamountlabel.grid(row=10, column=4)
                userlastridesbookingid1label = Label(dashboardframe, textvariable=userlastridesbookingid1)
                userlastridesbookingid2label = Label(dashboardframe, textvariable=userlastridesbookingid2)
                userlastridesbookingid3label = Label(dashboardframe, textvariable=userlastridesbookingid3)
                userlastridesdriverusername1label = Label(dashboardframe, textvariable=userlastridesdriverusername1)
                userlastridesdriverusername2label = Label(dashboardframe, textvariable=userlastridesdriverusername2)
                userlastridesdriverusername3label = Label(dashboardframe, textvariable=userlastridesdriverusername3)
                userlastridespickuploc1label = Label(dashboardframe, textvariable=userlastridespickuploc1)
                userlastridespickuploc2label = Label(dashboardframe, textvariable=userlastridespickuploc2)
                userlastridespickuploc3label = Label(dashboardframe, textvariable=userlastridespickuploc3)
                userlastridesdroploc1label = Label(dashboardframe, textvariable=userlastridesdroploc1)
                userlastridesdroploc2label = Label(dashboardframe, textvariable=userlastridesdroploc2)
                userlastridesdroploc3label = Label(dashboardframe, textvariable=userlastridesdroploc3)
                userlastridesamount1label = Label(dashboardframe, textvariable=userlastridesamount1)
                userlastridesamount2label = Label(dashboardframe, textvariable=userlastridesamount2)
                userlastridesamount3label = Label(dashboardframe, textvariable=userlastridesamount3)
                userlastridesbookingid1label.grid(row=11, column=0)
                userlastridesbookingid2label.grid(row=12, column=0)
                userlastridesbookingid3label.grid(row=13, column=0)
                userlastridesdriverusername1label.grid(row=11, column=1)
                userlastridesdriverusername2label.grid(row=12, column=1)
                userlastridesdriverusername3label.grid(row=13, column=1)
                userlastridespickuploc1label.grid(row=11, column=2)
                userlastridespickuploc2label.grid(row=12, column=2)
                userlastridespickuploc3label.grid(row=13, column=2)
                userlastridesdroploc1label.grid(row=11, column=3)
                userlastridesdroploc2label.grid(row=12, column=3)
                userlastridesdroploc3label.grid(row=13, column=3)
                userlastridesamount1label.grid(row=11, column=4)
                userlastridesamount2label.grid(row=12, column=4)
                userlastridesamount3label.grid(row=13, column=4)


                ifcancelledbydriver = StringVar()
                if(globaldrivercancelvalue == 1):
                    ifcancelledbydriver.set("Sorry !, Your Driver had cancelled the ride. You can try to book again")
                else:
                    ifcancelledbydriver.set("")
                ifcancelledlabel = Label(dashboardframe,textvariable=ifcancelledbydriver)
                ifcancelledlabel.grid(row=14,column=0)
                loginframe.forget()
                dashboardframe.pack(expand=True,padx=30,pady=30)

            else:
                messagebox.showinfo("Not Found","Username/Password Incorrect")
                usernameloginEntry.delete(0,END)
                passwordloginEntry.delete(0,END)

        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=dashboardframe)



def change_frame_to_user_login():
    parentframe.forget()
    regisframe.pack(expand=True,padx=30,pady=30)

def change_frame_to_driver_regis():
    parentframe.forget()
    driverregisframe.pack(expand=True,padx=30,pady=30)

def driver_change_frame_to_dashboard():
    driverregisframe.forget()
    driverdashboard.pack(expand=True,padx=30,pady=30)

def driver_change_frame_to_login():
    driverregisframe.forget()
    driverloginframe.pack(expand=True,padx=30,pady=30)

def change_to_driver_dashboard():


    driver_username = driverusernameloginEntry.get()
    global globaldrivername
    global globaldrivercartype
    global globaldriverusername
    driverlastridesusername = StringVar()
    driverlastridespickuploc = StringVar()
    driverlastridesdroploc = StringVar()
    driverlastridesbookingid = StringVar()
    driverlastridesamount = StringVar()
    driverlastridesbookingid1 = StringVar()
    driverlastridesbookingid2 = StringVar()
    driverlastridesbookingid3 = StringVar()
    driverlastridesusername1 = StringVar()
    driverlastridesusername2 = StringVar()
    driverlastridesusername3 = StringVar()
    driverlastridespickuploc1 = StringVar()
    driverlastridespickuploc2 = StringVar()
    driverlastridespickuploc3 = StringVar()
    driverlastridesdroploc1 = StringVar()
    driverlastridesdroploc2 = StringVar()
    driverlastridesdroploc3 = StringVar()
    driverlastridesamount1 = StringVar()
    driverlastridesamount2 = StringVar()
    driverlastridesamount3 = StringVar()


    if(driver_username == ""):
        messagebox.showerror("Error", "Enter User Name And Password", parent=driverdashboard)
    else:

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("select * from driver_info where driver_username = %s and driver_password = %s",(driver_username, driverpasswordloginEntry.get()))
            row_set = cur.fetchall()
            if(len(row_set) != 0):
                for row in row_set:
                    cartype = row[6]
                    print(cartype)
                cur.execute("select * from hired_cab where driver_user_name = %s and cartype = %s order by booking_id desc limit 3",(driver_username,cartype))
                row_set2 = cur.fetchall()

                if(len(row_set2) == 3):
                    driverlastridesbookingid.set("Booking ID")
                    driverlastridesusername.set("User username")
                    driverlastridespickuploc.set("Pickup")
                    driverlastridesdroploc.set("Drop")
                    driverlastridesamount.set("Amount")
                    driverlastridesusername1.set(row_set2[0][0])
                    driverlastridesusername2.set(row_set2[1][0])
                    driverlastridesusername3.set(row_set2[2][0])
                    driverlastridespickuploc1.set(row_set2[0][3])
                    driverlastridespickuploc2.set(row_set2[1][3])
                    driverlastridespickuploc3.set(row_set2[2][3])
                    driverlastridesdroploc1.set(row_set2[0][4])
                    driverlastridesdroploc2.set(row_set2[1][4])
                    driverlastridesdroploc3.set(row_set2[2][4])
                    driverlastridesamount1.set(row_set2[0][7])
                    driverlastridesamount2.set(row_set2[1][7])
                    driverlastridesamount3.set(row_set2[2][7])
                    driverlastridesbookingid1.set(row_set2[0][6])
                    driverlastridesbookingid2.set(row_set2[1][6])
                    driverlastridesbookingid3.set(row_set2[2][6])

                else:
                    driverlastridesbookingid.set("")
                    driverlastridesusername.set("")
                    driverlastridespickuploc.set("")
                    driverlastridesdroploc.set("")
                    driverlastridesamount.set("")
                    driverlastridesusername1.set("")
                    driverlastridesusername2.set("")
                    driverlastridesusername3.set("")
                    driverlastridespickuploc1.set("")
                    driverlastridespickuploc2.set("")
                    driverlastridespickuploc3.set("")
                    driverlastridesdroploc1.set("")
                    driverlastridesdroploc2.set("")
                    driverlastridesdroploc3.set("")
                    driverlastridesbookingid1.set("")
                    driverlastridesbookingid2.set("")
                    driverlastridesbookingid3.set("")
                    driverlastridesamount1.set("")
                    driverlastridesamount2.set("")
                    driverlastridesamount3.set("")
                for row in row_set:
                    globaldriverusername = driver_username
                    globaldrivername = row[0]
                    globaldrivercartype = row[6]
                    driver_namelabel = Label(driverdashboard, text="Name :")
                    driver_namelabel.grid(row=1, column=0,pady=10,padx=20)
                    drive_namevalue = StringVar()
                    drive_namevalue.set(row[0])
                    drive_namevaluelabel = Label(driverdashboard, textvariable=drive_namevalue)
                    drive_namevaluelabel.grid(row=1, column=1,pady=10,padx=20)
                    driver_usernamelabel = Label(driverdashboard, text="Username :")
                    driver_usernamelabel.grid(row=1, column=3,pady=10,padx=20)
                    drive_usernamevalue = StringVar()
                    drive_usernamevalue.set(driver_username)
                    drive_usernamevaluelabel = Label(driverdashboard, textvariable=drive_usernamevalue)
                    drive_usernamevaluelabel.grid(row=1, column=4,pady=10,padx=20)
                    driver_cartypenamelabel = Label(driverdashboard, text="Car Type :")
                    driver_cartypenamelabel.grid(row=3, column=0,pady=10,padx=20)
                    drive_cartypenamevalue = StringVar()
                    drive_cartypenamevalue.set(row[6])
                    drive_cartypenamevaluelabel = Label(driverdashboard, textvariable=drive_cartypenamevalue)
                    drive_cartypenamevaluelabel.grid(row=3, column=1,pady=10,padx=20)
                    set_status_menu = OptionMenu(driverdashboard, status_clicked, "Available", "Hired", "Offline",
                                                 command=change_status_of_driver)
                    set_status_menu.config(width=25)
                    set_status_menu.grid(row=3, column=4,pady=10,padx=20)
                    getlastthreebutton = Button(driverdashboard,text="View last 3 rides",command=show_driver_last_three(driver_username,row[5]))
                    getlastthreebutton.grid(row=6,column=0,pady=10,padx=20)
                    drivercancelcurrentbooking = Button(driverdashboard, text="Cancel current Ride",command=change_to_driver_cancel_frame)
                    drivercancelcurrentbooking.grid(row=6, column=1,pady=10,padx=20)
                    driverdashboardlogoutbutton = Button(driverdashboard, text="Log Out",
                                                command=driverdashboard_to_main)
                    driverdashboardlogoutbutton.grid(row=6, column=2, pady=10, padx=20)
                    driverdashboardfinishbutton = Button(driverdashboard,text="Ride Completed",command = driver_ride_completed)
                    driverdashboardfinishbutton.grid(row=6,column=3,padx=10,pady=20)
                    drivertotal = Label(driverdashboard,text="This Week total amount : ")
                    drivertotal.grid(row=8,column=0)
                    driver_username = driverusernameforentry.get()
                    driverweektotal = StringVar()
                    driverweektotal .set(row[9])

                    driverweektotallabel  = Label(driverdashboard,textvariable=driverweektotal)
                    driverweektotallabel.grid(row=8,column=1)

                    driverlastridesbookingidlabel = Label(driverdashboard,textvariable=driverlastridesbookingid)
                    driverlastridesusernamelabel = Label(driverdashboard,textvariable=driverlastridesusername)
                    driverlastridespickuploclabel = Label(driverdashboard,textvariable=driverlastridespickuploc)
                    driverlastridesdroploclabel = Label(driverdashboard,textvariable=driverlastridesdroploc)
                    driverlastridesamountlabel = Label(driverdashboard,textvariable=driverlastridesamount)
                    driverlastridesbookingidlabel.grid(row=10,column=0)
                    driverlastridesusernamelabel.grid(row=10,column=1)
                    driverlastridespickuploclabel.grid(row=10,column=2)
                    driverlastridesdroploclabel.grid(row=10,column=3)
                    driverlastridesamountlabel.grid(row=10,column=4)
                    driverlastridesbookingid1label = Label(driverdashboard,textvariable=driverlastridesbookingid1)
                    driverlastridesbookingid2label = Label(driverdashboard, textvariable=driverlastridesbookingid2)
                    driverlastridesbookingid3label = Label(driverdashboard, textvariable=driverlastridesbookingid3)
                    driverlastridesusername1label = Label(driverdashboard,textvariable=driverlastridesusername1)
                    driverlastridesusername2label = Label(driverdashboard, textvariable=driverlastridesusername2)
                    driverlastridesusername3label = Label(driverdashboard, textvariable=driverlastridesusername3)
                    driverlastridespickuploc1label = Label(driverdashboard,textvariable=driverlastridespickuploc1)
                    driverlastridespickuploc2label = Label(driverdashboard, textvariable=driverlastridespickuploc2)
                    driverlastridespickuploc3label = Label(driverdashboard, textvariable=driverlastridespickuploc3)
                    driverlastridesdroploc1label = Label(driverdashboard,textvariable=driverlastridesdroploc1)
                    driverlastridesdroploc2label = Label(driverdashboard, textvariable=driverlastridesdroploc2)
                    driverlastridesdroploc3label = Label(driverdashboard, textvariable=driverlastridesdroploc3)
                    driverlastridesamount1label = Label(driverdashboard,textvariable=driverlastridesamount1)
                    driverlastridesamount2label = Label(driverdashboard, textvariable=driverlastridesamount2)
                    driverlastridesamount3label = Label(driverdashboard, textvariable=driverlastridesamount3)
                    driverlastridesbookingid1label.grid(row=11,column=0)
                    driverlastridesbookingid2label.grid(row=12, column=0)
                    driverlastridesbookingid3label.grid(row=13, column=0)
                    driverlastridesusername1label.grid(row=11,column=1)
                    driverlastridesusername2label.grid(row=12, column=1)
                    driverlastridesusername3label.grid(row=13, column=1)
                    driverlastridespickuploc1label.grid(row=11,column=2)
                    driverlastridespickuploc2label.grid(row=12, column=2)
                    driverlastridespickuploc3label.grid(row=13, column=2)
                    driverlastridesdroploc1label.grid(row=11,column=3)
                    driverlastridesdroploc2label.grid(row=12, column=3)
                    driverlastridesdroploc3label.grid(row=13, column=3)
                    driverlastridesamount1label.grid(row=11,column=4)
                    driverlastridesamount2label.grid(row=12, column=4)
                    driverlastridesamount3label.grid(row=13, column=4)


                    ifcancelledbyuser = StringVar()
                    if (globalusercancelvalue == 1):
                        ifcancelledbyuser.set("Sorry !, Your Driver had cancelled the ride. You can try to book again")
                    else:
                        ifcancelledbyuser.set("")
                    ifcancelleddriverlabel = Label(driverdashboard, textvariable=ifcancelledbyuser)
                    ifcancelleddriverlabel.grid(row=15, column=0)
                driverloginframe.forget()
                driverdashboard.pack(expand=True, padx=30, pady=30)
            else:
                messagebox.showinfo("Not Found","User/Password is incorrect")
                driverusernameloginEntry.delete(0,END)
                driverpasswordloginEntry.delete(0,END)



        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)



def driver_ride_completed():
    try:
        driver_username = driverusernameloginEntry.get()
        status_now = "Hired"
        con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                  auth_plugin='mysql_native_password')
        cur = con.cursor()
        cur.execute("select * from hired_cab where driver_user_name = %s and status = %s",(driver_username, status_now))
        row_set = cur.fetchall()
        if(len(row_set) != 0):
            username = row_set[0][0]
            status_after = "Done"
            status_after_driver = "Available"
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(status_after_driver,driver_username))
            cur.execute("UPDATE hired_cab set status = %s WHERE driver_user_name = %s and username = %s",(status_after,driver_username,username))
            con.commit()
            con.close()
            messagebox.showinfo("information", "Ride Completed Succesfully")
        else:
            messagebox.showinfo("information", "You currently do not have any ongoing ride")

    except Exception as es:
        messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)


def show_driver_last_three(driver_username,driver_cartype):
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                      auth_plugin='mysql_native_password')
        cur = con.cursor()
        cur.execute("select * from hired_cab where driver_user_name = %s and cartype = %s",(driver_username, driver_cartype))
        row_set = cur.fetchall()
        print(row_set)






    except Exception as es:
        messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)
def change_to_driver_cancel_frame():
    driverdashboard.forget()

    drivercancelframe.pack(expand=True,padx=30,pady=30)

def change_to_user_cancel_frame():
    dashboardframe.forget()

    usercancelframe.pack(expand=True,padx=30,pady=30)


def Ok():
    driver_username = driverusernameforentry.get()
    try:

        con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                      auth_plugin='mysql_native_password')
        cur = con.cursor()
        hirestatus  = "Hired"
        cancelstatus = "Cancelled"

        cur.execute("SELECT * FROM hired_cab where status = %s  and driver_user_name = %s",(hirestatus,driver_username))
        row_set = cur.fetchone()

        if(row_set == None ):
            messagebox.showinfo("Error","Sorry!, But you don't have a booking to cancel")
        else:
            cur.execute("UPDATE hired_cab set status = %s WHERE driver_user_name = %s", (cancelstatus, driver_username))
            messagebox.showinfo("information", "Cancelled successfully...")
            global globaldrivercancelvalue
            globaldrivercancelvalue = 1
            change_to_dashboard_from_hiring()
            con.commit()
            con.close()

    except Exception as es:
        messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=drivercancelframe)
    drivercancelframe.forget()
    driverdashboard.pack(expand=True,padx=30,pady=30)

def userOk():
    username = userusernameforentry.get()
    try:

        con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                      auth_plugin='mysql_native_password')
        cur = con.cursor()
        hiredstatus = "Hired"
        cancelstatus = "Cancelled"
        now_status = "Available"
        cur.execute("SELECT * FROM hired_cab where status = %s  and username = %s",(hiredstatus, username))

        row_set = cur.fetchone()

        if(row_set == None ):
            messagebox.showinfo("Error","Sorry!, But you don't have a booking to cancel")
        else:
            driv_us = row_set[0][1]
            print(driv_us)
            cur.execute("UPDATE hired_cab set status = %s WHERE username = %s", (cancelstatus, username))
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(now_status,driv_us))
            messagebox.showinfo("information", "Cancelled successfully...")
            global globalusercancelvalue
            globalusercancelvalue = 1
            change_to_dashboard_from_hiring()
            con.commit()
            con.close()

    except Exception as es:
        messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=drivercancelframe)
    usercancelframe.forget()
    dashboardframe.pack(expand=True,padx=30,pady=30)

def change_to_dashboard_from_hiring():
    frame.forget()
    dashboardframe.pack(expand=True,padx=30,pady=30)

def radioclicked(value):
    global globalcartype
    if(value == 1):
        microprice.set("Rs.15")
        sedanprice.set("NA")
        suvprice.set("NA")
        numofpassengers.set("3")
        minbaseprice.set("30")
        globalcartype = "Micro"

    elif(value == 2):
        microprice.set("NA")
        sedanprice.set("Rs.25")
        suvprice.set("NA")
        numofpassengers.set("4")
        minbaseprice.set("45")
        globalcartype = "Sedan"

    elif(value == 3):
        microprice.set("NA")
        sedanprice.set("NA")
        suvprice.set("Rs.30")
        numofpassengers.set("6")
        minbaseprice.set("60")
        globalcartype = "SUV"

    return value

def checkboxclicked(value):
    global insuranceset
    if(value == 1):
        insuranceprice.set("Rs.10")
        insuranceset = 1
    else:
        insuranceprice.set("Rs.0")
        insuranceset = 0

def calcDistance(choice):
    picking = clicked.get()
    dropping = clicked1.get()
    maxDistance = 0
    global globalmaxdist
    if(picking == "Kannur"):
        if(dropping == "Thrissur"):
            maxDistance = 211
        elif(dropping == "Thiruvananthapuram"):
            maxDistance = 466
        elif (dropping == "Kollam"):
            maxDistance = 405
        elif (dropping == "Palakkad"):
            maxDistance = 213
        elif (dropping == "Kozhikode"):
            maxDistance = 90
        elif (dropping == "Kottayam"):
            maxDistance = 328
        elif (dropping == "Alappuzha"):
            maxDistance = 319
        elif (dropping == "Pathanamthitta"):
            maxDistance = 390
        elif (dropping == "Ernakulam"):
            maxDistance = 264
        elif (dropping == "Malappuram"):
            maxDistance = 136
        elif (dropping == "Idukki"):
            maxDistance = 358
        elif (dropping == "Wayanad"):
            maxDistance = 112

    elif(picking == "Thrissur"):
        if(dropping == "Kannur"):
            maxDistance = 211
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 276
        elif (dropping == "Kollam"):
            maxDistance = 215
        elif (dropping == "Palakkad"):
            maxDistance = 69
        elif (dropping == "Kozhikode"):
            maxDistance = 121
        elif (dropping == "Kottayam"):
            maxDistance = 132
        elif (dropping == "Alappuzha"):
            maxDistance = 129
        elif (dropping == "Pathanamthitta"):
            maxDistance = 180
        elif (dropping == "Ernakulam"):
            maxDistance = 74
        elif (dropping == "Malappuram"):
            maxDistance = 78
        elif (dropping == "Idukki"):
            maxDistance = 148
        elif (dropping == "Wayanad"):
            maxDistance = 193

    elif (picking == "Thiruvananthapuram"):
        if (dropping == "Kannur"):
            maxDistance = 466
        elif (dropping == "Thrissur"):
            maxDistance = 276
        elif (dropping == "Kollam"):
            maxDistance = 66
        elif (dropping == "Palakkad"):
            maxDistance = 338
        elif (dropping == "Kozhikode"):
            maxDistance = 381
        elif (dropping == "Kottayam"):
            maxDistance = 145
        elif (dropping == "Alappuzha"):
            maxDistance = 148
        elif (dropping == "Pathanamthitta"):
            maxDistance = 102
        elif (dropping == "Ernakulam"):
            maxDistance = 207
        elif (dropping == "Malappuram"):
            maxDistance = 355
        elif (dropping == "Idukki"):
            maxDistance = 241
        elif (dropping == "Wayanad"):
            maxDistance = 452

    elif (picking == "Palakkad"):
        if (dropping == "Kannur"):
            maxDistance = 213
        elif (dropping == "Thrissur"):
            maxDistance = 69
        elif (dropping == "Kollam"):
            maxDistance = 275
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 338
        elif (dropping == "Kozhikode"):
            maxDistance = 127
        elif (dropping == "Kottayam"):
            maxDistance = 191
        elif (dropping == "Alappuzha"):
            maxDistance = 189
        elif (dropping == "Pathanamthitta"):
            maxDistance = 240
        elif (dropping == "Ernakulam"):
            maxDistance = 134
        elif (dropping == "Malappuram"):
            maxDistance = 81
        elif (dropping == "Idukki"):
            maxDistance = 208
        elif (dropping == "Wayanad"):
            maxDistance = 183


    elif (picking == "Kozhikode"):
        if (dropping == "Kannur"):
            maxDistance = 90
        elif (dropping == "Thrissur"):
            maxDistance = 121
        elif (dropping == "Kollam"):
            maxDistance = 314
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 381
        elif (dropping == "Palakkad"):
            maxDistance = 127
        elif (dropping == "Kottayam"):
            maxDistance = 237
        elif (dropping == "Alappuzha"):
            maxDistance = 228
        elif (dropping == "Pathanamthitta"):
            maxDistance = 291
        elif (dropping == "Ernakulam"):
            maxDistance = 173
        elif (dropping == "Malappuram"):
            maxDistance = 50
        elif (dropping == "Idukki"):
            maxDistance = 259
        elif (dropping == "Wayanad"):
            maxDistance = 86

    elif (picking == "Kollam"):
        if (dropping == "Kannur"):
            maxDistance = 405
        elif (dropping == "Thrissur"):
            maxDistance = 215
        elif (dropping == "Kozhikode"):
            maxDistance = 314
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 66
        elif (dropping == "Palakkad"):
            maxDistance = 275
        elif (dropping == "Kottayam"):
            maxDistance = 94
        elif (dropping == "Alappuzha"):
            maxDistance = 86
        elif (dropping == "Pathanamthitta"):
            maxDistance = 56
        elif (dropping == "Ernakulam"):
            maxDistance = 144
        elif (dropping == "Malappuram"):
            maxDistance = 293
        elif (dropping == "Idukki"):
            maxDistance = 195
        elif (dropping == "Wayanad"):
            maxDistance = 390

    elif (picking == "Kottayam"):
        if (dropping == "Kannur"):
            maxDistance = 328
        elif (dropping == "Thrissur"):
            maxDistance = 132
        elif (dropping == "Kozhikode"):
            maxDistance = 237
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 145
        elif (dropping == "Palakkad"):
            maxDistance = 191
        elif (dropping == "Kollam"):
            maxDistance = 94
        elif (dropping == "Alappuzha"):
            maxDistance = 46
        elif (dropping == "Pathanamthitta"):
            maxDistance = 59
        elif (dropping == "Ernakulam"):
            maxDistance = 68
        elif (dropping == "Malappuram"):
            maxDistance = 212
        elif (dropping == "Idukki"):
            maxDistance = 125
        elif (dropping == "Wayanad"):
            maxDistance = 310

    elif (picking == "Alappuzha"):
        if (dropping == "Kannur"):
            maxDistance = 320
        elif (dropping == "Thrissur"):
            maxDistance = 129
        elif (dropping == "Kozhikode"):
            maxDistance = 228
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 157
        elif (dropping == "Palakkad"):
            maxDistance = 190
        elif (dropping == "Kollam"):
            maxDistance = 86
        elif (dropping == "Kottayam"):
            maxDistance = 46
        elif (dropping == "Pathanamthitta"):
            maxDistance = 71
        elif (dropping == "Ernakulam"):
            maxDistance = 59
        elif (dropping == "Malappuram"):
            maxDistance = 207
        elif (dropping == "Idukki"):
            maxDistance = 151
        elif (dropping == "Wayanad"):
            maxDistance = 305

    elif (picking == "Pathanamthitta"):
        if (dropping == "Kannur"):
            maxDistance = 390
        elif (dropping == "Thrissur"):
            maxDistance = 180
        elif (dropping == "Kozhikode"):
            maxDistance = 291
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 277
        elif (dropping == "Palakkad"):
            maxDistance = 68
        elif (dropping == "Kollam"):
            maxDistance = 217
        elif (dropping == "Kottayam"):
            maxDistance = 59
        elif (dropping == "Alappuzha"):
            maxDistance = 71
        elif (dropping == "Ernakulam"):
            maxDistance = 124
        elif (dropping == "Malappuram"):
            maxDistance = 260
        elif (dropping == "Idukki"):
            maxDistance = 140
        elif (dropping == "Wayanad"):
            maxDistance = 372

    elif (picking == "Ernakulam"):
        if (dropping == "Kannur"):
            maxDistance = 264
        elif (dropping == "Thrissur"):
            maxDistance = 74
        elif (dropping == "Kozhikode"):
            maxDistance = 173
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 215
        elif (dropping == "Palakkad"):
            maxDistance = 134
        elif (dropping == "Kollam"):
            maxDistance = 144
        elif (dropping == "Kottayam"):
            maxDistance = 67
        elif (dropping == "Alappuzha"):
            maxDistance = 59
        elif (dropping == "Pathanamthitta"):
            maxDistance = 124
        elif (dropping == "Malappuram"):
            maxDistance = 152
        elif (dropping == "Idukki"):
            maxDistance = 122
        elif (dropping == "Wayanad"):
            maxDistance = 250

    elif (picking == "Malappuram"):
        if (dropping == "Kannur"):
            maxDistance = 136
        elif (dropping == "Thrissur"):
            maxDistance = 78
        elif (dropping == "Kozhikode"):
            maxDistance = 50
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 364
        elif (dropping == "Palakkad"):
            maxDistance = 81
        elif (dropping == "Kollam"):
            maxDistance = 293
        elif (dropping == "Kottayam"):
            maxDistance = 212
        elif (dropping == "Alappuzha"):
            maxDistance = 207
        elif (dropping == "Pathanamthitta"):
            maxDistance = 260
        elif (dropping == "Ernakulam"):
            maxDistance = 152
        elif (dropping == "Idukki"):
            maxDistance = 228
        elif (dropping == "Wayanad"):
            maxDistance = 110

    elif (picking == "Idukki"):
        if (dropping == "Kannur"):
            maxDistance = 358
        elif (dropping == "Thrissur"):
            maxDistance = 148
        elif (dropping == "Kozhikode"):
            maxDistance = 259
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 241
        elif (dropping == "Palakkad"):
            maxDistance = 208
        elif (dropping == "Kollam"):
            maxDistance = 195
        elif (dropping == "Kottayam"):
            maxDistance = 125
        elif (dropping == "Alappuzha"):
            maxDistance = 151
        elif (dropping == "Pathanamthitta"):
            maxDistance = 140
        elif (dropping == "Ernakulam"):
            maxDistance = 122
        elif (dropping == "Malappuram"):
            maxDistance = 228
        elif (dropping == "Wayanad"):
            maxDistance = 341

    elif (picking == "Wayanad"):
        if (dropping == "Kannur"):
            maxDistance = 112
        elif (dropping == "Thrissur"):
            maxDistance = 193
        elif (dropping == "Kozhikode"):
            maxDistance = 86
        elif (dropping == "Thiruvananthapuram"):
            maxDistance = 452
        elif (dropping == "Palakkad"):
            maxDistance = 183
        elif (dropping == "Kollam"):
            maxDistance = 390
        elif (dropping == "Kottayam"):
            maxDistance = 310
        elif (dropping == "Alappuzha"):
            maxDistance = 305
        elif (dropping == "Pathanamthitta"):
            maxDistance = 372
        elif (dropping == "Ernakulam"):
            maxDistance = 250
        elif (dropping == "Malappuram"):
            maxDistance = 110
        elif (dropping == "Idukki"):
            maxDistance = 341
    elif(picking == dropping):
        messagebox.showinfo("Success", "Booked ", parent=frame)


    globalmaxdist = maxDistance
    convertedmaxDistance = str(maxDistance)
    maxdistancecities.set(convertedmaxDistance)

    return None

def change_to_main():
    
    loginframe.forget()
    frame.pack(expand=True,padx=30,pady=30)

def change_to_login():
    frame.forget()
    loginframe.pack(expand=True,padx=30,pady=30)



def change_to_hire_a_cab():
    dashboardframe.forget()
    frame.pack(expand=True,padx=30,pady=30)


def getBill():
    finalamt = 0
    picking = clicked.get()
    dropping = clicked1.get()
    if(globalmaxdist != 0):
        startinglocationvariable.set("Pickup Location :")
        pickupvariable.set(picking)
        endinglocationvariable.set("Destination Location :")
        dropvariable.set(dropping)
        cabtypevariable.set("Cab Type")

        cabtype.set(globalcartype)
        if(globalcartype == "Micro"):
            cabchargefinal = 30 + (15 * globalmaxdist)
        elif (globalcartype == "Sedan"):
            cabchargefinal = 45 + (25 * globalmaxdist)
        elif (globalcartype == "SUV"):
            cabchargefinal = 60 + (30 * globalmaxdist)
        cabchargetotal.set("Cab Charge :")
        cabcharge.set(cabchargefinal)
        if(insuranceset == 1):
            insuranceneeded.set("Insurance Amount :")
            insuranceamt.set("Rs.10")
            finalamt = cabchargefinal + 10
        elif(insuranceset == 0):
            insuranceneeded.set("")
            insuranceamt.set("")
            finalamt = cabchargefinal
        totalamountlab.set("Total :")
        convertedtotal = str(finalamt)
        global globalamount
        globalamount = convertedtotal
        totalamt.set(convertedtotal)

    else:
        messagebox.showinfo("Alert Message","We do not provide inter district cab service right now! , please select a different district!")

def book_cab():
    username = usernameloginEntry.get()
    driver_user_name = driverusernameloginEntry.get()
    cartype = globalcartype
    startinglocforsaving = clicked.get()
    endinglocforsaving = clicked1.get()
    wantedstatus = "Available"
    try:

        con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                      auth_plugin='mysql_native_password')
        cur = con.cursor()

        cur.execute("select * from driver_status where count = ( select MIN(count) from driver_status where driver_car_type = %s and driver_status_now = %s)",(cartype,wantedstatus))
        row_set = cur.fetchall()

        if(len(row_set) == 0):
            messagebox.showerror("Error", "Sorry ! No Drivers Available now", parent=frame)

        else:
            print(len(row_set))
            for row in row_set:

                driver_user_name = row[0]
                cartype = row[1]

            global globalamount
            hired_amount = globalamount
            setstatus = "Hired"
            messagebox.showinfo("Success", "Hired cab successfully!", parent=frame)
            cur.execute("select * from user_information where user_name = %s and password = %s",(usernameloginEntry.get(),passwordloginEntry.get()))
            user_row_set = cur.fetchall()
            userphone = user_row_set[0][5]
            sql = "INSERT INTO hired_cab (username,driver_user_name,cartype,pickuploc,droploc,status,amount,userphone) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (username,driver_user_name,cartype,startinglocforsaving,endinglocforsaving,setstatus,hired_amount,userphone)

            cur.execute(sql, val)
            status_now = "Hired"
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(status_now,driver_user_name))
            newstatus = "Hired"
            cur.execute("UPDATE driver_status set count = count+1 where driver_user_name = %s and driver_status_now = %s",(driver_user_name,newstatus))
            cur.execute("select driver_week_total from driver_info where driver_username = %s and driver_car_type = %s",(driver_user_name,cartype))
            now_total = cur.fetchall()
            converted_now_total = now_total[0][0]
            c_now_total = int(converted_now_total)
            converted_global_amount = int(globalamount)
            new_total = c_now_total + converted_global_amount
            cur.execute("UPDATE driver_info set driver_week_total = %s where driver_username = %s",(new_total, driver_user_name))

            con.commit()
            messagebox.showinfo("information", "Cab hired inserted successfully...")
            change_to_dashboard_from_hiring()
            root_tk = Tk()
            root_tk.geometry(f"{600}x{400}")
            root_tk.title("map_view_simple_example.py")
    
            # create map widget
            map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
            map_widget.pack(fill="both", expand=True)

            # google normal tile server
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            marker_2 = map_widget.set_address(startinglocforsaving, marker=True)
            marker_3 = map_widget.set_address(endinglocforsaving,marker=True)
            path_1 = map_widget.set_path([marker_2.position,marker_3 .position])
            root_tk.mainloop()



        con.close()

    except Exception as es:
        messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=frame)

def change_status_of_driver(choice):
    status_now = status_clicked.get()
    driver_usname = driverusernameloginEntry.get()
    if(status_now == "Available"):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(status_now,driver_usname))
            con.commit()
            messagebox.showinfo("information", "Status Changed Succesfully")
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)
    elif (status_now == "Hired"):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(status_now, driver_usname))
            con.commit()
            messagebox.showinfo("information", "Cab hired inserted successfully...")
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)
    elif (status_now == "Offline"):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="cabapp",
                                          auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("UPDATE driver_status set driver_status_now = %s WHERE driver_user_name = %s",(status_now, driver_usname))
            con.commit()
            messagebox.showinfo("information", "Cab hired inserted successfully...")
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=driverdashboard)

def hire_to_home():
    frame.forget()
    dashboardframe.pack(expand=True,padx=30,pady=30)

def hire_to_logout():
    frame.forget()
    loginframe.pack(expand=True,padx=30,pady=30)

def userlogin_to_main():
    loginframe.forget()
    parentframe.pack(expand=True,padx=30,pady=30)


def driverlogin_to_main():
    driverloginframe.forget()
    parentframe.pack(expand=True,padx=30,pady=30)

def driverregis_to_main():
    driverregisframe.forget()
    parentframe.pack(expand=True,padx=30,pady=30)


def userregis_to_main():
    regisframe.forget()
    parentframe.pack(expand=True,padx=30,pady=30)

def driverdashboard_to_main():
    driverdashboard.forget()
    parentframe.pack(expand=True,padx=30,pady=30)

def userdashboard_to_main():
    dashboardframe.forget()
    parentframe.pack(expand=True,padx=30,pady=30)

def usercancelframe_to_dashboard():
    usercancelframe.forget()
    dashboardframe.pack(expand=True,padx=30,pady=30)

def dashboard_to_edit():
    dashboardframe.forget()
    useredit.pack(expand=True,padx=10,pady=10)

root = Tk()
root.title('Cab Hiring System')
root.geometry("1000x600")
root.config(bg='#A67449')
image = Image.open("taxi.png")
bg = ImageTk.PhotoImage(image)

label1 = Label(root,image=bg)
label1.place(x=0,y=0)

clicked = StringVar()
clicked1 = StringVar()
r = IntVar()

globalcartype = "Micro"
globalmaxdist = 0
insuranceset = 0
globaldrivername = "Akshara"
globaldrivercartype = ""
globaldriverusername = ""
globalusercancelvalue = 0
globaldrivercancelvalue = 0
globalamount = 0
usernamename = ""


clicked.set(" Select Location")


clicked1.set("Select Location")

status_clicked = StringVar()
status_clicked.set("Set Status")


r.set(1)

cbox1 = IntVar()

parentframe = LabelFrame(root,text="Who are you?",padx=50,pady=50)
parentframe.config(bg="black")
regisframe = LabelFrame(root,text="User Registeration",padx=10,pady=10)
loginframe = LabelFrame(root,text="User Login",padx=10,pady=10)
dashboardframe = LabelFrame(root,text="Dashboard",padx=10,pady=10)
driverregisframe = LabelFrame(root,text="Cab Driver Registeration",padx=10,pady=10)
driverloginframe = LabelFrame(root,text="Driver Login",padx=10,pady=10)
driverdashboard = LabelFrame(root,text="Driver Dashboard",padx=10,pady=10)
useredit = LabelFrame(root,text="Edit Details",padx=10,pady=10)

parentframe.pack(expand=True,padx=30,pady=30)


userbutton = Button(parentframe,text="I am a User",command=change_frame_to_user_login)
userbutton.grid(row=1,column=0,padx=10,pady=30,ipadx=40,ipady=30)
driverbutton = Button(parentframe,text="I am a Driver",command=change_frame_to_driver_regis)
driverbutton.grid(row=1,column=1,padx=10,pady=30,ipadx=40,ipady=30)


firstnamelabel = Label(regisframe,text="Firstname")
firstnamelabel.grid(row=1,column=0,pady=10,padx=20)
firstnameEntry = Entry(regisframe,width=30)
firstnameEntry.grid(row=1,column=1,pady=10,padx=20)
lastnamelabel = Label(regisframe,text="Last name")
lastnamelabel.grid(row=2,column=0,pady=10,padx=20)
lasttnameEntry = Entry(regisframe,width=30)
lasttnameEntry.grid(row=2,column=1,pady=10,padx=20)
agelabel = Label(regisframe,text="Age")
agelabel.grid(row=3,column=0,pady=10,padx=20)
ageEntry = Entry(regisframe,width=30)
ageEntry.grid(row=3,column=1,pady=10,padx=20)
citylabel = Label(regisframe,text="City")
citylabel.grid(row=4,column=0,pady=10,padx=20)
cityEntry = Entry(regisframe,width=30)
cityEntry.grid(row=4,column=1,pady=10,padx=20)
addelabel = Label(regisframe,text="Address")
addelabel.grid(row=5,column=0,pady=10,padx=20)
addeEntry = Entry(regisframe,width=30)
addeEntry.grid(row=5,column=1,pady=10,padx=20)
phonelabel = Label(regisframe,text="Mobile")
phonelabel.grid(row=6,column=0,pady=10,padx=20)
phoneEntry = Entry(regisframe,width=30)
phoneEntry.grid(row=6,column=1,pady=10,padx=20)
maillabel = Label(regisframe,text="E-mail")
maillabel.grid(row=7,column=0,pady=10,padx=20)
mailEntry = Entry(regisframe,width=30)
mailEntry.grid(row=7,column=1,pady=10,padx=20)
usernamelabel = Label(regisframe,text="Username")
usernamelabel.grid(row=8,column=0,pady=10,padx=20)
usernameEntry = Entry(regisframe,width=30)
usernameEntry.grid(row=8,column=1,pady=10,padx=20)
passwordlabel = Label(regisframe,text="Password")
passwordlabel.grid(row=9,column=0,pady=10,padx=20)
passwordEntry = Entry(regisframe,width=30)
passwordEntry.grid(row=9,column=1,pady=10,padx=20)
signupbutton = Button(regisframe,text="Sign Up",command=Add)
signupbutton.grid(row=10,column=0,pady=10,padx=20)
loginbutton = Button(regisframe,text="Already have an account",command=change_frame)
loginbutton.grid(row=10,column=1,pady=10,padx=20)
userregisframeback = Button(regisframe,text="Back",command=userregis_to_main)
userregisframeback.grid(row=10,column=2,pady=10,padx=20)

usernameloginlabel = Label(loginframe ,text="Username")
usernameloginlabel.grid(row=1,column=0,pady=10,padx=20)
usernameloginEntry = Entry(loginframe ,width=30)
usernameloginEntry.grid(row=1,column=1,pady=10,padx=20)
passwordloginlabel = Label(loginframe ,text="Password")
passwordloginlabel.grid(row=2,column=0,pady=10,padx=20)
passwordloginEntry = Entry(loginframe ,width=30)
passwordloginEntry.grid(row=2,column=1,pady=10,padx=20)
enterdashboardbutton = Button(loginframe,text="Login",command=change_to_dashboard)
enterdashboardbutton.grid(row=3,column=0,pady=10,padx=20)
userloginframeback = Button(loginframe,text="Back",command=userlogin_to_main)
userloginframeback.grid(row=3,column=1,pady=10,padx=20)




driverfirstnamelabel = Label(driverregisframe,text="Firstname")
driverfirstnamelabel.grid(row=1,column=0,pady=10,padx=20)
driverfirstnameEntry = Entry(driverregisframe,width=30)
driverfirstnameEntry.grid(row=1,column=1,pady=10,padx=20)
driverlastnamelabel = Label(driverregisframe,text="Last name")
driverlastnamelabel.grid(row=2,column=0,pady=10,padx=20)
driverlasttnameEntry = Entry(driverregisframe,width=30)
driverlasttnameEntry.grid(row=2,column=1,pady=10,padx=20)
driveragelabel = Label(driverregisframe,text="Age")
driveragelabel.grid(row=3,column=0,pady=10,padx=20)
driverageEntry = Entry(driverregisframe,width=30)
driverageEntry.grid(row=3,column=1,pady=10,padx=20)
drivercitylabel = Label(driverregisframe,text="City")
drivercitylabel.grid(row=4,column=0,pady=10,padx=20)
drivercityEntry = Entry(driverregisframe,width=30)
drivercityEntry.grid(row=4,column=1,pady=10,padx=20)
driveraddelabel = Label(driverregisframe,text="Address")
driveraddelabel.grid(row=5,column=0,pady=10,padx=20)
driveraddeEntry = Entry(driverregisframe,width=30)
driveraddeEntry.grid(row=5,column=1,pady=10,padx=20)
driverphonelabel = Label(driverregisframe,text="Mobile")
driverphonelabel.grid(row=6,column=0,pady=10,padx=20)
driverphoneEntry = Entry(driverregisframe,width=30)
driverphoneEntry.grid(row=6,column=1,pady=10,padx=20)
drivercartype = Label(driverregisframe,text="Car Type")
drivercartype.grid(row=7,column=0,pady=10,padx=20)
drivercartypeentry = Entry(driverregisframe,width=30)
drivercartypeentry.grid(row=7,column=1,pady=10,padx=20)
driverusernamelabel = Label(driverregisframe,text="Username")
driverusernamelabel.grid(row=8,column=0,pady=10,padx=20)
driverusernameEntry = Entry(driverregisframe,width=30)
driverusernameEntry.grid(row=8,column=1,pady=10,padx=20)
driverpasswordlabel = Label(driverregisframe,text="Password")
driverpasswordlabel.grid(row=9,column=0,pady=10,padx=20)
driverpasswordEntry = Entry(driverregisframe,width=30)
driverpasswordEntry.grid(row=9,column=1,pady=10,padx=20)
driversignupbutton = Button(driverregisframe,text="Sign Up",command=driver_Add)
driversignupbutton.grid(row=10,column=0,pady=10,padx=20)
driverloginbutton = Button(driverregisframe,text="Already Have an Account",command=driver_change_frame_to_login)
driverloginbutton.grid(row=10,column=1,pady=10,padx=20)
driverregisframeback = Button(driverregisframe,text="Back",command=driverregis_to_main)
driverregisframeback.grid(row=10,column=2,pady=10,padx=20)

driverusernameloginlabel = Label(driverloginframe ,text="Username")
driverusernameloginlabel.grid(row=1,column=0,pady=10,padx=20)
driverusernameloginEntry = Entry(driverloginframe,width=30)
driverusernameloginEntry.grid(row=1,column=1,pady=10,padx=20)
driverpasswordloginlabel = Label(driverloginframe ,text="Password")
driverpasswordloginlabel.grid(row=2,column=0,pady=10,padx=20)
driverpasswordloginEntry = Entry(driverloginframe ,width=30)
driverpasswordloginEntry.grid(row=2,column=1,pady=10,padx=20)
driverenterdashboardbutton = Button(driverloginframe,text="Login",command=change_to_driver_dashboard)
driverenterdashboardbutton.grid(row=3,column=0,pady=10,padx=20)
driverloginframeback = Button(driverloginframe,text="Back",command=driverlogin_to_main)
driverloginframeback.grid(row=3,column=1,pady=10,padx=20)




frame = LabelFrame(root,text="Cab Booking",padx=10,pady=20)
frame1 = LabelFrame(frame,text="Customer Info",padx=10,pady=20)
frame2 = LabelFrame(frame,text="Route Info",padx=10,pady=20)
frame3 = LabelFrame(frame,text="Car Selection",padx=10,pady=20)
frame4 = LabelFrame(frame,text="Receipt",padx=10,pady=20)


frame3.pack(side=BOTTOM ,expand = True, fill = BOTH)
frame1.pack(side=LEFT, expand = True, fill = BOTH)
frame2.pack(side=LEFT, expand = True, fill = BOTH)
frame4.pack(side=LEFT, expand = True, fill = BOTH)






mylabel00 = Label(frame1,text="First Name",pady=10,padx=10)
mylabel01 = Label(frame1,text="Last Name",pady=10,padx=10)
mylabel02 = Label(frame1,text="Address",pady=10,padx=10)
mylabel03 = Label(frame1,text="Mobile",pady=10,padx=10)
mylabel04 = Label(frame1,text="Email",pady=10,padx=10)
mylabel05 = Label(frame1,text="Emergency Num",pady=10,padx=10)
e00 = Entry(frame1,width=30)
e00.insert(0,'Optional')
e01 = Entry(frame1,width=30)
e01.insert(0,'Optional')
e02 = Entry(frame1,width=30)
e02.insert(0,'Optional')
e03 = Entry(frame1,width=30)
e03.insert(0,'Optional')
e04 = Entry(frame1,width=30)
e04.insert(0,'Optional')
e05 = Entry(frame1,width=30)
e05.insert(0,'Optional')


mylabel00.grid(row=1,column=0)
mylabel01.grid(row=2,column=0)
mylabel02.grid(row=3,column=0)
mylabel03.grid(row=4,column=0)
mylabel04.grid(row=5,column=0)
mylabel05.grid(row=6,column=0)
e00.grid(row=1,column=1)
e01.grid(row=2,column=1)
e02.grid(row=3,column=1)
e03.grid(row=4,column=1)
e04.grid(row=5,column=1)
e05.grid(row=6,column=1)


mylabel1 = Label(frame2,text="Pickup",pady=10,padx=10)
mylabel2 = Label(frame2,text="Drop",pady=10,padx=10)
mylabel3 = Label(frame2,text="Max Passengers :",pady=10,padx=10)
mylabel4 = Label(frame2,text="Base Charge :",pady=10,padx=10)
mylabel5 = Label(frame2,text="Distance (Kms) :",pady=10,padx=10)

pdrop1 =  OptionMenu(frame2,clicked,"Kannur","Thrissur","Thiruvananthapuram","Kollam","Palakkad","Kozhikode","Kottayam","Alappuzha","Pathanamthitta","Ernakulam","Malappuram","Idukki","Kasaragod","Wayanad")
pdrop1.config(width=25)
e2 = Entry(frame2,width=30)
numofpassengers = StringVar()
numofpassengers.set("3")
numpassengerslabel = Label(frame2,textvariable=numofpassengers)
pdrop2 =  OptionMenu(frame2,clicked1,"Kannur","Thrissur","Thiruvananthapuram","Kollam","Palakkad","Kozhikode","Kottayam","Alappuzha","Pathanamthitta","Ernakulam","Malappuram","Idukki","Kasaragod","Wayanad",command=calcDistance)
pdrop2.config(width=25)
minbaseprice = StringVar()
minbaseprice.set("30")
basepricelabel = Label(frame2,textvariable= minbaseprice)
maxdistancecities  =StringVar()
maxdistancecities.set("0")
distancebtwcitieslabel = Label(frame2,textvariable=maxdistancecities)
c1 = Checkbutton(frame2,text="Travel Insurance",variable=cbox1,command=lambda: checkboxclicked(cbox1.get()))
insuranceprice = StringVar()
insuranceprice.set("Rs.0")
insurancelabel = Label(frame2,textvariable=insuranceprice)
getbillbutton = Button(frame2,text="Get Bill",padx=20,command = getBill)



mylabel1.grid(row=1,column=0)
mylabel2.grid(row=2,column=0)
mylabel3.grid(row=3,column=0)
mylabel4.grid(row=4,column=0)
mylabel5.grid(row=5,column=0)
pdrop1.grid(row=1,column=1)
pdrop2.grid(row=2,column=1)
numpassengerslabel.grid(row=3,column=1)
basepricelabel.grid(row=4,column=1)
distancebtwcitieslabel.grid(row=5,column=1)
c1.grid(row=6,column=0)
insurancelabel.grid(row=6,column=1)
getbillbutton.grid(row=8,column=0,pady=(20,0))

rb1 = Radiobutton(frame3,text="Micro (Charge per Km) :",variable=r,value=1,command=lambda: radioclicked(1))
rb2 = Radiobutton(frame3,text="Sedan (Charge per Km) :",variable=r,value=2,command=lambda: radioclicked(2))
rb3 = Radiobutton(frame3,text="SUV     (Charge per Km) :",variable=r,value=3,command=lambda: radioclicked(3))
microprice = StringVar()
microprice.set("Rs.15")
sedanprice = StringVar()
sedanprice.set("NA")
suvprice = StringVar()
suvprice.set("NA")
microlabel =  Label(frame3,textvariable=microprice)
sedanlabel =  Label(frame3,textvariable=sedanprice)
suvlabel =  Label(frame3,textvariable=suvprice)
bookbutton = Button(frame3,text="Book",command = book_cab)
hirehomebutton = Button(frame3,text="Home",command = hire_to_home)
hirelogoutbutton = Button(frame3,text="Log Out",command=hire_to_logout)



rb1.grid(row=1,column=0)
rb2.grid(row=2,column=0)
rb3.grid(row=3,column=0)

microlabel.grid(row=1,column=1)
sedanlabel.grid(row=2,column=1)
suvlabel.grid(row=3,column=1)
bookbutton.grid(row=3, column=3,padx=50)
hirehomebutton.grid(row=3,column=4,padx=50)
hirelogoutbutton.grid(row=3,column=5,padx=50)




billlabel = Label(frame4,text="####              BILL             ####")
billlabel.grid(row=0,column = 0)
startinglocationvariable = StringVar()
startinglocationvariable.set("")
pickupvariable = StringVar()
pickupvariable.set("")
startingloclabel = Label(frame4,textvariable=startinglocationvariable)
pickuploclabel = Label(frame4,textvariable=pickupvariable)
endinglocationvariable = StringVar()
endinglocationvariable.set("")
dropvariable = StringVar()
dropvariable.set("")
endingloclabel = Label(frame4,textvariable=endinglocationvariable)
droploclabel = Label(frame4,textvariable=dropvariable)
cabtypevariable = StringVar()
cabtypevariable.set("")
cabtype = StringVar()
cabtype.set("")
cabnametypelabel = Label(frame4,textvariable=cabtypevariable)
cabtypelabel = Label(frame4,textvariable=cabtype)
cabchargetotal = StringVar()
cabchargetotal.set("")
cabcharge = StringVar()
cabcharge.set("")
cabchargetotallabel = Label(frame4,textvariable=cabchargetotal)
cabchargelabel = Label(frame4,textvariable=cabcharge)
insuranceneeded = StringVar()
insuranceneeded.set("")
insuranceamt = StringVar()
insuranceamt.set("")
insuranceneededlabel = Label(frame4,textvariable=insuranceneeded)
insuranceamtlabel = Label(frame4,textvariable=insuranceamt)
totalamountlab = StringVar()
totalamountlab.set("")
totalamt = StringVar()
totalamt.set("")
totalamountlabel = Label(frame4,textvariable=totalamountlab)
totalamtlabel = Label(frame4,textvariable=totalamt)



startingloclabel.grid(row=3,column=0,pady=10)
pickuploclabel.grid(row=3,column=1,pady=10)
endingloclabel.grid(row=5,column=0,pady=10)
droploclabel.grid(row=5,column=1,pady=10)
cabnametypelabel.grid(row=7,column=0,pady=10)
cabtypelabel.grid(row=7,column=1,pady=10)
cabchargetotallabel.grid(row=9,column=0,pady=10)
cabchargelabel.grid(row=9,column=1,pady=10)
insuranceneededlabel.grid(row=10,column=0,pady=10)
insuranceamtlabel.grid(row=10,column=1,pady=10)
totalamountlabel.grid(row=11,column=0,pady=10)
totalamtlabel.grid(row=11,column=1,pady=(10,0))

drivercancelframe = LabelFrame(root,text="Cancel Booking",padx=10,pady=10)
drivercancelusername = Label(drivercancelframe, text="Driver Username :")
drivercancelusername.grid(row=1,column=0,padx=10,pady=10)
driverusernameforentry = Entry(drivercancelframe,width=30)
driverusernameforentry.grid(row=1,column=1,padx=10,pady=10)
drivercancelbookingid = Label(drivercancelframe,text="Booking ID : ")
drivercancelbookingid.grid(row=2,column=0,padx=10,pady=10)
drivercancelbookingidentry = Entry(drivercancelframe,width=30)
drivercancelbookingidentry.grid(row=2,column=1)


options = [
        "user is not present at current location",
        "unable to contact user",
        "don't want to go this particular location",
        "busy with some other work",
        "other reason",
    ]
drivercancelclicked = StringVar()
drivercancelclicked.set("Select Reason")
drivercanceldrop = OptionMenu(drivercancelframe, drivercancelclicked, *options)
drivercanceldrop.grid(row=3,column=0,padx=10,pady=10)

confirmdrivercancelbutton = Button(drivercancelframe, text="CANCEL RIDE", command=Ok)
confirmdrivercancelbutton.grid(row=4,column=0,padx=10,pady=10)

usercancelframe = LabelFrame(root,text="Cancel Booking",padx=10,pady=10)
usercancelusername = Label(usercancelframe, text="User Username :")
usercancelusername.grid(row=1,column=0,padx=10,pady=10)
userusernameforentry = Entry(usercancelframe,width=30)
userusernameforentry.grid(row=1,column=1,padx=10,pady=10)


useroptions = [
        "user is not present at current location",
        "unable to contact user",
        "don't want to go this particular location",
        "busy with some other work",
        "other reason",
    ]
usercancelclicked = StringVar()
usercancelclicked.set("Select Reason")
usercanceldrop = OptionMenu(usercancelframe, drivercancelclicked, *useroptions)
usercanceldrop.grid(row=2,column=0,padx=10,pady=10)

confirmusercancelbutton = Button(usercancelframe, text="CANCEL RIDE", command=userOk)
confirmusercancelbutton.grid(row=3,column=0,padx=10,pady=10)

usercancelframbackbutton = Button(usercancelframe,text="Back",command=usercancelframe_to_dashboard)
usercancelframbackbutton.grid(row=3,column=1,padx=10,pady=10)


changefirstnamelabel = Label(useredit,text="Firstname")
changefirstnamelabel.grid(row=1,column=0,pady=10,padx=20)
changefirstnameEntry = Entry(useredit,width=30)
changefirstnameEntry.grid(row=1,column=1,pady=10,padx=20)
changelastnamelabel = Label(useredit,text="Last name")
changelastnamelabel.grid(row=2,column=0,pady=10,padx=20)
changelasttnameEntry = Entry(useredit,width=30)
changelasttnameEntry.grid(row=2,column=1,pady=10,padx=20)
changeagelabel = Label(useredit,text="Age")
changeagelabel.grid(row=3,column=0,pady=10,padx=20)
changeageEntry = Entry(useredit,width=30)
changeageEntry.grid(row=3,column=1,pady=10,padx=20)
changecitylabel = Label(useredit,text="City")
changecitylabel.grid(row=4,column=0,pady=10,padx=20)
changecityEntry = Entry(useredit,width=30)
changecityEntry.grid(row=4,column=1,pady=10,padx=20)
changeaddelabel = Label(useredit,text="Address")
changeaddelabel.grid(row=5,column=0,pady=10,padx=20)
changeaddeEntry = Entry(useredit,width=30)
changeaddeEntry.grid(row=5,column=1,pady=10,padx=20)
changephonelabel = Label(useredit,text="Mobile")
changephonelabel.grid(row=6,column=0,pady=10,padx=20)
changephoneEntry = Entry(useredit,width=30)
changephoneEntry.grid(row=6,column=1,pady=10,padx=20)
changeusernamelabel = Label(useredit,text="Username")
changeusernamelabel.grid(row=7,column=0,pady=10,padx=20)
changeusernameEntry = Entry(useredit,width=30)
changeusernameEntry.grid(row=7,column=1,pady=10,padx=20)
changepasswordlabel = Label(useredit,text="Password")
changepasswordlabel.grid(row=8,column=0,pady=10,padx=20)
changepasswordEntry = Entry(useredit,width=30)
changepasswordEntry.grid(row=8,column=1,pady=10,padx=20)
saveandbackbutton = Button(useredit,text="Save and Logout ",command=change_details)
saveandbackbutton.grid(row=9,column=0,pady=10,padx=20)







root.mainloop()