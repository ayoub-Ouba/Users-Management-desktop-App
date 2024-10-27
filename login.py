from tkinter import *
from pymongo import MongoClient
from tkinter import messagebox


client= MongoClient(host='localhost', port=27017)
db = client['project']



root2=Tk()
root2.title("login")
root2.geometry("925x500+300+200")
root2.configure(bg="#fff")
root2.resizable(False,False)

# function login
# def signin():
#     username=user.get()
#     password=passw.get()
    
#     users=db.test.find_one({"usernam": username, "password": password})

#     if (users==None):
#         messagebox.showerror("invalid","invalid username and password")
#     else:
#         print("Login successful")
#         root.destroy()
#         root2=Tk()
#         root2.geometry("925x500+300+200")
#         root2.configure(bg="#fff")
#         root2.resizable(False,False)
        
        

      
# img=PhotoImage(file="login.png")
# Label(root,image=img,bg="white").place(x=50,y=50)

# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=480,y=70)

# heading=Label(frame,text='Login',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
# heading.place(x=100,y=5)



# # Username

# # username function 
# def on_enter(e):
#     user.delete(0, "end")
# def on_leave(e):
#     name=user.get()
#     if name=="":
#         user.insert(0,'Username')
# user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# user.place(x=30,y=80)
# user.insert(0,"Username")
# user.bind("<FocusIn>",on_enter)
# user.bind("<FocusOut>",on_leave)

# Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# # Password
# def on_enter2(e):
#     passw.delete(0, "end")
#     passw.config(show="*")
# def on_leave2(e):
#     name=passw.get()
#     if name=="":
#         passw.insert(0,'Password')
#         passw.config(show="")
# passw=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# passw.place(x=30,y=150)
# passw.insert(0,"Password")
# passw.bind("<FocusIn>",on_enter2)
# passw.bind("<FocusOut>",on_leave2)

# Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# # Button 
# Button(frame,width=39,pady=7,text="Login",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)


# Div_titre
frame=Frame(root2,width=350,height=350,bg="white")
frame.place(x=390,y=60)
#  titre
heading=Label(frame,text='Add User',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",28,"bold"))
heading.place(x=5,y=1)

# Div_1
frame=Frame(root2,width=350,height=350,bg="white")
frame.place(x=10,y=100)
# FirstName  
def on_enter(e):
    first_name.delete(0, "end")
def on_leave(e):
    name=first_name.get()
    if name=="":
        first_name.insert(0,'FirstName') 
first_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
first_name.place(x=30,y=80)
first_name.insert(0,"FirstName")
first_name.bind("<FocusIn>",on_enter)
first_name.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# LastName 
def on_enter(e):
    lastt_name.delete(0, "end")
def on_leave(e):
    name=lastt_name.get()
    if name=="":
        lastt_name.insert(0,'LasttName') 
lastt_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
lastt_name.place(x=30,y=150)
lastt_name.insert(0,"LasttName")
lastt_name.bind("<FocusIn>",on_enter)
lastt_name.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# Age  
def on_enter(e):
    age.delete(0, "end")
def on_leave(e):
    name=age.get()
    if name=="":
        age.insert(0,'Age')
age=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
age.place(x=30,y=215)
age.insert(0,"Age")
age.bind("<FocusIn>",on_enter)
age.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
# Number
def on_enter(e):
    tele.delete(0, "end")
def on_leave(e):
    name=tele.get()
    if name=="":
        tele.insert(0,'Number')
tele=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
tele.place(x=30,y=285)
tele.insert(0,"Number")
tele.bind("<FocusIn>",on_enter)
tele.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=312)

# Div_2
frame=Frame(root2,width=350,height=350,bg="white")
frame.place(x=560,y=100)
# username 
def on_enter(e):
    user3.delete(0, "end")
def on_leave(e):
    name=user3.get()
    if name=="":
        user3.insert(0,'Username')
user3=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user3.place(x=30,y=80)
user3.insert(0,"User3name")
user3.bind("<FocusIn>",on_enter)
user3.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# Password  
def on_enter(e):
    pw.delete(0, "end")
    pw.config(show="*")
def on_leave(e):
    name=pw.get()
    if name=="":
        pw.insert(0,'Password')
        pw.config(show="")
pw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
pw.place(x=30,y=150)
pw.insert(0,"Password")
pw.bind("<FocusIn>",on_enter)
pw.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# Confirm Password  
def on_enter(e):
    cpw.delete(0, "end")
    cpw.config(show="*")
def on_leave(e):
    name=cpw.get()
    if name=="":
        cpw.insert(0,'Confirm Password')
        cpw.config(show="")
cpw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11) )
cpw.place(x=30,y=215)
cpw.insert(0,"Confirm Password")
cpw.bind("<FocusIn>",on_enter)
cpw.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
def insert():
    print("hfb")
# Button 
Button(frame,width=27,pady=0,text="ADD",bg="#57a1f8",fg="white",border=0,font=("Microsoft YaHei UI Light",13,"bold"),command=insert).place(x=25,y=295)
root2.mainloop()
    
# # Ajouter Utilisateur
# # Div_titre
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=390,y=60)
# #  titre
# heading=Label(frame,text='Add User',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",28,"bold"))
# heading.place(x=5,y=1)

