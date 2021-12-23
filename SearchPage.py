from tkinter import *
import psycopg2
import sys
import os

uid=sys.argv[1]

def connect():
    global cur,con
    con=psycopg2.connect(
    host="localhost",
    database="knowledge_repo",
    user="postgres",
    password="Ganesh@123"
)
    cur = con.cursor()

connect()

# def search_screen():
#     global main_screen,search_item
#     main_screen = Tk()
#     main_screen.geometry("3000x1000")
#     main_screen.title("Search for Articles")

#     search_item = Entry(main_screen, text="Search")
#     search_item.pack()
#     Button(text="Search", height=1, width=10,command=search).pack()
#     Button(text="BACK",command=back).pack()

#     main_screen.mainloop()

def search_screen():
    global main_screen, search_item
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    Frm = Frame(main_screen)
    Label(Frm,text='Enter Article to Find:').pack(side=LEFT)
    search_item = Entry(Frm)

    search_item.pack(side=LEFT, fill=BOTH, expand=1)

    search_item.focus_set()

    buttn = Button(Frm, text='Find', command=search)
    buttn.pack(side=RIGHT)
    Frm.pack(side=TOP)

    back = Button(main_screen, text='Back', command=back1)
    back.pack(side=LEFT)

    cur.execute("SELECT ARTICLE_TITLE FROM ARTICLE")
    titles=cur.fetchall()

    Label(text="\nSelect the Article from below:\n")

    for i in titles:
        Label(text=i[0]+"\n").pack()

    #txt = Text(main_screen)

    #txt.pack(side=BOTTOM)

    main_screen.mainloop()

def search():
    
    connect()
    word=search_item.get()

    cur.execute("SELECT ARTICLE_ID FROM ARTICLE WHERE ARTICLE_TITLE='"+word+"'")

    row=cur.fetchone()

    if(row):
        a_id=row[0]

        main_screen.destroy()
        os.system("py Article.py "+str(uid)+" "+str(a_id))
    else:
        Label(text="Article not present").pack()

def back1():
    main_screen.destroy()
    os.system("py Window1.py "+uid)


search_screen()