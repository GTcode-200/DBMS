from tkinter import *;
import os
import sys

uid=sys.argv[1]

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    main_screen.title("Read or Create Article")

    Button(text="Read Articles", height="2", width="30",command=read).pack()
    Label(text="").pack()

    Button(text="Create Articles", height="2", width="30",command=create).pack()

    Button(text="Log Out",command=logout).place(x=1000,y=0)

    main_screen.mainloop()

def read():
    main_screen.destroy()
    os.system("python SearchPage.py "+uid)
def create():
    main_screen.destroy()
    os.system("python CreateArticle.py "+uid)
def logout():
    main_screen.destroy()
    os.system("python login.py")



main_account_screen()