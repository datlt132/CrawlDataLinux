from lib.mySqlConfig import *

if __name__ == '__main__':
    init_database()
    insert_into_product("hello", "hello")
    insert_into_price("1", "10000", "4")