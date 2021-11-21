from tkinter import *
import os

def EditHistory():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    main_screen.title("Edit History")

    Label(main_screen, text="User: ").pack()
    user_edit = Label(main_screen, text="user1").pack()

    Label(main_screen, text="Date of edit: ").pack()
    date_edit = Label(main_screen, text="10.10.2021").pack()

    Label(main_screen, text="Type of edit: ").pack()
    type_edit = Label(main_screen, text="Creation").pack()

    Button(main_screen,text="Back",command=back).pack()

    main_screen.mainloop()


def back():
    main_screen.destroy()
    os.system("python Article.py")
    


EditHistory()