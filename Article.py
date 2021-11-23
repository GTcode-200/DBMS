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
au_id=row[1]
cur.execute("SELECT USER_NAME FROM USER_PERMISSION WHERE USER_ID="+str(au_id))
uname=cur.fetchone()[0]
cur.execute("SELECT PER_ID FROM USER_PERMISSION WHERE USER_ID="+uid)
pid=cur.fetchone()[0]
cur.execute("SELECT AVG(RATING) FROM RATING GROUP BY ARTICLE_ID HAVING ARTICLE_ID="+a_id)
avg=cur.fetchone()




k=450


def article():
    global main_screen,k,clicked,rate_label,comments_dict
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    main_screen.title("Article")

    if(avg):
        rate_label = Label(text="Rating for this article:"+str(avg[0]))
        rate_label.place(x=1200,y=200)
    else:
        rate_label = Label(text="No rating yet")
        rate_label.place(x=1200,y=200)

    Label(main_screen, text="Title:"+row[3]).pack()
    article_title = Label(main_screen, text="").pack()
    Label(main_screen,text="Author:"+uname).pack()

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
    clicked.set(0)

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

    comments_dict={}

    for c in read_comment:
        cur.execute("SELECT COUNT(COMMENT_LIKE_ID) FROM COMMENT_LIKES WHERE COMM_ID="+str(c[0]))
        like_count=cur.fetchone()[0]
        comments_dict[c[0]]=Label(main_screen,text=like_count)
        txt="User "+str(c[2])+" commented on "+str(c[3])+" at "+str(c[4])[:8]+"\n"+c[5]
        Label(main_screen,text=txt).place(x=0,y=k)
        Button(main_screen,text="like",command=lambda k=c[0]:like(k)).place(x=0,y=k+40)
        comments_dict[c[0]].place(x=40,y=k+40)
        k+=80

    global comm
    Label(main_screen,text="Add comment:").pack()
    comm=Entry()
    comm.pack()

    post=Button(main_screen,text="Post Comment",command=post_comment)
    post.pack()

    Label(main_screen, text="Rate This: ").place(x=1250,y=100)
    article_rating = OptionMenu(main_screen, clicked, *ratings).place(x=1300,y=100)
    Button(main_screen,text="Rate article",command=rate).place(x=1270,y=150)

    if(int(uid)==row[1] or pid==1):
        Button(text="Edit Content",command=edit_cont).pack()

    Button(main_screen,text="BACK",command=back).place(x=1000,y=500)

    main_screen.mainloop()



def edit():
    main_screen.destroy()
    os.system("python EditHistory.py "+uid+" "+a_id)

def post_comment():
    global k
    cur.execute("SELECT * FROM COMMENTS")
    comments=cur.fetchall()
    #print(comments)
    comm_content=comm.get()
    if(not comments):
        comm_id=1
    else:
        comm_id=comments[-1][0]+1
    if(comm_content):
        cur.execute("INSERT INTO COMMENTS VALUES(%s,%s,%s,%s,%s,%s)",(comm_id,a_id,uid,datetime.now(),datetime.now(),comm_content))
        con.commit()
        comm.delete(0,'end')

        cur.execute("SELECT * FROM COMMENTS WHERE ARTICLE_ID="+a_id)
        c=cur.fetchall()[-1]
        txt="User "+str(c[2])+" commented on "+str(c[3])+" at "+str(c[4])[:8]+"\n"+c[5]
        Label(main_screen,text=txt).place(x=0,y=k)
        Button(main_screen,text="like",command=lambda k=comm_id:like(k)).place(x=0,y=k+40)
        comments_dict[comm_id]=Label(text="0")
        comments_dict[comm_id].place(x=40,y=k+40)
        k+=80


def back():
    main_screen.destroy()
    os.system("python SearchPage.py "+uid)

def edit_cont():
    main_screen.destroy()
    os.system("python EditContent.py "+uid+" "+a_id)

def rate():
    rate_value=clicked.get()
    cur.execute("SELECT ARTICLE_ID,USER_ID FROM RATING")
    ratings=cur.fetchall()

    if (int(a_id),int(uid)) in ratings:
        cur.execute("UPDATE RATING SET RATING="+rate_value+" WHERE ARTICLE_ID="+a_id+" AND USER_ID="+uid)
        con.commit()
    else:
        cur.execute("INSERT INTO RATING VALUES(%s,%s,%s)",(a_id,uid,rate_value))
        con.commit()

    cur.execute("SELECT AVG(RATING) FROM RATING GROUP BY ARTICLE_ID HAVING ARTICLE_ID="+a_id)
    avg=cur.fetchone()

    rate_label.configure(text="Rating for this article:"+str(avg[0]))

def like(comm_id):
    cur.execute("SELECT * FROM COMMENT_LIKES")
    likes=cur.fetchall()
    if(likes):
        comm_like_id=likes[-1][0]+1
    else:
        comm_like_id=1

    cur.execute("SELECT COMM_ID,USER_ID FROM COMMENT_LIKES")

    cid_uid=cur.fetchall()
    if (comm_id,int(uid)) in cid_uid:
        cur.execute("DELETE FROM COMMENT_LIKES WHERE COMM_ID="+str(comm_id)+" AND USER_ID="+uid)
        con.commit()
    else:
        cur.execute("INSERT INTO COMMENT_LIKES VALUES(%s,%s,%s)",(comm_like_id,comm_id,int(uid)))
        con.commit()

    cur.execute("SELECT COUNT(COMMENT_LIKE_ID) FROM COMMENT_LIKES WHERE COMM_ID="+str(comm_id))
    like_count=cur.fetchone()[0]

    comments_dict[comm_id].configure(text=like_count)

    


article()

    




