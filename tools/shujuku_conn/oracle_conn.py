import cx_Oracle
import tools.shujuku_conn.config as config
import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

class OracleOperation(object):

    # 执行下面的execute_sql方法时会自动执行该初始化方法进行连接数据库
    def __init__(self):
        # 建立连接
        self.conn = cx_Oracle.connect(config.name, config.password, config.host_port_sid)
        # 创建游标
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql):
        """
        执行sql语句，并commit提交
        :param sql:需要执行的sql语句
        :return:
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def get_data(self):
        """
        获得查询数据
        :return: 返回查到的数据
        """
        data = self.cursor.fetchall()
        return data
    def get_one(self):
        data = self.cursor.fetchone()
        return data

    def close_oracle(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()