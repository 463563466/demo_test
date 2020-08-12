from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,about_patent FROM judgement_table_new_0717 where identify='专利号'")
data = db.get_data()
num = 0

for concent in data:
    case_id = concent[0]
    try:
        patent = concent[1]#专利号
        data_num = []
        num_1_1 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(8[5-9][1-3]\d{5})\.?[\dＸｘXx×]?', patent)
        num_1_2 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(9[0-9][1-3]\d{5})\.?[\dＸｘXx×]?', patent)
        num_1_3 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(0[0-3][1-3]\d{5})\.?[\dＸｘXx×]?', patent)
        num_1_4 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{7})\.?[\dＸｘXx×]?', patent)
        num_1_5 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{7})\.?[\dＸｘXx×]?', patent)
        num_1_6 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{7})\.?[\dＸｘXx×]?', patent)

        num_2_1 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?',
                             patent)
        num_2_2 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?',
                             patent)
        num_2_3 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?',
                             patent)
        num_2_4 = re.findall('[专申]?[请利]?号?为?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([ＸｘXx×]{12})\.?[\dＸｘXx×]?', patent)

        if len(num_1_1) > 0:
            for i in num_1_1:
                data_num.append(i)
        if len(num_1_2) > 0:
            for i in num_1_2:
                data_num.append(i)
        if len(num_1_3) > 0:
            for i in num_1_3:
                data_num.append(i)
        if len(num_1_4) > 0:
            for i in num_1_4:
                data_num.append(i)
        if len(num_1_5) > 0:
            for i in num_1_5:
                data_num.append(i)
        if len(num_2_1) > 0:
            for i in num_2_1:
                data_num.append(i)
        if len(num_2_2) > 0:
            for i in num_2_2:
                data_num.append(i)
        if len(num_2_3) > 0:
            for i in num_2_3:
                data_num.append(i)
        if len(num_2_4) > 0:
            for i in num_2_4:
                data_num.append(i)
        if len(data_num) > 0:
            data_num_set = list(set(data_num))
            test_num = [i for i in data_num_set if i != '']
            test_str_num = ';'.join(test_num)
        else:
            test_str_num = 'null'
        sql = "update judgement_table_new_0717 set clear_about_patent='{}' where case_id='{}' and identify='专利号'".format(test_str_num,case_id)
        db.execute_sql(sql)
        num += 1
        print('已清洗', num, '条')
    except Exception:
        num += 1
        with open('log.txt', 'a', encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')