import pymysql


def resetTable(host, user, passwd, dbname, charset, tablename):
    '''
    重置表，删除所有数据，不改变表结构
    :param host:主机名
    :param user:用户
    :param passwd:密码
    :param dbname:数据库名
    :param charset:字符集类型
    :param tablename:表名
    :return:-2:连接数据库失败;-1:写入数据失败;0:重置表成功;
    '''
    try:
        conn = pymysql.connect(host, user, passwd, dbname, charset=charset)
    except Exception as ex:
        return -2
    cursor = conn.cursor()
    sql = 'truncate table ' + tablename
    try:
        cursor.execute(sql)
        conn.commit()
        conn.close()
    except Exception as ex:
        conn.rollback()
        conn.close()
        return -1
    return 0


def insertDB(host, user, passwd, dbname, charset, tablename, data):
    '''
        多行数据写入MySql，data格式([(value1,value2...),(value1,value2...)...])
        :param host:主机名
        :param user:用户
        :param passwd:密码
        :param dbname:数据库名
        :param charset:字符集类型
        :param tablename:表名
        :param data:欲写入数据
        :return:受影响行数  -2:连接数据库失败;-1:写入数据失败;
        '''
    try:
        conn = pymysql.connect(host, user, passwd, dbname, charset=charset)
    except Exception as ex:
        return -2
    cursor = conn.cursor()
    sql = 'insert into ' + tablename + ' values('
    if len(data) > 0:
        for i in range(0, len(data[0])):
            if i == 0:
                sql += '%s'
            else:
                sql += ',%s'
    sql += ')'
    try:
        cursor.executemany(sql, data)
        conn.commit()
        conn.close()
    except Exception as ex:
        conn.rollback()
        conn.close()
        return -1
    return cursor.rowcount


def selectDB(host, user, passwd, dbname, charset, tablename, colname):
    '''
    查询表，返回所有表数据
    :param host:主机名
    :param user:用户
    :param passwd:密码
    :param dbname:数据库名
    :param charset:字符集类型
    :param tablename:表名
    :param colname:列名
    :return:所有表数据  -2:连接数据库失败;-1:查询数据失败;
    '''
    try:
        conn = pymysql.connect(host, user, passwd, dbname, charset=charset)
    except Exception as ex:
        return -2
    cursor = conn.cursor()
    sql = 'select '+colname+' from '+tablename
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.close()
    except Exception as ex:
        conn.close()
        return -1
    return data

