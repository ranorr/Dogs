import MySQLdb


def connection():
    """
    Create the connection to MySQL DB
    """
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='2865',
                           db='test')
    c = conn.cursor()

    return c, conn

if __name__ == '__main__':
    c, conn = connection()
    print ('it worked!')

