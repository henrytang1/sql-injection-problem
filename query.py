import os
import sqlite3
import sys


def getConn(db_path):
    if not os.path.exists(db_path):
        print(f'database {db_path} not found', file=sys.stderr)
        raise FileNotFoundError(f'database {db_path} not found')
        # sys.exit(1)
    conn = sqlite3.connect(db_path)
    return conn


def runQuery(username):
    conn = getConn('users.db')
    cur = conn.cursor()

    query = '''
        SELECT COUNT(1)
        FROM users
        WHERE username = \'%s\''''

    try:
        # cur.execute(query, params)
        cur.execute(query % username)
    except sqlite3.Error as e:
        print(f'{e}', file=sys.stderr)
        raise e
        # sys.exit(1)

    res = cur.fetchone()[0]

    cur.close()
    conn.close()

    if res:
        return True
    else:
        return False

if __name__ == "__main__":
    runRegQuery()