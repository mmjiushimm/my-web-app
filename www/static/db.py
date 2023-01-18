# -*- coding: utf-8 -*-

import aiomysql

# db_pool

async def create_db_pool():
    global db_pool
    db_pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, db='mysql',
                                        user='root', password='password')
    # return db_pool

async def db_select(sql_statement, args):
    global db_pool
    async with db_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_statement.replace('?', '%s'), args)
            result = await cur.fetchall()
            return result

async def db_execute(sql_statement, args):
    global db_pool
    async with db_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_statement.replace('?', '%s'), args)
            return cur.rowcount
