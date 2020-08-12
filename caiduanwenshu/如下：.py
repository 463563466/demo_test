from tools.shujuku_conn.oracle_conn import OracleOperation
import re

db = OracleOperation()
sql ="select case_id from jugement_table_0807_re_qxxx "
db.execute_sql(sql)
data = db.get_data()


for datas in data:
    case_id = datas[0]
    sql1 = "select clear_two from jugement_table_0807_re_qxxx where case_id='{}' and identify='专利名称'".format(case_id)
    db.execute_sql(sql)
    clear_two  = db.get_data()
    num = 0
    for i in name:

