# -*- coding: utf-8 -*-

import configparser
import time
import sqlite3


CONFIG = "data/c.conf"
INIT_DB_SQL = "dbscripts/init_db.sql"

c = configparser.ConfigParser()
c.read(CONFIG)

DB_FILENAME = c.get("db", "db_file")

CONN = None
MAX_RETRIES = 3

SQL_INSERT = "INSERT INTO STOCKS (code, name, buying_price, buying_at) VALUES (?, ?, ?, ?)"

def connect_db():
    if CONN == None:
        CONN = sqlite3.connect(DB_FILENAME)
        return CONN
    return CONN

def create_table_once():
    connect_db();
    CONN.executescript(INIT_DB_SQL);
    CONN.commit()

def insert_one(code, name, buying_price, buying_at):
    t = (code, name, buying_price, buying_at)
    connect_db();
    CONN.execute(SQL_INSERT, t);
    CONN.commit()

def insert_bulk(l):
    connect_db();
    for t in l:
        CONN.execute(sql, t);
    CONN.commit()

def get_statistics():
    return

def close_conn():
    CONN.close()
