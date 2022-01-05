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
        mycursor.execute("CREATE TABLE IF NOT EXISTS shopee_product( productid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL UNIQUE,"
                         "name VARCHAR(500),"
                         "shopid VARCHAR(500),"
                         "catid VARCHAR(500),"
                         "PRIMARY KEY (productid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS shopee_price( priceid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL,"
                         "price VARCHAR(500),"
                         "rating_star FLOAT,"
                         "ctime TIMESTAMP NOT NULL,"
                         "PRIMARY KEY (priceid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS tiki_product( productid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL UNIQUE,"
                         "name VARCHAR(500),"
                         "shopid VARCHAR(500),"
                         "PRIMARY KEY (productid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS tiki_price( priceid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL,"
                         "price VARCHAR(500),"
                         "rating_star FLOAT,"
                         "ctime TIMESTAMP NOT NULL,"
                         "PRIMARY KEY (priceid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS sendo_product( productid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL UNIQUE,"
                         "name VARCHAR(500),"
                         "shopid VARCHAR(500),"
                         "PRIMARY KEY (productid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS sendo_price( priceid INT NOT NULL AUTO_INCREMENT,"
                         "itemid VARCHAR(500) NOT NULL,"
                         "price VARCHAR(500),"
                         "rating_star FLOAT,"
                         "ctime TIMESTAMP NOT NULL,"
                         "PRIMARY KEY (priceid))"
                         "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    except Exception as err:
        print(Exception, err)

    cnx.commit()


def insert_into_product(ecom, itemid, name, shopid, catid):
    try:
        sql = f'INSERT INTO `ecom`.`{ecom}_product` (`itemid`, `name`, `shopid`, `catid`) ' \
              f'VALUES ("{itemid}" ,"{name}", "{shopid}", "{catid}")'
        # val = (itemid, name, shopid, catid)
        # mycursor.execute(sql, val)
        # cnx.commit()
        return sql
    except Exception as err:
        print(Exception, err)


def insert_into_price(ecom, itemid, price, rating_star):
    try:
        sql = f'INSERT INTO `ecom`.`{ecom}_price` (`itemid`, `price`, `rating_star`) VALUES ("{itemid}", "{price}", "{rating_star}")'
        # val = (itemid, price, rating_star)
        # mycursor.execute(sql, val)
        # cnx.commit()
        return sql
    except Exception as err:
        print(Exception, err)


def close_database():
    cnx.close()
