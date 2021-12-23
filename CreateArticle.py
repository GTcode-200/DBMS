from tkinter import *
import os
import psycopg2
import sys
from datetime import datetime

uid=sys.argv[1]

category_id = {"Fashion":1, "Technology":2, "Gaming":3, "Educational":4}

def connect():
    global cur,con
    con=psycopg2.connect(
    host="localhost",
    database="knowledge_repo",
    user="postgres",
    password="Ganesh@123"
)
    cur = con.cursor()

# def create_article():
#     global main_screen
#     global article_title,article_description
#     main_screen = Tk()
#     main_screen.geometry("3000x1000")
#     main_screen.title("Create an Article")

#     Label(main_screen, text="Title: ").pack()
#     article_title = Entry(main_screen)
#     article_title.pack()

#     Label(main_screen, text="Description: ").pack()
#     article_description = Entry(main_screen)
#     article_description.pack()

    

#     global clicked
#     global article_content
    
#     clicked = StringVar()
#     clicked.set("")
#     categories = ["Fashion", "Technology", "Gaming", "Educational"]
#     Label(main_screen, text="Category: ").pack()
#     article_category = OptionMenu(main_screen, clicked, *categories).pack()
    
#     Label(main_screen, text="Content: ").pack()
#     article_content = Text(main_screen,height=10,width=50)
#     article_content.pack()

#     Button(main_screen, text="Submit",command=submit).pack()

#     main_screen.mainloop()

def create_article():
    global main_screen
    global article_title,article_description
    main_screen = Tk()
    main_screen.geometry("1000x650")
    main_screen.title("Create an Article")
    main_screen.configure(bg='#f2c496')

    Label(main_screen, text="Enter the details to create your Article!", bg='#f2c496').pack()
    Label(main_screen, text="", bg='#f2c496').pack()

    Label(main_screen, text="Title: ", bg='#f2c496').pack()
    article_title = Entry(main_screen)
    article_title.pack()
    Label(main_screen, text="", bg='#f2c496').pack()

    Label(main_screen, text="Description: ", bg='#f2c496').pack()
    article_description = Text(main_screen, height=3, width=40)
    article_description.pack()
    Label(main_screen, text="", bg='#f2c496').pack()


    global clicked
    global article_content

    clicked = StringVar()
    clicked.set("Choose a category")
    categories = ["Fashion", "Technology", "Gaming", "Educational"]
    Label(main_screen, text="Category: ", bg='#f2c496').pack()
    article_category = OptionMenu(main_screen, clicked, *categories).pack()
    Label(main_screen, text="", bg='#f2c496').pack()

    Label(main_screen, text="Content: ", bg='#f2c496').pack()
    article_content = Text(main_screen,height=15,width=80)
    article_content.pack()

    Label(main_screen, text="", bg='#f2c496').pack()
    Button(main_screen, text="Submit", command=submit,bd=2, bg='#eddaa1').pack()

    main_screen.mainloop()

def submit():
    connect()
    category=clicked.get()
    cid=category_id[category]
    content = article_content.get(1.0, "end-1c")
    title=article_title.get()
    desc=article_description.get(1.0, "end-1c")

    cur.execute("SELECT * FROM ARTICLE")
    rows=cur.fetchall()

    if(rows):
        article_id=rows[-1][0]+1
    else:
        article_id=1

    cur.execute("INSERT INTO ARTICLE VALUES(%s,%s,%s,%s,%s,%s)",(int(article_id),uid,cid,title,content,desc))
    con.commit()

    cur.execute("SELECT * FROM EDIT_HISTORY")
    edit_rows=cur.fetchall()
    if(edit_rows):
        edit_id=edit_rows[-1][0]+1
    else:
        edit_id=1
    cur.execute("INSERT INTO EDIT_HISTORY VALUES(%s,%s,%s,%s,%s,%s)",(edit_id,article_id,datetime.now(),datetime.now(),'created',uid))
    con.commit()

    main_screen.destroy()
    os.system("py Window1.py "+uid)
    

create_article()