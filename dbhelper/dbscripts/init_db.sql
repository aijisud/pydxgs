DROP TABLE IF EXISTS STOCKS;
CREATE TABLE STOCKS(
    match_id integer,
    user_id integer,
    user_name nvarchar(200),
    votes_count integer,
    stock_code varchar(6),
    stock_name nvarchar(20),
    stock_buying_price DECIMAL(6,2),
    stock_buying_at_str nvarchar(20),
    stock_buying_at integer,
    stock_best_increase_percentage DECIMAL(6,2)
);
