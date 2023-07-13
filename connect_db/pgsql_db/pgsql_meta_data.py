#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: pgsql_meta_data.py
@date: 2023/7/13 
"""

import psycopg2

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host",
                        port="your_port")
cursor = conn.cursor()

# 查询 pg_stat_user_tables 视图
cursor.execute(""" SELECT
                        relid,
                        schemaname,
                        relname,
                        seq_scan,
                        seq_tup_read,
                        idx_scan,
                        idx_tup_fetch,
                        n_tup_ins,
                        n_tup_upd,
                        n_tup_del,
                        n_tup_hot_upd,
                        n_live_tup,
                        n_dead_tup,
                        n_mod_since_analyze,
                        last_vacuum,
                        last_autovacuum,
                        last_analyze,
                        last_autoanalyze,
                        vacuum_count,
                        autovacuum_count,
                        analyze_count,
                        autoanalyze_count 
                    FROM
                        pg_stat_user_tables""")
table_stats = cursor.fetchall()

# 打印表级别的统计信息
for stat in table_stats:
    relid = stat[0]
    schemaname = stat[1]
    relname = stat[2]
    seq_scan = stat[3]
    seq_tup_read = stat[4]
    idx_scan = stat[5]
    idx_tup_fetch = stat[6]
    n_tup_ins = stat[7]
    n_tup_upd = stat[8]
    n_tup_del = stat[9]
    n_tup_hot_upd = stat[10]
    n_live_tup = stat[11]
    n_dead_tup = stat[12]
    n_mod_since_analy = stat[13]
    last_vacuum = stat[14]
    last_autovacuum = stat[15]
    last_analyze = stat[16]
    last_autoanalyze = stat[17]
    vacuum_count = stat[18]
    autovacuum_count = stat[19]
    analyze_count = stat[20]
    autoanalyze_count = stat[21]

    print(
        f"Table: {relname}, Seq Scan: {seq_scan}, Seq Tuples Read: {seq_tup_read}, Index Scan: {idx_scan}, Index Tuples Fetched: {idx_tup_fetch}")
    print(f"Inserts: {n_tup_ins}, Updates: {n_tup_upd}, Deletes: {n_tup_del}, Hot Updates: {n_tup_hot_upd}")
    print(f"Live Tuples: {n_live_tup}, Dead Tuples: {n_dead_tup}")
    print(
        f"Last Vacuum: {last_vacuum}, Last Autovacuum: {last_autovacuum}, Last Analyze: {last_analyze}, Last Autoanalyze: {last_autoanalyze}")
    print("")

# 关闭数据库连接
cursor.close()
conn.close()
