def getsql_insert_into_product(ecom, itemid, name, shopid, catid):
    try:
        sql = f'INSERT INTO `ecom`.`{ecom}_product` (`itemid`, `name`, `shopid`, `catid`) ' \
              f'VALUES ("{itemid}" ,"{name}", "{shopid}", "{catid}")'
        return sql
    except Exception as err:
        print(Exception, err)


def getsql_insert_into_price(ecom, itemid, price, rating_star):
    try:
        sql = f'INSERT INTO `ecom`.`{ecom}_price` (`itemid`, `price`, `rating_star`) VALUES ("{itemid}", "{price}", "{rating_star}")'
        return sql
    except Exception as err:
        print(Exception, err)
