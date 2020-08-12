# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql('SELECT case_id,case_reason,fmt_content FROM jugement_table_0728')
data = db.get_data()
num = 0

for concent in data:
    case_id = concent[0]
    try:
        case_reason = concent[1]
        fmt_content_clob = concent[2]  # clob
        fmt_content = fmt_content_clob.read()
        if fmt_content == None:
            sql = "insert into jugement_table_0728_re values ('{}','{}','{}','{}','{}','{}','{}')".format(case_id,case_reason,'','','','','')
            db.execute_sql(sql)
            num += 1
            print('已筛选', num, '条')
            continue
        fmt_content_r = fmt_content.replace('&amp;', '&').replace('&times;', '×').replace('&ldquo;', '“').\
            replace('&rdquo;', '”').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '“').\
            replace('&hellip;','…').replace('&middot;', '·').replace('&mdash;', '—').replace('&nbsp;', ' ')

        '''
        现有技术抗辩，参考文献，附件，一般都在文章后边，不限定位置，直接.*删除
        证据需要限定位置，位置还需要讨论
        对比文件需要限定位置，
        还有一种情况是文章中同事出现两种或两种以上
        需要层级删除
        限定删除的优先级--
        一般参考文献都会出现在文章最后，先删除参考文献应该会没有影响
        然后是附件，一般附件也会出现在文章最后，第二删除附件
        
        专利号-- ，年份后边的数字，12389，还有 85-03年的xxxx的匹配规则
        专利号-- 。\w{8,13}
        引号问题--中文引号，英文引号，双引号与单引号，
        专利公开号-- 末尾字符需要改成有或者没有，或者末尾是数字
        专利名称---名称为。。。。。的问题
        
        限定问题，在case_reason,case_name 字段中限定关键字，
        知识产权，专利，发明，实用新型，外观设计，发明人，设计人，
        
        
        
        '''
        #先删除参考文献
        wenxian = re.findall('参考文献.*', fmt_content_r)
        # 第二删除附件
        fujian = re.findall('附件.*', fmt_content_r)



        zhengju = re.findall('证据.*', fmt_content_r)
        kangbian = re.findall('现有技术抗辩.*', fmt_content_r)
        duibi = re.findall('对比文件.*', fmt_content_r)

        fmt_content_n = fmt_content_r
        if len(zhengju) > 0:
            fmt_content_n = fmt_content_r.replace(zhengju[0], '')
        if len(kangbian) > 0:
            fmt_content_n = fmt_content_r.replace(kangbian[0], '')
        if len(wenxian) > 0:
            fmt_content_n = fmt_content_r.replace(wenxian[0], '')
        if len(duibi) > 0:
            fmt_content_n = fmt_content_r.replace(duibi[0], '')
        if len(fujian) > 0:
            fmt_content_n = fmt_content_r.replace(fujian[0], '')
        test_str_num = 'null'
        if case_reason != '侵害商标专用权纠纷':
            data_num = []
            # ZL开头
            num_1_1  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_1_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_1_3  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_1_4  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_1_5  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_1_6  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_1  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_2  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_3  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_4  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_5  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_2_6  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_1  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_2  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_3  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_4  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]2020[1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_5  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_3_6  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{7}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_1  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_2  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_3  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_4  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_5  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_4_6  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_1  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_2  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_3  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_4  = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][ＸｘXx×]{12}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_5  = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[ＸｘXx×]{12}\.?[\dＸｘXx×]?',fmt_content_n)
            num_5_6  = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[ＸｘXx×]{12}\.?[\dＸｘXx×]?',fmt_content_n)
            # 第开头
            num_6_1 = re.findall('第8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
            num_6_2 = re.findall('第9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
            num_6_3 = re.findall('第0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
            num_6_4 = re.findall('第200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
            num_6_5 = re.findall('第201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)
            num_6_6 = re.findall('第2020[1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)


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
            if len(num_6_2) > 0:
                for i in num_6_2:
                    data_num.append(i)
            if len(num_6_3) > 0:
                for i in num_6_3:
                    data_num.append(i)
            if len(num_6_4) > 0:
                for i in num_6_4:
                    data_num.append(i)
            if len(num_6_5) > 0:
                for i in num_6_5:
                    data_num.append(i)
            if len(num_6_6) > 0:
                for i in num_6_6:
                    data_num.append(i)

            if len(data_num) > 0:
                data_num_set = list(set(data_num))
                test_num = [i for i in data_num_set if i != '']
                test_str_num = ';'.join(test_num)
            else:
                test_str_num = ''

        #专利名称
        data_name = []
        # name_1_1 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',fmt_content_n)
        name_1_1_1 = re.findall('“[^”，；。]+”发明',fmt_content_n)
        name_1_1_2 = re.findall('“[^”，；。]+”、发明',fmt_content_n)
        name_1_1_3 = re.findall('“[^”，；。]+”，发明',fmt_content_n)
        name_1_1_4 = re.findall('“[^”，；。]+”涉案发明',fmt_content_n)
        name_1_1_5 = re.findall('“[^”，；。]+”的发明',fmt_content_n)
        # name_1_2 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
        name_1_2_1 = re.findall('“[^”，；。]+”实用新型', fmt_content_n)
        name_1_2_2 = re.findall('“[^”，；。]+”、实用新型', fmt_content_n)
        name_1_2_3 = re.findall('“[^”，；。]+”，实用新型', fmt_content_n)
        name_1_2_4 = re.findall('“[^”，；。]+”涉案实用新型', fmt_content_n)
        name_1_2_5 = re.findall('“[^”，；。]+”的实用新型', fmt_content_n)
        # name_1_3 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
        name_1_3_1 = re.findall('“[^”，；。]+”外观', fmt_content_n)
        name_1_3_2 = re.findall('“[^”，；。]+”、外观', fmt_content_n)
        name_1_3_3 = re.findall('“[^”，；。]+”，外观', fmt_content_n)
        name_1_3_4 = re.findall('“[^”，；。]+”涉案外观', fmt_content_n)
        name_1_3_5 = re.findall('“[^”，；。]+”的外观', fmt_content_n)
        # name_1_4 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
        name_1_4_1 = re.findall('“[^”，；。]+”专利', fmt_content_n)
        name_1_4_2 = re.findall('“[^”，；。]+”、专利', fmt_content_n)
        name_1_4_3 = re.findall('“[^”，；。]+”，专利', fmt_content_n)
        name_1_4_4 = re.findall('“[^”，；。]+”涉案专利', fmt_content_n)
        name_1_4_5 = re.findall('“[^”，；。]+”的专利', fmt_content_n)
        # name_1_5 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
        name_1_5_1 = re.findall('“[^”，；。]+”申请', fmt_content_n)
        name_1_5_2 = re.findall('“[^”，；。]+”、申请', fmt_content_n)
        name_1_5_3 = re.findall('“[^”，；。]+”，申请', fmt_content_n)
        name_1_5_4 = re.findall('“[^”，；。]+”涉案申请', fmt_content_n)
        name_1_5_5 = re.findall('“[^”，；。]+”的申请', fmt_content_n)


        # name_2_1 = re.findall('发明名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_1_1 = re.findall('发明“[^”，；。]+”', fmt_content_n)
        name_2_1_2 = re.findall('发明名称“[^”，；。]+”', fmt_content_n)
        name_2_1_3 = re.findall('发明为“[^”，；。]+”', fmt_content_n)
        name_2_1_4 = re.findall('发明名称为“[^”，；。]+”', fmt_content_n)
        # name_2_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_2_1 = re.findall('实用新型“[^”，；。]+”', fmt_content_n)
        name_2_2_2 = re.findall('实用新型名称“[^”，；。]+”', fmt_content_n)
        name_2_2_3 = re.findall('实用新型为“[^”，；。]+”', fmt_content_n)
        name_2_2_4 = re.findall('实用新型名称为“[^”，；。]+”', fmt_content_n)
        # name_2_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_3_1 = re.findall('外观设计“[^”，；。]+”', fmt_content_n)
        name_2_3_2 = re.findall('外观设计名称“[^”，；。]+”', fmt_content_n)
        name_2_3_3 = re.findall('外观设计为“[^”，；。]+”', fmt_content_n)
        name_2_3_4 = re.findall('外观设计名称为“[^”，；。]+”', fmt_content_n)
        # name_2_4 = re.findall('专利名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_4_1 = re.findall('专利“[^”，；。]+”', fmt_content_n)
        name_2_4_2 = re.findall('专利名称“[^”，；。]+”', fmt_content_n)
        name_2_4_3 = re.findall('专利为“[^”，；。]+”', fmt_content_n)
        name_2_4_4 = re.findall('专利名称为“[^”，；。]+”', fmt_content_n)
        # name_2_5 = re.findall('申请名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_5_1 = re.findall('申请“[^”，；。]+”', fmt_content_n)
        name_2_5_2 = re.findall('申请名称“[^”，；。]+”', fmt_content_n)
        name_2_5_3 = re.findall('申请为“[^”，；。]+”', fmt_content_n)
        name_2_5_4 = re.findall('申请名称为“[^”，；。]+”', fmt_content_n)

        name_3_1 =re.findall('名称为“[^”，；。]+”（专利',fmt_content_n)
        name_3_2 =re.findall('名称为“[^”，；。]+”（发明',fmt_content_n)
        name_3_3 =re.findall('名称为“[^”，；。]+”（实用新型',fmt_content_n)
        name_3_4 =re.findall('名称为“[^”，；。]+”（外观设计',fmt_content_n)
        name_3_5 =re.findall('名称为“[^”，；。]+”（申请',fmt_content_n)

        # name_4_1 = re.findall('《.*?》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',fmt_content_n)
        name_4_1_1 = re.findall('《[^》，；。]+》发明', fmt_content_n)
        name_4_1_2 = re.findall('《[^》，；。]+》、发明', fmt_content_n)
        name_4_1_3 = re.findall('《[^》，；。]+》，发明', fmt_content_n)
        name_4_1_4 = re.findall('《[^》，；。]+》涉案发明', fmt_content_n)
        name_4_1_5 = re.findall('《[^》，；。]+》的发明', fmt_content_n)
        # name_4_2 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
        name_4_2_1 = re.findall('《[^》，；。]+》实用新型', fmt_content_n)
        name_4_2_2 = re.findall('《[^》，；。]+》、实用新型', fmt_content_n)
        name_4_2_3 = re.findall('《[^》，；。]+》，实用新型', fmt_content_n)
        name_4_2_4 = re.findall('《[^》，；。]+》涉案实用新型', fmt_content_n)
        name_4_2_5 = re.findall('《[^》，；。]+》的实用新型', fmt_content_n)
        # name_4_3 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
        name_4_3_1 = re.findall('《[^》，；。]+》外观', fmt_content_n)
        name_4_3_2 = re.findall('《[^》，；。]+》、外观', fmt_content_n)
        name_4_3_3 = re.findall('《[^》，；。]+》，外观', fmt_content_n)
        name_4_3_4 = re.findall('《[^》，；。]+》涉案外观', fmt_content_n)
        name_4_3_5 = re.findall('《[^》，；。]+》的外观', fmt_content_n)
        # name_4_4 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
        name_4_4_1 = re.findall('《[^》，；。]+》专利', fmt_content_n)
        name_4_4_2 = re.findall('《[^》，；。]+》、专利', fmt_content_n)
        name_4_4_3 = re.findall('《[^》，；。]+》，专利', fmt_content_n)
        name_4_4_4 = re.findall('《[^》，；。]+》涉案专利', fmt_content_n)
        name_4_4_5 = re.findall('《[^》，；。]+》的专利', fmt_content_n)
        # name_4_5 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
        name_4_5_1 = re.findall('《[^》，；。]+》申请', fmt_content_n)
        name_4_5_2 = re.findall('《[^》，；。]+》、申请', fmt_content_n)
        name_4_5_3 = re.findall('《[^》，；。]+》，申请', fmt_content_n)
        name_4_5_4 = re.findall('《[^》，；。]+》涉案申请', fmt_content_n)
        name_4_5_5 = re.findall('《[^》，；。]+》的申请', fmt_content_n)

        # name_5_1 = re.findall('发明名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_1_1 = re.findall('发明《[^》，；。]+》', fmt_content_n)
        name_5_1_2 = re.findall('发明名称《[^》，；。]+》', fmt_content_n)
        name_5_1_3 = re.findall('发明为《[^》，；。]+》', fmt_content_n)
        name_5_1_4 = re.findall('发明名称为《[^》，；。]+》', fmt_content_n)
        # name_5_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_2_1 = re.findall('实用新型《[^》，；。]+》', fmt_content_n)
        name_5_2_2 = re.findall('实用新型名称《[^》，；。]+》', fmt_content_n)
        name_5_2_3 = re.findall('实用新型为《[^》，；。]+》', fmt_content_n)
        name_5_2_4 = re.findall('实用新型名称为《[^》，；。]+》', fmt_content_n)
        # name_5_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_3_1 = re.findall('外观设计《[^》，；。]+》', fmt_content_n)
        name_5_3_2 = re.findall('外观设计名称《[^》，；。]+》', fmt_content_n)
        name_5_3_3 = re.findall('外观设计为《[^》，；。]+》', fmt_content_n)
        name_5_3_4 = re.findall('外观设计名称为《[^》，；。]+》', fmt_content_n)
        # name_5_4 = re.findall('专利名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_4_1 = re.findall('专利《[^》，；。]+》', fmt_content_n)
        name_5_4_2 = re.findall('专利名称《[^》，；。]+》', fmt_content_n)
        name_5_4_3 = re.findall('专利为《[^》，；。]+》', fmt_content_n)
        name_5_4_4 = re.findall('专利名称为《[^》，；。]+》', fmt_content_n)
        # name_5_5 = re.findall('申请名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_5_1 = re.findall('申请《[^》，；。]+》', fmt_content_n)
        name_5_5_2 = re.findall('申请名称《[^》，；。]+》', fmt_content_n)
        name_5_5_3 = re.findall('申请为《[^》，；。]+》', fmt_content_n)
        name_5_5_4 = re.findall('申请名称为《[^》，；。]+》', fmt_content_n)

        name_6_1 = re.findall('名称为《[^》，；。]+》（专利',fmt_content_n)
        name_6_2 = re.findall('名称为《[^》，；。]+》（发明',fmt_content_n)
        name_6_3 = re.findall('名称为《[^》，；。]+》（实用新型',fmt_content_n)
        name_6_4 = re.findall('名称为《[^》，；。]+》（外观设计',fmt_content_n)
        name_6_5 = re.findall('名称为《[^》，；。]+》（申请',fmt_content_n)
        if len(name_1_1_1) > 0:
            for i in name_1_1_1:
                data_name.append(i)
        if len(name_1_1_2) > 0:
            for i in name_1_1_2:
                data_name.append(i)
        if len(name_1_1_3) > 0:
            for i in name_1_1_3:
                data_name.append(i)
        if len(name_1_1_4) > 0:
            for i in name_1_1_4:
                data_name.append(i)
        if len(name_1_1_5) > 0:
            for i in name_1_1_5:
                data_name.append(i)
        if len(name_1_2_1) > 0:
            for i in name_1_2_1:
                data_name.append(i)
        if len(name_1_2_2) > 0:
            for i in name_1_2_2:
                data_name.append(i)
        if len(name_1_2_3) > 0:
            for i in name_1_2_3:
                data_name.append(i)
        if len(name_1_2_4) > 0:
            for i in name_1_2_4:
                data_name.append(i)
        if len(name_1_2_5) > 0:
            for i in name_1_2_5:
                data_name.append(i)
        if len(name_1_3_1) > 0:
            for i in name_1_3_1:
                data_name.append(i)
        if len(name_1_3_2) > 0:
            for i in name_1_3_2:
                data_name.append(i)
        if len(name_1_3_3) > 0:
            for i in name_1_3_3:
                data_name.append(i)
        if len(name_1_3_4) > 0:
            for i in name_1_3_4:
                data_name.append(i)
        if len(name_1_3_5) > 0:
            for i in name_1_3_5:
                data_name.append(i)
        if len(name_1_4_1) > 0:
            for i in name_1_4_1:
                data_name.append(i)
        if len(name_1_4_2) > 0:
            for i in name_1_4_2:
                data_name.append(i)
        if len(name_1_4_3) > 0:
            for i in name_1_4_3:
                data_name.append(i)
        if len(name_1_4_4) > 0:
            for i in name_1_4_4:
                data_name.append(i)
        if len(name_1_4_5) > 0:
            for i in name_1_4_5:
                data_name.append(i)
        if len(name_1_5_1) > 0:
            for i in name_1_5_1:
                data_name.append(i)
        if len(name_1_5_2) > 0:
            for i in name_1_5_2:
                data_name.append(i)
        if len(name_1_5_3) > 0:
            for i in name_1_5_3:
                data_name.append(i)
        if len(name_1_5_4) > 0:
            for i in name_1_5_4:
                data_name.append(i)
        if len(name_1_5_5) > 0:
            for i in name_1_5_5:
                data_name.append(i)
        if len(name_2_1_1) > 0:
            for i in name_2_1_1:
                data_name.append(i)
        if len(name_2_1_2) > 0:
            for i in name_2_1_2:
                data_name.append(i)
        if len(name_2_1_3) > 0:
            for i in name_2_1_3:
                data_name.append(i)
        if len(name_2_1_4) > 0:
            for i in name_2_1_4:
                data_name.append(i)
        if len(name_2_2_1) > 0:
            for i in name_2_2_1:
                data_name.append(i)
        if len(name_2_2_2) > 0:
            for i in name_2_2_2:
                data_name.append(i)
        if len(name_2_2_3) > 0:
            for i in name_2_2_3:
                data_name.append(i)
        if len(name_2_2_4) > 0:
            for i in name_2_2_4:
                data_name.append(i)
        if len(name_2_3_1) > 0:
            for i in name_2_3_1:
                data_name.append(i)
        if len(name_2_3_2) > 0:
            for i in name_2_3_2:
                data_name.append(i)
        if len(name_2_3_3) > 0:
            for i in name_2_3_3:
                data_name.append(i)
        if len(name_2_3_4) > 0:
            for i in name_2_3_4:
                data_name.append(i)
        if len(name_2_4_1) > 0:
            for i in name_2_4_1:
                data_name.append(i)
        if len(name_2_4_2) > 0:
            for i in name_2_4_2:
                data_name.append(i)
        if len(name_2_4_3) > 0:
            for i in name_2_4_3:
                data_name.append(i)
        if len(name_2_4_4) > 0:
            for i in name_2_4_4:
                data_name.append(i)
        if len(name_2_5_1) > 0:
            for i in name_2_5_1:
                data_name.append(i)
        if len(name_2_5_2) > 0:
            for i in name_2_5_2:
                data_name.append(i)
        if len(name_2_5_3) > 0:
            for i in name_2_5_3:
                data_name.append(i)
        if len(name_2_5_4) > 0:
            for i in name_2_5_4:
                data_name.append(i)
        if len(name_3_1) > 0:
            for i in name_3_1:
                data_name.append(i)
        if len(name_3_2) > 0:
            for i in name_3_2:
                data_name.append(i)
        if len(name_3_3) > 0:
            for i in name_3_3:
                data_name.append(i)
        if len(name_3_4) > 0:
            for i in name_3_4:
                data_name.append(i)
        if len(name_3_5) > 0:
            for i in name_3_5:
                data_name.append(i)
        if len(name_4_1_1) > 0:
            for i in name_4_1_1:
                data_name.append(i)
        if len(name_4_1_2) > 0:
            for i in name_4_1_2:
                data_name.append(i)
        if len(name_4_1_3) > 0:
            for i in name_4_1_3:
                data_name.append(i)
        if len(name_4_1_4) > 0:
            for i in name_4_1_4:
                data_name.append(i)
        if len(name_4_1_5) > 0:
            for i in name_4_1_5:
                data_name.append(i)
        if len(name_4_2_1) > 0:
            for i in name_4_2_1:
                data_name.append(i)
        if len(name_4_2_2) > 0:
            for i in name_4_2_2:
                data_name.append(i)
        if len(name_4_2_3) > 0:
            for i in name_4_2_3:
                data_name.append(i)
        if len(name_4_2_4) > 0:
            for i in name_4_2_4:
                data_name.append(i)
        if len(name_4_2_5) > 0:
            for i in name_4_2_5:
                data_name.append(i)
        if len(name_4_3_1) > 0:
            for i in name_4_3_1:
                data_name.append(i)
        if len(name_4_3_2) > 0:
            for i in name_4_3_2:
                data_name.append(i)
        if len(name_4_3_3) > 0:
            for i in name_4_3_3:
                data_name.append(i)
        if len(name_4_3_4) > 0:
            for i in name_4_3_4:
                data_name.append(i)
        if len(name_4_3_5) > 0:
            for i in name_4_3_5:
                data_name.append(i)
        if len(name_4_4_1) > 0:
            for i in name_4_4_1:
                data_name.append(i)
        if len(name_4_4_2) > 0:
            for i in name_4_4_2:
                data_name.append(i)
        if len(name_4_4_3) > 0:
            for i in name_4_4_3:
                data_name.append(i)
        if len(name_4_4_4) > 0:
            for i in name_4_4_4:
                data_name.append(i)
        if len(name_4_4_5) > 0:
            for i in name_4_4_5:
                data_name.append(i)
        if len(name_4_5_1) > 0:
            for i in name_4_5_1:
                data_name.append(i)
        if len(name_4_5_2) > 0:
            for i in name_4_5_2:
                data_name.append(i)
        if len(name_4_5_3) > 0:
            for i in name_4_5_3:
                data_name.append(i)
        if len(name_4_5_4) > 0:
            for i in name_4_5_4:
                data_name.append(i)
        if len(name_4_5_5) > 0:
            for i in name_4_5_5:
                data_name.append(i)
        if len(name_5_1_1) > 0:
            for i in name_5_1_1:
                data_name.append(i)
        if len(name_5_1_2) > 0:
            for i in name_5_1_2:
                data_name.append(i)
        if len(name_5_1_3) > 0:
            for i in name_5_1_3:
                data_name.append(i)
        if len(name_5_1_4) > 0:
            for i in name_5_1_4:
                data_name.append(i)
        if len(name_5_2_1) > 0:
            for i in name_5_2_1:
                data_name.append(i)
        if len(name_5_2_2) > 0:
            for i in name_5_2_2:
                data_name.append(i)
        if len(name_5_2_3) > 0:
            for i in name_5_2_3:
                data_name.append(i)
        if len(name_5_2_4) > 0:
            for i in name_5_2_4:
                data_name.append(i)
        if len(name_5_3_1) > 0:
            for i in name_5_3_1:
                data_name.append(i)
        if len(name_5_3_2) > 0:
            for i in name_5_3_2:
                data_name.append(i)
        if len(name_5_3_3) > 0:
            for i in name_5_3_3:
                data_name.append(i)
        if len(name_5_3_4) > 0:
            for i in name_5_3_4:
                data_name.append(i)
        if len(name_5_4_1) > 0:
            for i in name_5_4_1:
                data_name.append(i)
        if len(name_5_4_2) > 0:
            for i in name_5_4_2:
                data_name.append(i)
        if len(name_5_4_3) > 0:
            for i in name_5_4_3:
                data_name.append(i)
        if len(name_5_4_4) > 0:
            for i in name_5_4_4:
                data_name.append(i)
        if len(name_5_5_1) > 0:
            for i in name_5_5_1:
                data_name.append(i)
        if len(name_5_5_2) > 0:
            for i in name_5_5_2:
                data_name.append(i)
        if len(name_5_5_3) > 0:
            for i in name_5_5_3:
                data_name.append(i)
        if len(name_5_5_4) > 0:
            for i in name_5_5_4:
                data_name.append(i)
        if len(name_6_1) > 0:
            for i in name_6_1:
                data_name.append(i)
        if len(name_6_2) > 0:
            for i in name_6_2:
                data_name.append(i)
        if len(name_6_3) > 0:
            for i in name_6_3:
                data_name.append(i)
        if len(name_6_4) > 0:
            for i in name_6_4:
                data_name.append(i)
        if len(name_6_5) > 0:
            for i in name_6_5:
                data_name.append(i)
        if len(data_name) > 0:
            data_name_set = list(set(data_name))
            test_name = [i for i in data_name_set if i != '']
            test_str_name1 = ';'.join(test_name)
            test_str_name = test_str_name1.replace("'","’")
        else:
            test_str_name = ''

        #商标号和商标名称
        data_Sname = []
        # Sname_1 = re.findall('申请号是{0,1}为{0,1}第{0,1}：{0,1}\d{6,9}号{0,1}', fmt_content_n)
        # Sname_2 = re.findall('注册证{0,1}号是{0,1}为{0,1}第{0,1}：{0,1}\d{6,9}号{0,1}', fmt_content_n)
        # Sname_3 = re.findall('“[^“]+”.{0,3}商标', fmt_content_n)
        # Sname_4 = re.findall('第\d{6,9}号的{0,1}“[^”，；。]+”', fmt_content_n)
        # Sname_5 = re.findall('第\d{6,9}号的{0,1}.*?..{0,3}商标', fmt_content_n)
        # Sname_1 = re.findall('[申注]?[请册]?证?号?是?为?第?：?\d{6,9}号?', fmt_content_n)
        # Sname_2 = re.findall('第\d{6,9}号\w{0,10}[注图文]?[册文字形]?商标', fmt_content_n)
        # Sname_3 = re.findall('“[^”，；。]+”[注图文]?[册文字形]?商标', fmt_content_n)
        # Sname_4 = re.findall('第\d{6,9}号“[^”，；。]+”[注图文]?[册文字形]?商标', fmt_content_n)
        # Sname_5 = re.findall('第\d{6,9}号“[^”，；。\d]+”', fmt_content_n)

        Sname_1_1 = re.findall('申请号是?为?第?：?[^\dLＬlｌNＮｎn]\d{6,9}[^\da-zA-Z]号?',fmt_content_n)
        Sname_1_2 = re.findall('注册证?号是?为?第?：?[^\dLＬlｌNＮｎn]\d{6,9}[^\da-zA-Z]号?',fmt_content_n)
        Sname_2 = re.findall('第\d{6,9}号\w{0,10}[注图文]?[册文字形]?商标', fmt_content_n)
        Sname_3 = re.findall('“[^”，；。]+”[注图文]?[册文字形]?商标', fmt_content_n)
        Sname_4 = re.findall('第\d{6,9}号“[^”，；。]+”[注图文]?[册文字形]?商标', fmt_content_n)
        Sname_5 = re.findall('第\d{6,9}号“[^”，；。\d]+”', fmt_content_n)
        if len(Sname_1_1) > 0:
            for i in Sname_1_1:
                data_Sname.append(i)
        if len(Sname_1_2) > 0:
            for i in Sname_1_2:
                data_Sname.append(i)
        if len(Sname_2) > 0:
            for i in Sname_2:
                data_Sname.append(i)
        if len(Sname_3) > 0:
            for i in Sname_3:
                data_Sname.append(i)
        if len(Sname_4) > 0:
            for i in Sname_4:
                data_Sname.append(i)
        if len(Sname_5) > 0:
            for i in Sname_5:
                data_Sname.append(i)
        if len(data_Sname) > 0:
            data_Sname_set = list(set(data_Sname))
            test_Sname = [i for i in data_Sname_set if i != '']
            test_str_Sname1 = ';'.join(test_Sname)
            test_str_Sname = test_str_Sname1.replace("'","‘")
        else:
            test_str_Sname = ''




        data_public_patent = []
        public_num_patent = re.findall('[CcＣｃ][NnＮｎ][1-3]\d{5,9}[ABUSCDY][1-9]{0,1}',fmt_content_n)
        if len(public_num_patent) > 0:
            for i in public_num_patent:
                data_public_patent.append(i)
        if len(data_public_patent) > 0:
            data_public_patent_set = list(set(data_public_patent))
            test_public_num_patent = [i for i in data_public_patent_set if i != '']
            test_str_public_num_patent = ';'.join(test_public_num_patent)
        else:
            test_str_public_num_patent = ''

        data_public_shangbiao = []
        public_num_shangbiao = re.findall('G\d{6,9}[A-Z]{0,2}',fmt_content_n)
        if len(public_num_shangbiao) > 0:
            for i in public_num_shangbiao:
                data_public_shangbiao.append(i)
        if len(data_public_shangbiao) > 0:
            data_public_shangbiao_set = list(set(data_public_shangbiao))
            test_public_num_shangbiao = [i for i in data_public_shangbiao_set if i != '']
            test_str_public_num_shangbiao = ';'.join(test_public_num_shangbiao)
        else:
            test_str_public_num_shangbiao = ''



        # '''
        # declare a_clob clob:='1111'; begin insert into  judgement_table(FMT_CONTENT) values (a_clob); end;
        # '''
        # sql1 = "declare a_clob clob:='{}'".format(fmt_content)
        # sql2 = "begin"
        sql = "insert into jugement_table_0728_re values ('{}','{}','{}','{}','{}','{}','{}')".format(case_id,case_reason,test_str_num,test_str_name,test_str_Sname,test_str_public_num_patent,test_str_public_num_shangbiao)
        # sql4 = "end"
        # sql = "declare" \
        #       "a_clob clob:='{}';" \
        #       "begin" \
        #       "insert into judgement_table values ('{}','{}',{},'{}','{}','{}');" \
        #       "end".format(fmt_content,case_id,case_reason,'a_clob',test_str_num,test_str_name,test_str_Sname)

        db.execute_sql(sql)
        num+=1
        print('已筛选',num,'条')
    except Exception as e:
        num+=1
        with open('log.txt','a',encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')




