# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,fmt_content FROM shangbiao_zhengju_position where case_id = '2ede79fa6ec19b40d67b1f8a8fa594190' ")
data = db.get_data()
num = 0

for concent in data:
    case_id = concent[0]
    try:
        find_name = '证据'
        fmt_content_clob = concent[1]
        fmt_content = fmt_content_clob.read()
        # 匹配证据的个数
        find_count = fmt_content.count(find_name)
        #匹配到的第一个证据所占的位置百分比
        if len(fmt_content) > 0 or find_count == None:
            if find_count > 0:
                fmt_content_len = len(fmt_content)
                find_name_one_position =  fmt_content.find(find_name)
                baifenbi_position_one = int(find_name_one_position)/int(fmt_content_len) * 100
                found = round(baifenbi_position_one,2)
                baifenbi_position_one_y = str(found) + '%'
                if find_count > 1:
                    #匹配到的第二个证据所占的位置百分比
                    find_name_two_position = fmt_content.find(find_name,find_name_one_position+1)
                    baifenbi_position_two = int(find_name_two_position) / int(fmt_content_len) * 100
                    found2 = round(baifenbi_position_two, 2)
                    baifenbi_position_two_y = str(found2) + '%'
                else:
                    baifenbi_position_two_y = ''
            else:
                baifenbi_position_one_y = ''
                baifenbi_position_two_y = ''
            sql = "insert into shangbiao_zhengju_position1 values ('{}','{}','{}','{}')".format(case_id,baifenbi_position_one_y,baifenbi_position_two_y,find_count)
            db.execute_sql(sql)
            num+=1
            print('已筛选',num,'条')
        else:
            baifenbi_position_one_y = ''
            baifenbi_position_two_y = ''
            sql = "insert into shangbiao_zhengju_position1 values ('{}','{}','{}','{}')".format(case_id,baifenbi_position_one_y,baifenbi_position_two_y,find_count)
            db.execute_sql(sql)
            num += 1
            print('已筛选',num,'条')
    except Exception as e:
        with open('0805.txt','a',encoding='utf-8') as a:
            a.write(case_id)
            a.write('\n')