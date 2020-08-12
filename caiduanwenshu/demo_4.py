# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT * FROM caiduanwenshu_0728_finally where clear_two is null and identify='商标号和商标名称'")
data = db.get_data()
num = 0
#43741
for concent in data:
    case_id = concent[0]
    try:
        clear_one = concent[1]
        identify = concent[3]
        clear_two = re.findall('\d{6,9}',clear_one)
        if len(clear_two) == 0:
            continue
        clear_two_set = list(set(clear_two))
        test_clear_two = [i for i in clear_two_set if i != '']
        test_str_clear_two = ';'.join(test_clear_two)
        sql = "update caiduanwenshu_0728_finally set clear_two='{}' where case_id='{}' and clear_one='{}' and clear_two is null and identify='{}'".format(test_str_clear_two,case_id,clear_one,identify)
        db.execute_sql(sql)
        num += 1
        print('已清洗', num, '条')
    except Exception:
        num += 1
        with open('log_null.txt', 'a', encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')