from tkinter import *
import os
import psycopg2
import sys
from datetime import datetime



a_id=sys.argv[2]
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

cur.execute("SELECT * FROM ARTICLE WHERE ARTICLE_ID="+str(a_id))
row=cur.fetchone()


k=450


def article():
    global main_screen,k
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    main_screen.title("Article")

    Label(main_screen, text="Title:"+row[3]).pack()
    article_title = Label(main_screen, text="").pack()

    Button(text="Edit History", height=1, width=40,command=edit).place(x=1200, y=0)

    Label(main_screen, text="Description:"+row[5]).pack()
    article_desc = Label(main_screen, text="").pack()

    cur.execute("SELECT CATEGORY_TITLE,CATEGORY_DESC FROM ARTICLE_CATEGORY WHERE CATEGORY_ID="+str(row[2]))
    categ=cur.fetchone()

    Label(main_screen,text="Category:"+categ[0]+"-"+categ[1]).pack()
    article_category = Label(main_screen, text="").pack()

    Label(main_screen, text="Content:"+row[4]).pack()
    article_content = Label(main_screen, text="").pack()

    clicked = StringVar()
    clicked.set("")

    l=[]

    for i in range(5):
        l.append(i)
        l.append(i+0.5)
    l.append(5)
    ratings = l
    

   # like = Button(main_screen, text="Like").pack()

    Label(main_screen, text="Comments:", bg="yellow").place(x=0,y=400)
    #user1 = Label(main_screen, text="user1: ").pack()
   # user1_comment = Label(main_screen, text="........").pack()
   # comment_like = Button(main_screen, text="Like").pack()

   
    cur.execute("SELECT * FROM COMMENTS WHERE ARTICLE_ID="+a_id)
    read_comment=cur.fetchall()

    for c in read_comment:
        txt="User "+str(c[2])+" commented at "+str(c[3])[:8]+"\n"+c[4]
        Label(main_screen,text=txt).place(x=0,y=k)
        k+=40

    global comm
    Label(main_screen,text="Add comment:").pack()
    comm=Entry()
    comm.pack()

    post=Button(main_screen,text="Post Comment",command=post_comment)
    post.pack()

    Label(main_screen, text="Rating: ").pack()
    article_rating = OptionMenu(main_screen, clicked, *ratings).pack()

    if(int(uid)==row[1]):
        Button(text="Edit Content").pack()

    Button(main_screen,text="BACK",command=back).place(x=1000,y=500)

    main_screen.mainloop()



def edit():
    main_screen.destroy()
    os.system("python EditHistory.py")

def post_comment():
    global k
    cur.execute("SELECT * FROM COMMENTS")
    comments=cur.fetchall()
    print(comments)
    comm_content=comm.get()
    if(not comments):
        comm_id=1
    else:
        comm_id=comments[-1][0]+1
    if(comm_content):
        cur.execute("INSERT INTO COMMENTS VALUES(%s,%s,%s,%s,%s)",(comm_id,a_id,uid,datetime.now(),comm_content))
        con.commit()
        comm.delete(0,'end')

    cur.execute("SELECT * FROM COMMENTS WHERE ARTICLE_ID="+a_id)
    c=cur.fetchall()[-1]
    txt="User "+str(c[2])+" commented at "+str(c[3])[:8]+"\n"+c[4]
    Label(main_screen,text=txt).place(x=0,y=k)
    k+=40


def back():
    main_screen.destroy()
    os.system("python SearchPage.py "+uid)

article()

    



