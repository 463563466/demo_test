# coding:utf-8
import re
from caiduanwenshu.just_about_patent import just_about_patent
from tools.shujuku_conn.oracle_conn import OracleOperation
import re



if __name__ == '__main__':
    db = OracleOperation()
    db1 = OracleOperation()
    db.execute_sql("select * from jugement_table_0807 where case_id='{}'".format('258329cf5c82cef3e8ee6ba60c4c28f00'))
    null_count = 0
    panjue_count = 0
    all_count = 0
    caiding_count = 0
    patent_count = 0
    print('开始--------')
    while True :
        data = db.get_one()
        if not data:
            break
        all_count+=1
        case_id = data[0]
        case_name = data[1]
        if case_name == None:
            case_name = ''
        try:
            case_reason = data[2]
            if case_reason == None:
                case_reason = ''
            fmt_content_clob = data[3]  # clob
            if fmt_content_clob == None:
                null_count+=1
                continue
            else:
                fmt_content = fmt_content_clob.read()
            run = just_about_patent(fmt_content, case_name, case_reason,patent_count,caiding_count)
            data1 = run.run()
            if data1 == None:
                panjue_count+=1
                # print('不在范围内--跳过，判决书+1')
                continue
            else:
                patent_num = data1["patent_num"]
                patent_name = data1["patent_name"]
                public_num = data1["public_num"]
                sql = "insert into jugement_table_0807_re values ('{}','{}','{}','{}','{}','{}')".format(case_id,case_reason,patent_num,patent_name,public_num,case_name)
                db1.execute_sql(sql)
                data_count = run.sql_name()
                patent_count = data_count["patent_count"]
                caiding_count = data_count["caiding_count"]
                print('已插入',all_count,'条','--','专利文书数量',patent_count,'--','裁定文书数量',caiding_count,'--','判决文书等数量',panjue_count,'--','文书为空数量',null_count)
        except Exception as e :
            with open('0807.txt','a',encoding='utf-8') as a:
                a.write(case_id)
                a.write('\n')






