from tkinter import *;
import os
import sys

uid=sys.argv[1]

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x200")
    main_screen.title("Read or Create Article")
    main_screen.configure(bg='#f2c496')

    Button(text="Read Articles", height="2", width="30",command=read).pack()
    Label(text="", bg='#f2c496').pack()

    Button(text="Create Articles", height="2", width="30",command=create).pack()

    Button(text="Log Out",command=logout).pack(side=TOP)

    main_screen.mainloop()

def read():
    main_screen.destroy()
    os.system("py SearchPage.py "+uid)
def create():
    main_screen.destroy()
    os.system("py CreateArticle.py "+uid)
def logout():
    main_screen.destroy()
    os.system("py login.py")



main_account_screen()