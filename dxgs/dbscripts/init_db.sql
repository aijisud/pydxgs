DROP TABLE IF EXISTS STOCKS;
CREATE TABLE STOCKS(
    match_id integer,
    user_id integer,
    votes_count integer,
    stock_code varchar(6),
    stock_name nvarchar(20),
    buying_price DECIMAL(6,2),
    buying_at integer,
);
