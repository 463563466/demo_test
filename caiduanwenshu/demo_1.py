# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,clear_about_patent FROM jugement_table_0728_re_qx where identify='专利号'")
data = db.get_data()
num = 0
#57687
for concent in data:
    case_id = concent[0]
    try:
        fmt_content_n = concent[1]
        data_num = []
        num_1_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](8[5-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_1_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(8[5-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_1_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(8[5-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_1_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](9[0-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_1_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(9[0-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_1_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(9[0-9][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](0[0-3][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(0[0-3][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(0[0-3][1-3]\d{5})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](200[3-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_2_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](201[0-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](2020[1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_3_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{7})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](200[3-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(200[3-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](201[0-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_4_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(201[0-9][1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn](2020[1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?(2020[1-3]\d{3}[ＸｘXx×]{4})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([ＸｘXx×]{12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([ＸｘXx×]{12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_5_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([ＸｘXx×]{12})\.?[\dＸｘXx×]?', fmt_content_n)
        # 第开头
        num_6_1 = re.findall('第(8[5-9][1-3]\d{5})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_1_1 = re.findall('第8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_2 = re.findall('第(9[0-9][1-3]\d{5})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_2_2 = re.findall('第9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_3 = re.findall('第(0[0-3][1-3]\d{5})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_3_3 = re.findall('第0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_4 = re.findall('第(200[3-9][1-3]\d{7})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_4_4 = re.findall('第200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_5 = re.findall('第(201[0-9][1-3]\d{7})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_5_5 = re.findall('第201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_6 = re.findall('第(2020[1-3]\d{7})\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
        num_6_6_6 = re.findall('第2020[1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“([^”，；。]+)”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)

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
        if len(num_1_6) > 0:
            for i in num_1_6:
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
        if len(num_2_5) > 0:
            for i in num_2_5:
                data_num.append(i)
        if len(num_2_6) > 0:
            for i in num_2_6:
                data_num.append(i)

        if len(num_3_1) > 0:
            for i in num_3_1:
                data_num.append(i)
        if len(num_3_2) > 0:
            for i in num_3_2:
                data_num.append(i)
        if len(num_3_3) > 0:
            for i in num_3_3:
                data_num.append(i)
        if len(num_3_4) > 0:
            for i in num_3_4:
                data_num.append(i)
        if len(num_3_5) > 0:
            for i in num_3_5:
                data_num.append(i)
        if len(num_3_6) > 0:
            for i in num_3_6:
                data_num.append(i)

        if len(num_4_1) > 0:
            for i in num_4_1:
                data_num.append(i)
        if len(num_4_2) > 0:
            for i in num_4_2:
                data_num.append(i)
        if len(num_4_3) > 0:
            for i in num_4_3:
                data_num.append(i)
        if len(num_4_4) > 0:
            for i in num_4_4:
                data_num.append(i)
        if len(num_4_5) > 0:
            for i in num_4_5:
                data_num.append(i)
        if len(num_4_6) > 0:
            for i in num_4_6:
                data_num.append(i)

        if len(num_5_1) > 0:
            for i in num_5_1:
                data_num.append(i)
        if len(num_5_2) > 0:
            for i in num_5_2:
                data_num.append(i)
        if len(num_5_3) > 0:
            for i in num_5_3:
                data_num.append(i)
        if len(num_5_4) > 0:
            for i in num_5_4:
                data_num.append(i)
        if len(num_5_5) > 0:
            for i in num_5_5:
                data_num.append(i)
        if len(num_5_6) > 0:
            for i in num_5_6:
                data_num.append(i)

        if len(num_6_1) > 0:
            for i in num_6_1:
                data_num.append(i)
        if len(num_6_1_1) > 0:
            for i in num_6_1_1:
                data_num.append(i)
        if len(num_6_2) > 0:
            for i in num_6_2:
                data_num.append(i)
        if len(num_6_2_2) > 0:
            for i in num_6_2_2:
                data_num.append(i)
        if len(num_6_3) > 0:
            for i in num_6_3:
                data_num.append(i)
        if len(num_6_3_3) > 0:
            for i in num_6_3_3:
                data_num.append(i)
        if len(num_6_4) > 0:
            for i in num_6_4:
                data_num.append(i)
        if len(num_6_4_4) > 0:
            for i in num_6_4_4:
                data_num.append(i)
        if len(num_6_5) > 0:
            for i in num_6_5:
                data_num.append(i)
        if len(num_6_5_5) > 0:
            for i in num_6_5_5:
                data_num.append(i)
        if len(num_6_6) > 0:
            for i in num_6_6:
                data_num.append(i)
        if len(num_6_6_6) > 0:
            for i in num_6_6_6:
                data_num.append(i)

        if len(data_num) > 0:
            data_num_set = list(set(data_num))
            test_num = [i for i in data_num_set if i != '']
            test_str_num = ';'.join(test_num)
        else:
            test_str_num = ''

        sql = "insert into  caiduanwenshu_0728 values ('{}','{}','{}','专利号')".format(case_id,fmt_content_n,test_str_num)
        db.execute_sql(sql)
        num+=1
        print('已筛选',num,'条')
    except Exception as e:
        num+=1
        with open('log_patentnum.txt','a',encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')
















