import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def create_post2(name, content):
        con = sql.connect(path.join(ROOT, 'database2.db'))
        cur = con.cursor()
        cur.execute('insert into posts2 (name, content) values(?, ?)', (name, content))
        con.commit()
        con.close()

def get_posts2():
        con = sql.connect(path.join(ROOT, 'database2.db'))
        cur = con.cursor()
        cur.execute('select * from posts2')
        posts = cur.fetchall()
        return posts


def create_post3(name, content):
        con = sql.connect(path.join(ROOT, 'database3.db'))
        cur = con.cursor()
        cur.execute('insert into posts3 (name, content) values(?, ?)', (name, content))
        con.commit()
        con.close()

def get_posts3():
        con = sql.connect(path.join(ROOT, 'database3.db'))
        cur = con.cursor()
        cur.execute('select * from posts3')
        posts = cur.fetchall()
        return posts


def create_post4(name, content):
        con = sql.connect(path.join(ROOT, 'database4.db'))
        cur = con.cursor()
        cur.execute('insert into posts4 (name, content) values(?, ?)', (name, content))
        con.commit()
        con.close()

def get_posts4():
        con = sql.connect(path.join(ROOT, 'database4.db'))
        cur = con.cursor()
        cur.execute('select * from posts4')
        posts = cur.fetchall()
        return posts
