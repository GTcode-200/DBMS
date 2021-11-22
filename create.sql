drop database knowledge_repo;
create database knowledge_repo;

\c knowledge_repo

create table USER_PERMISSION
(
    user_id int,
    per_id int NOT NULL,
    user_name varchar,
    user_mobile varchar,
    user_email varchar,
    user_addr varchar,
    per_name varchar,
    pwd varchar,
    primary key(user_id)
);

create table ARTICLE_CATEGORY
(
    category_id int,
    category_desc varchar,
    category_title varchar,
    primary key(category_id)
    
);

create table ARTICLE
(
    article_id int,
    user_id int,
    category_id int,
    article_title varchar,
    article_content varchar,
    article_desc varchar,
    primary key(article_id),
    foreign key(user_id) references USER_PERMISSION(user_id),
    foreign key(category_id) references ARTICLE_CATEGORY(category_id)
);

 create table EDIT_HISTORY
 (
    edit_id int,
    article_id int,
    edit_time time,
    edit_date date,
    edit_type varchar,
    user_id int,
    primary key(edit_id),
    foreign key(article_id) references ARTICLE(article_id),
    foreign key(user_id) references USER_PERMISSION(user_id)
 );

 create table COMMENTS
 (
     comment_id int,
     article_id int,
     user_id int,
     comm_date date,
     comm_time time,
     comm_content varchar,
     primary key(comment_id),
     foreign key(article_id) references ARTICLE(article_id),
     foreign key(user_id) references USER_PERMISSION(user_id)
 );

 create table COMMENT_LIKES
 (
     comment_like_id int,
     comm_id int,
     user_id int,
     primary key(comment_like_id,comm_id),
     foreign key(comm_id) references COMMENTS(comment_id),
     foreign key(user_id) references USER_PERMISSION(user_id)
 );

 create table RATING
 (
     article_id int,
     user_id int,
     rating float,
     primary key(article_id,user_id),
     foreign key(article_id) references ARTICLE(article_id),
     foreign key(user_id) references USER_PERMISSION(user_id)
 );

 INSERT INTO ARTICLE_CATEGORY VALUES(1,'All kinds of artistic and fashionable expressions','Fashion');
 INSERT INTO ARTICLE_CATEGORY VALUES(2,'Related to the latest innovations in computer science and tech','Technology');
 INSERT INTO ARTICLE_CATEGORY VALUES(3,'Adding Fun to your Life','Gaming');
 INSERT INTO ARTICLE_CATEGORY VALUES(4,'A Great place for education','Educational');

 INSERT INTO USER_PERMISSION VALUES(555,1,'Admin1','9876543210','admin1@gmail.com','Admin 1 Address','admin','root');
 INSERT INTO USER_PERMISSION VALUES(666,1,'Admin2','9876543211','admin2@gmail.com','Admin 2 Address','admin','root');



