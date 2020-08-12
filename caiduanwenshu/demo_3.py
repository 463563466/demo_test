# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,clear_about_patent FROM jugement_table_0728_re_qx where identify='商标号和商标名称'")
data = db.get_data()
num = 0
#468533
for concent in data:
    case_id = concent[0]
    try:
        patent = concent[1]  # 商标号和商标名称
        data_Sname = []
        Sname_1 = re.findall('申请号是?为?第?：?[^\dLＬlｌNＮｎn](\d{6,9})[^\da-zA-Z]号?', patent)
        Sname_1_1 = re.findall('注册证?号是?为?第?：?[^\dLＬlｌNＮｎn](\d{6,9})[^\da-zA-Z]号?', patent)
        Sname_2 = re.findall('第(\d{6,9})号\w{0,10}[注图文]?[册文字形]?商标', patent)
        Sname_2_1 = re.findall('第\d{6,9}号(\w{0,10})[注图文]?[册文字形]?商标', patent)
        Sname_3 = re.findall('“([^”，；。]+)”[注图文]?[册文字形]?商标', patent)
        Sname_4 = re.findall('第(\d{6,9})号“[^”，；。]+”[注图文]?[册文字形]?商标', patent)
        Sname_4_1 = re.findall('第\d{6,9}号“([^”，；。]+)”[注图文]?[册文字形]?商标', patent)
        Sname_5 = re.findall('第(\d{6,9})号“[^”，；。\d]+”', patent)
        Sname_5_1 = re.findall('第\d{6,9}号“([^”，；。\d]+)”', patent)
        if len(Sname_1) > 0:
            for i in Sname_1:
                data_Sname.append(i)
        if len(Sname_2) > 0:
            for i in Sname_2:
                data_Sname.append(i)
        if len(Sname_2_1) > 0:
            for i in Sname_2_1:
                data_Sname.append(i)
        if len(Sname_3) > 0:
            for i in Sname_3:
                data_Sname.append(i)
        if len(Sname_4) > 0:
            for i in Sname_4:
                data_Sname.append(i)
        if len(Sname_4_1) > 0:
            for i in Sname_4_1:
                data_Sname.append(i)
        if len(Sname_5) > 0:
            for i in Sname_5:
                data_Sname.append(i)
        if len(Sname_5_1) > 0:
            for i in Sname_5_1:
                data_Sname.append(i)
        if len(data_Sname) > 0:
            data_Sname_set = list(set(data_Sname))
            test_Sname = [i for i in data_Sname_set if i != '']
            test_str_Sname = ';'.join(test_Sname)
        else:
            test_str_Sname = 'null'
        # sql = "update judgement_table_new_0717 set clear_about_patent='{}' where case_id='{}' and identify='商标号和商标名称'".format(
        #     test_str_Sname, case_id)
        sql = "insert into  caiduanwenshu_0728 values ('{}','{}','{}','商标号和商标名称')".format(case_id,patent,test_str_Sname)
        db.execute_sql(sql)
        num += 1
        print('已清洗', num, '条')
    except Exception:
        num += 1
        with open('log.txt', 'a', encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')