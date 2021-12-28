import mysql.connector

config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'ecom',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

mycursor = cnx.cursor()


def init_database():
    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS product( itemid INT NOT NULL AUTO_INCREMENT,"
                         "name VARCHAR(500) NULL,"
                         "shop_location VARCHAR(500) NULL,"
                         "PRIMARY KEY (itemid))")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS price( priceid INT NOT NULL AUTO_INCREMENT,"
                         "itemid INT NOT NULL,"
                         "price INT,"
                         "rating_star INT,"
                         "ctime TIMESTAMP NOT NULL,"
                         "PRIMARY KEY (priceid))")
    except Exception as err:
        print(Exception, err)

    cnx.commit()


def insert_into_product(name, shop_location):
    try:
        sql = "INSERT INTO product (name, shop_location) VALUES (%s, %s)"
        val = (name, shop_location)
        mycursor.execute(sql, val)
        cnx.commit()
    except Exception as err:
        print(Exception, err)


def insert_into_price(itemid, price, rating_star):
    try:
        sql = "INSERT INTO price (itemid, price, rating_star) VALUES (%s, %s, %s)"
        val = (itemid, price, rating_star)
        mycursor.execute(sql, val)
        cnx.commit()
    except Exception as err:
        print(Exception, err)


def close_database():
    cnx.close()
