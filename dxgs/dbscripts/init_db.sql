DROP TABLE IF EXISTS STOCKS;
CREATE TABLE STOCKS(
    code varchar(6),
    name nvarchar(20),
    buying_price DECIMAL(6,2),
    buying_at integer,
);
