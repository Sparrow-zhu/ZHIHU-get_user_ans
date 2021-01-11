#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import datetime
today = datetime.datetime.today().strftime('%Y_%m_%d')

# 创建一个数据库表来保存信息
## 连接数据库
def mysql_conn():
    conn = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "你的数据库密码",
        db="你的数据库名称",
        charset = "utf8"
    )
    return conn

## 建表
def create_table(user_name_ch):
    create_sql = f'''
    CREATE TABLE `{user_name_ch}{today}`(
    id INT,
    编辑时间 VARCHAR(255),
    话题名称 VARCHAR(255),
    回答链接 VARCHAR(255),
    话题浏览量 INT,
    话题关注量 INT,
    回答总数 INT,
    PRIMARY KEY (`话题名称`)
    )ENGINE=INNODB DEFAULT CHARSET =utf8
    '''
    conn = mysql_conn()
    cursor = conn.cursor()
    cursor.execute(create_sql)
    conn.commit()
    conn.close()

## 插入记录
def insert(user_name_ch, item):
    sql = f"insert ignore `{user_name_ch}{today}`(id, 编辑时间, 话题名称, 回答链接, 话题浏览量, 话题关注量, 回答总数) " \
          "values (%s, %s, %s, %s, %s, %s, %s)"
    params = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    conn = mysql_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        cursor.connection.commit()

    except BaseException as e:
        print(u"错误在这里>>>>", e, u"<<<<错误在这里")

    conn.commit()
    conn.close()

## 数据整理
def regulate(user_name_ch):

    conn = mysql_conn()
    cursor = conn.cursor()
    cursor.execute(f"ALTER TABLE `{user_name_ch}{today}` ADD COLUMN 回答作者 VARCHAR(255)")
    cursor.execute(f"ALTER TABLE `{user_name_ch}{today}` ADD COLUMN 回答排名 VARCHAR(255)")

    cursor.execute(f"UPDATE `{user_name_ch}{today}` INNER JOIN `小鹿{today}` ON `{user_name_ch}{today}`.`话题名称` = `小鹿{today}`.`话题名称` "
                   f"SET `{user_name_ch}{today}`.`回答作者` = CONCAT('小鹿, '), "
                   f"`{user_name_ch}{today}`.`回答排名` = CONCAT(`小鹿{today}`.`当前排名`, ', ')"
                   )

    cursor.execute(f"UPDATE `{user_name_ch}{today}` INNER JOIN `探长2020_12_29` ON `{user_name_ch}{today}`.`话题名称` = `探长2020_12_29`.`话题名称` "
                   f"SET `{user_name_ch}{today}`.`回答作者` = CONCAT(`回答作者`, '探长, '), "
                   f"`{user_name_ch}{today}`.`回答排名` = CONCAT(`回答排名`, `探长2020_12_29`.`当前排名`, ', ')"
                   )

    cursor.execute(f"UPDATE `{user_name_ch}{today}` INNER JOIN `知群{today}` ON `{user_name_ch}{today}`.`话题名称` = `知群{today}`.`话题名称` "
                   f"SET `{user_name_ch}{today}`.`回答作者` = CONCAT(`回答作者`, '知群, '), "
                   f"`{user_name_ch}{today}`.`回答排名` = CONCAT(`回答排名`, `知群{today}`.`当前排名`, ', ')"
                   )

    conn.commit()
    conn.close()
