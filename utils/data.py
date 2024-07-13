import os

from utils.databasefunctions import create_table, create_unique_index
from aiomysql import Error

from utils.sqliteutils import create_db, create_table_sqlite


async def assemble_data(database, server):
    try:
        await create_table(database,
                           f"""CREATE TABLE IF NOT EXISTS server_%s ( configname text, configoption BIGINT );""",
                           server)
        await create_unique_index(database,
                                  f""" CREATE UNIQUE INDEX IF NOT EXISTS idx_configname ON server_%s (configname); """,
                                  server)

    except Exception or Error as e:
        print(f"Assemble Data: {e}")


async def create_dirs(serverids):
    for a in serverids:
        if not os.path.exists(f"storage/{a.id}"):
            os.makedirs(f"storage/{a.id}")
        db = await create_db(f"storage/{a.id}/moderation.db")
        await create_table_sqlite(db,
                                  """CREATE TABLE IF NOT EXISTS warnings ( userid bigint NOT NULL, reason text);""")
