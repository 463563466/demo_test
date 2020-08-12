# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("select t.* from judgement_distinct_clear t where t.identify = '专利名称' and t.clear_two like '20%.%'")
data = db.get_data()
num = 0
#57687
for concent in data:
    case_id = concent[0]
    clear_one = concent[1]
    identify = concent[3]
    try:
        fmt_content_n = concent[2]
        fmt_content_n_r = fmt_content_n.replace('ＺＬ','')
        dele = re.findall('\.\w',fmt_content_n_r)
        fmt_content = fmt_content_n_r.replace(dele[0],'')

        sql = "update judgement_distinct_clear set  clear_two = '{}' where case_id='{}' and clear_one ='{}' and identify = '{}'".format(fmt_content,case_id,clear_one,identify)
        db.execute_sql(sql)
        num+=1
        print('已筛选',num,'条')
    except Exception as e:
        num+=1
        with open('log_patentnum.txt','a',encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')
















