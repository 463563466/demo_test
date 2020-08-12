from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,about_patent FROM judgement_table_new_0717 where identify='商标号和商标名称'")
data = db.get_data()
num1 = 0

for concent in data:
    case_id = concent[0]
    try:
        patent = concent[1]#商标号和商标名称
        num = re.findall('\d+', patent)

        if len(num) > 0:
            data_Snum_set = list(set(num))
            test_Snum = [i for i in data_Snum_set if i != '']
            test_str_Snum = ';'.join(test_Snum)
            sql = "insert into judgement_table_shangbiao values('{}','{}','商标号','{}')".format(case_id,patent,test_str_Snum)
            db.execute_sql(sql)

        data_Sname = []
        name_1 = re.findall('“([^“].*?)”', patent)
        name_2 = re.findall('号([^“”].*?)[商图注文]', patent)
        if len(name_1) > 0:
            for i in name_1:
                data_Sname.append(i)
        if len(name_2) > 0:
            for i in name_2:
                data_Sname.append(i)
        if len(data_Sname) > 0:
            data_Sname_set = list(set(data_Sname))
            test_Sname = [i for i in data_Sname_set if i != '']
            test_str_Sname = ';'.join(test_Sname)
            sql = "insert into judgement_table_shangbiao values('{}','{}','商标名称','{}')".format(case_id, patent, test_str_Sname)
            db.execute_sql(sql)
        num1 += 1
        print('已清洗', num1, '条')
    except Exception as e:
        num1 += 1
        with open('log.txt', 'a', encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')



