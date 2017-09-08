# -*- coding: utf-8 -*-

import configparser
import time
import sqlite3


CONFIG = "c.conf"
INIT_DB_SQL = "dbscripts/init_db.sql"

c = configparser.ConfigParser()
c.read(CONFIG)

DB_FILENAME = c.get("db", "db_file")

CONN = None
MAX_RETRIES = 3

SQL_INSERT = "INSERT INTO STOCKS (id, user_id, user_name, votes_count, stock_code, stock_name, \
              stock_buying_price, stock_buying_at_str, stock_buying_at, stock_best_increase_percentage) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"


SQL_EXISTS = "SELECT count(*) from STOCKS WHERE user_id = ?"

SQL_STATISTICS = "SELECT sum(1) as buying_count, \
                    sum(votes_count) as votes_count, \
                    stock_code, \
                    stock_name, \
                    avg(buying_price) as buying_price, \
               FROM STOCKS \
              GROUP BY stock_code, stock_name"
"""
有%s人买了，%s人关注，股票[%s][%s]，均价%s
select "A"||ID AS MyStr from table1;
"""


def connect_db():
    if CONN == None:
        CONN = sqlite3.connect(DB_FILENAME)
        return CONN
    return CONN

def create_table_once():
    connect_db();
    CONN.executescript(INIT_DB_SQL);
    CONN.commit()

def __insert_one(match_id, user_id, votes_count, stock_code, stock_name, buying_price, buying_at):
    t = (match_id, user_id, votes_count, stock_code, stock_name, buying_price, buying_at)
    connect_db();
    if CONN.execute(SQL_EXISTS, t) > = 1:
        CONN.execute(SQL_INSERT, t);
    return True

def insert_bulk(l):
    connect_db();
    for t in l:
        CONN.execute(sql, t);
    CONN.commit()

def get_statistics():
    #SQL_STATISTICS
    return

def close_conn():
    CONN.close()







#end