# # Div_1
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=10,y=100)
# # FirstName  
# def on_enter(e):
#     first_name.delete(0, "end")
# def on_leave(e):
#     name=first_name.get()
#     if name=="":
#         first_name.insert(0,'FirstName') 
# first_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# first_name.place(x=30,y=80)
# first_name.insert(0,"FirstName")
# first_name.bind("<FocusIn>",on_enter)
# first_name.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# # LastName 
# def on_enter(e):
#     lastt_name.delete(0, "end")
# def on_leave(e):
#     name=lastt_name.get()
#     if name=="":
#         lastt_name.insert(0,'LasttName') 
# lastt_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# lastt_name.place(x=30,y=150)
# lastt_name.insert(0,"LasttName")
# lastt_name.bind("<FocusIn>",on_enter)
# lastt_name.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# # Age  
# def on_enter(e):
#     age.delete(0, "end")
# def on_leave(e):
#     name=age.get()
#     if name=="":
#         age.insert(0,'Age')
# age=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# age.place(x=30,y=215)
# age.insert(0,"Age")
# age.bind("<FocusIn>",on_enter)
# age.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
# # Number
# def on_enter(e):
#     tele.delete(0, "end")
# def on_leave(e):
#     name=tele.get()
#     if name=="":
#         tele.insert(0,'Number')
# tele=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# tele.place(x=30,y=285)
# tele.insert(0,"Number")
# tele.bind("<FocusIn>",on_enter)
# tele.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=312)

# # Div_2
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=560,y=100)
# # username 
# def on_enter(e):
#     user.delete(0, "end")
# def on_leave(e):
#     name=user.get()
#     if name=="":
#         user.insert(0,'Username')
# user=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# user.place(x=30,y=80)
# user.insert(0,"Username")
# user.bind("<FocusIn>",on_enter)
# user.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# # Password  
# def on_enter(e):
#     pw.delete(0, "end")
#     pw.config(show="*")
# def on_leave(e):
#     name=pw.get()
#     if name=="":
#         pw.insert(0,'Password')
#         pw.config(show="")
# pw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# pw.place(x=30,y=150)
# pw.insert(0,"Password")
# pw.bind("<FocusIn>",on_enter)
# pw.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# # Confirm Password  
# def on_enter(e):
#     cpw.delete(0, "end")
#     cpw.config(show="*")
# def on_leave(e):
#     name=cpw.get()
#     if name=="":
#         cpw.insert(0,'Confirm Password')
#         cpw.config(show="")
# cpw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11) )
# cpw.place(x=30,y=215)
# cpw.insert(0,"Confirm Password")
# cpw.bind("<FocusIn>",on_enter)
# cpw.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)

# # Button 
# Button(frame,width=27,pady=0,text="ADD",bg="#57a1f8",fg="white",border=0,font=("Microsoft YaHei UI Light",13,"bold")).place(x=25,y=295)



# Modifier Utilisateur
# Div_titre
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=390,y=60)
# #  titre
# heading=Label(frame,text='Update User',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",28,"bold"))
# heading.place(x=0,y=0)

# # Div_1
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=10,y=110)
# # FirstName  
# def on_enter(e):
#     first_name.delete(0, "end")
# def on_leave(e):
#     name=first_name.get()
#     if name=="":
#         first_name.insert(0,'FirstName') 
# first_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# first_name.place(x=30,y=80)
# first_name.insert(0,"FirstName")
# first_name.bind("<FocusIn>",on_enter)
# first_name.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# # LastName 
# def on_enter(e):
#     lastt_name.delete(0, "end")
# def on_leave(e):
#     name=lastt_name.get()
#     if name=="":
#         lastt_name.insert(0,'LasttName') 
# lastt_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# lastt_name.place(x=30,y=150)
# lastt_name.insert(0,"LasttName")
# lastt_name.bind("<FocusIn>",on_enter)
# lastt_name.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# # Age  
# def on_enter(e):
#     age.delete(0, "end")
# def on_leave(e):
#     name=age.get()
#     if name=="":
#         age.insert(0,'Age')
# age=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# age.place(x=30,y=215)
# age.insert(0,"Age")
# age.bind("<FocusIn>",on_enter)
# age.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
# # Number
# def on_enter(e):
#     tele.delete(0, "end")
# def on_leave(e):
#     name=tele.get()
#     if name=="":
#         tele.insert(0,'Number')
# tele=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# tele.place(x=30,y=285)
# tele.insert(0,"Number")
# tele.bind("<FocusIn>",on_enter)
# tele.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=312)

# # Div_2
# frame=Frame(root,width=350,height=350,bg="white")
# frame.place(x=560,y=110)
# # username 
# def on_enter(e):
#     user.delete(0, "end")
# def on_leave(e):
#     name=user.get()
#     if name=="":
#         user.insert(0,'Username')
# user=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# user.place(x=30,y=80)
# user.insert(0,"Username")
# user.bind("<FocusIn>",on_enter)
# user.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# # Password  
# def on_enter(e):
#     pw.delete(0, "end")
#     pw.config(show="*")
# def on_leave(e):
#     name=pw.get()
#     if name=="":
#         pw.insert(0,'Password')
#         pw.config(show="")
# pw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
# pw.place(x=30,y=150)
# pw.insert(0,"Password")
# pw.bind("<FocusIn>",on_enter)
# pw.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# # Confirm Password  
# def on_enter(e):
#     cpw.delete(0, "end")
#     cpw.config(show="*")
# def on_leave(e):
#     name=cpw.get()
#     if name=="":
#         cpw.insert(0,'Confirm Password')
#         cpw.config(show="")
# cpw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11) )
# cpw.place(x=30,y=215)
# cpw.insert(0,"Confirm Password")
# cpw.bind("<FocusIn>",on_enter)
# cpw.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)

# # Button 
# Button(frame,width=27,pady=0,text="Update",bg="#57a1f8",fg="white",border=0,font=("Microsoft YaHei UI Light",13,"bold")).place(x=25,y=295)

root.mainloop()