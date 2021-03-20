import os
import sys
import psycopg2.pool
from urllib.parse import urlparse

def getConn():
    db_url = urlparse(os.environ.get('DATABASE_URL'))

    dbconfig = {
        'minconn': 1,
        'maxconn': 3,
        'user': db_url.username,
        'password': db_url.password,
        'host': db_url.hostname,
        'database': db_url.path[1:],
    }

    con = psycopg2.pool.SimpleConnectionPool(**dbconfig)

    return con


def runQuery(username, pool):
    conn = pool.getconn()
    cur = conn.cursor()

    query = '''
        SELECT COUNT(1)
        FROM users
        WHERE username = \'%s\''''

    try:
        cur.execute(query % username)
    except psycopg2.Error as e:
        print(f'{e}', file=sys.stderr)
        raise e

    res = cur.fetchone()[0]

    cur.close()
    conn.close()

    if res:
        return True
    else:
        return False