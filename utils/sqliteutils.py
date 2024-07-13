import sqlite3
from sqlite3 import Error


async def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error or Exception as e:
        print(f"create db: {e}")


async def create_table_sqlite(conn, tabledata):
    """ create a table from the create_table_sql statement
    :param tabledata: Data to create in table
    :param conn: Connection object
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(tabledata)
        c.close()

    except Error or Exception as e:
        print(f"create table: {e}")


async def createuniqueindex(conn, datatoinsert):
    try:
        c = conn.cursor()
        c.execute(datatoinsert)
        conn.commit()
        c.close()
        conn.close()
    except Error or Exception as e:
        print(f"createuniqueindex: {e}")


async def get_config(conn, configname):
    try:
        c = conn.cursor()
        c.execute(""" SELECT configoption FROM config WHERE configname=? """, [configname])
        option = c.fetchone()
        if option:
            return option[0]
        return option
    except Exception as e:
        print(f"get config: {e}")


async def insertconfig(conn, configlist):
    # config list should be a length of 2.
    try:
        datatoinsert = f""" REPLACE INTO config(configname, configoption) VALUES( ?, ?) """
        c = conn.cursor()
        c.execute(datatoinsert, (configlist[0], str(configlist[1])))
        conn.commit()
        c.close()
        conn.close()

    except Error or Exception as e:
        print(f"insert config: {e}")


async def get_logging_config(conn, configname):
    try:
        c = conn.cursor()
        c.execute(""" SELECT logoption FROM logging WHERE logname=? """, [configname])
        option = c.fetchone()
        if option:
            return option[0]
        return option
    except Exception as e:
        print(f"get config: {e}")


async def insert_logging_config(conn, configlist):
    # config list should be a length of 2.
    try:
        datatoinsert = f""" REPLACE INTO logging(logname, logoption) VALUES( ?, ?) """
        c = conn.cursor()
        c.execute(datatoinsert, (configlist[0], str(configlist[1])))
        conn.commit()
        c.close()
        conn.close()

    except Error or Exception as e:
        print(f"insert logging config: {e}")


async def get_warnings(conn, userid):
    try:
        c = conn.cursor()
        c.execute(""" SELECT reason FROM warnings WHERE userid=? """, [userid])
        option = c.fetchall()
        c.close()
        conn.close()
        if option:
            return option
        else:
            return None

    except Exception or Error as e:
        print(f"get warnings: {e}")


async def insert_warning(conn, configlist):
    # config list should be a length of 2.
    try:
        datatoinsert = f""" INSERT INTO warnings(userid, reason) VALUES( ?, ?) """
        c = conn.cursor()
        c.execute(datatoinsert, (configlist[0], str(configlist[1])))
        conn.commit()
        c.close()

    except Error or Exception as e:
        print(f"insert warning: {e}")


async def remove_warnings(conn, user):
    try:
        datatoinsert = f""" DELETE from warnings WHERE userid=? """
        c = conn.cursor()
        c.execute(datatoinsert, (user,))
        conn.commit()
        c.close()
    except Error or Exception as e:
        print(f"Remove warnings: {e}")
