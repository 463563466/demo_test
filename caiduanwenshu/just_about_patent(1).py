# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re
from tqdm import tqdm

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
class just_about_patent(object):

    def __init__(self):
        self.fmt_content_n = ''
        self.case_name = ''
        self.case_reason = ''
        self.db = OracleOperation()
        self.db1 = OracleOperation()
        self.patent_count = 0
        self.caiding_count = 0
        self.null_count = 0
        self.panjue_count = 0
        self.all_count = 0

    def com_true(self):
        #知识产权、专利、发明、实用新型、外观设计、设计人
        keyword = ['知识产权','专利','发明','实用新型','外观设计','设计人']
        for key in keyword:
            if key not in self.case_name and key not in self.case_reason:
                continue
            else:
                self.patent_count+=1
                self.re_name(self.case_name,self.fmt_content_n)
                patent_num = self.re_patent_num()
                patent_name = self.re_patent_name()
                public_num = self.re_public_num()
                data = {}
                data["patent_num"] = patent_num
                data["patent_name"] = patent_name
                data["public_num"] = public_num
                return data

    def re_name(self,case_name,fmt_content):
        #替换特殊符号
        fmt_content_r = fmt_content.replace('&amp;', '&').replace('&times;', '×').replace('&ldquo;', '“'). \
            replace('&rdquo;', '”').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '“'). \
            replace('&hellip;', '…').replace('&middot;', '·').replace('&mdash;', '—').replace('&nbsp;', ' ').\
            replace('01lydyh01','"')
        #如果case_name中包含’裁定‘两个字，不用走限定
        keyword = '裁定'
        if keyword not in case_name:
            #先删除参考文献
            #获取文章长度的35%
            length = int(round(len(fmt_content_r) * 0.35,0))
            length_35_after = fmt_content_r[length:]
            wenxian = re.findall('参考文献.*', length_35_after)
            wenxianstr = ''.join(wenxian)
            fujian = re.findall('附件.*', length_35_after)
            fujianstr = ''.join(fujian)
            duibi = re.findall('对比文件.*', length_35_after)
            duibistr = ''.join(duibi)
            kangbian = re.findall('现有技术抗辩.*', length_35_after)
            kangbianstr = ''.join(kangbian)
            zhengju = re.findall('证据.*', length_35_after)
            zhengjustr = ''.join(zhengju)
            self.fmt_content_n = fmt_content_r.replace(wenxianstr,'').replace(fujianstr,'').replace(duibistr,'').replace(kangbianstr,'').replace(zhengjustr,'')
        else:
            self.caiding_count+=1
            self.fmt_content_n = fmt_content_r

    def re_patent_num(self):
        fmt_content_n = self.fmt_content_n
        #8开头
        num_1_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_1_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?',fmt_content_n)
        num_1_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_1_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号',fmt_content_n)

        # 9开头
        num_2_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_2_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?',fmt_content_n)
        num_2_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_2_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号',fmt_content_n)

        #0开头
        num_3_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_3_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?',fmt_content_n)
        num_3_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_3_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5}\.?[\dＸｘXx×]?号',fmt_content_n)

        #200x
        num_4_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_4_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?',fmt_content_n)
        num_4_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_4_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号',fmt_content_n)

        #201x
        num_5_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_5_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?',fmt_content_n)
        num_5_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_5_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号',fmt_content_n)

        #2020
        num_6_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?)',fmt_content_n)
        num_6_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?',fmt_content_n)
        num_6_3 = re.findall('[^\d]([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号?、?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》])',fmt_content_n)
        num_6_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7}\.?[\dＸｘXx×]?号',fmt_content_n)

        #全部匹配
        num_7_1 = re.findall('专利号?为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_2 = re.findall('申请号?为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_3 = re.findall('外观设计为?是?\s?:?([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        num_7_4 = re.findall('发明为?是?\s?:?([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        num_7_5 = re.findall('实用新型为?是?\s?:?([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        num_7_6 = re.findall('涉案为?是?\s?:?([ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        num_7_7 = re.findall('[^a-zA-Z]([ZＺzｚCＣｃc][LＬlｌNＮｎn][\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        # num_7_1 = re.findall('[^\dLＬlｌNＮｎn]([\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        # num_7_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]{8,12}\.?[\dＸｘXx×]?',fmt_content_n)
        # num_7_3 = re.findall('[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?号?、?名?称?为?[‘“"《][^”，；。《]+[’”"》]',fmt_content_n)
        # num_7_4 = re.findall('[‘“"《][^”，；。《]+[’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?号',fmt_content_n)

        #拼接并去重
        data_num = num_1_1 + num_1_2 + num_1_3 + num_1_4 + \
                   num_2_1 + num_2_2 + num_2_3 + num_2_4 + \
                   num_3_1 + num_3_2 + num_3_3 + num_3_4 + \
                   num_4_1 + num_4_2 + num_4_3 + num_4_4 + \
                   num_5_1 + num_5_2 + num_5_3 + num_5_4 + \
                   num_6_1 + num_6_2 + num_6_3 + num_6_4 + \
                   num_7_1 + num_7_2 + num_7_3 + num_7_4 + \
                   num_7_5 + num_7_6 + num_7_7
        if len(data_num) > 0:
            data_num_set = list(set(data_num))
            test_num = [i for i in data_num_set if i != '']
            test_str_num = ';'.join(test_num)
        else:
            test_str_num = ''
        return test_str_num

    def re_patent_name(self):
        fmt_content_n = self.fmt_content_n
        # 发明
        #[”‘“"《][^”"’“‘，；。《]+[“’”"》]\w{0,2}专利
        #[”‘“"《][^”"’“‘，；。《]+[“’”"》]\w{0,2}发明
        #[”‘“"《][^”"’“‘，；。《]+[“’”"》]\w{0,2}实用新型
        #[”‘“"《][^”"’“‘，；。《]+[“’”"》]\w{0,2}外观
        #[”‘“"《][^”"’“‘，；。《]+[“’”"》]\w{0,2}申请
        #名称？为？[”‘“"《][^”"’“‘，；。《]+[“’”"》]
        #名称？为？\w[^。]+[的、，（(]\w{0,2}发明
        name_1_1 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》][，、]?\w{0,2}专利',fmt_content_n)
        name_1_2 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》][，、]?\w{0,2}发明',fmt_content_n)
        name_1_3 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》][，、]?\w{0,2}实用新型',fmt_content_n)
        name_1_4 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》][，、]?\w{0,2}外观',fmt_content_n)
        name_1_5 = re.findall('[”‘“"《][^”"’“‘，；。《]+[“’”"》][，、]?\w{0,2}申请',fmt_content_n)

        name_1_1_1 = re.findall('[”‘“"《][^”，；。《]+[“’”"》][，、]?\w{0,2}专利',fmt_content_n)
        name_1_1_2 = re.findall('[”‘“"《][^”，；。《]+[“’”"》][，、]?\w{0,2}发明',fmt_content_n)
        name_1_1_3 = re.findall('[”‘“"《][^”，；。《]+[“’”"》][，、]?\w{0,2}实用新型',fmt_content_n)
        name_1_1_4 = re.findall('[”‘“"《][^”，；。《]+[“’”"》][，、]?\w{0,2}外观',fmt_content_n)
        name_1_1_5 = re.findall('[”‘“"《][^”，；。《]+[“’”"》][，、]?\w{0,2}申请',fmt_content_n)

        name_2_1 = re.findall('发明名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)
        name_2_2 = re.findall('专利名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)
        name_2_3 = re.findall('实用新型名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)
        name_2_4 = re.findall('外观设?计?名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)
        name_2_5 = re.findall('申请名?称?为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)

        name_2_1_1 = re.findall('发明名?称?为?[”‘“"《][^”，；。《]+[“’”"》]', fmt_content_n)
        name_2_2_2 = re.findall('专利名?称?为?[”‘“"《][^”，；。《]+[“’”"》]', fmt_content_n)
        name_2_3_3 = re.findall('实用新型名?称?为?[”‘“"《][^”，；。《]+[“’”"》]', fmt_content_n)
        name_2_4_4 = re.findall('外观设?计?名?称?为?[”‘“"《][^”，；。《]+[“’”"》]', fmt_content_n)
        name_2_5_5 = re.findall('申请名?称?为?[”‘“"《][^”，；。《]+[“’”"》]', fmt_content_n)

        name_3_1 = re.findall('名称为?[”‘“"《][^”"’“‘，；。《]+[“’”"》]',fmt_content_n)
        name_3_1_1 = re.findall('名称为?[”‘“"《][^”，；。《]+[“’”"》]',fmt_content_n)

        name_3_2 = re.findall('名称为?\w[^。”；"’“‘]+[的、，（(]?\w{0,2}发明',fmt_content_n)
        name_3_3 = re.findall('名称为?\w[^。”；"’“‘]+[的、，（(]?\w{0,2}专利',fmt_content_n)
        name_3_4 = re.findall('名称为?\w[^。”；"’“‘]+[的、，（(]?\w{0,2}实用新型',fmt_content_n)
        name_3_5 = re.findall('名称为?\w[^。”；"’“‘]+[的、，（(]?\w{0,2}外观',fmt_content_n)
        name_3_6 = re.findall('名称为?\w[^。”；"’“‘]+[的、，（(]?\w{0,2}申请',fmt_content_n)

        name_4_1 = re.findall('名为\w[^。”；"’“‘]+[的、，（(]?\w{0,2}发明', fmt_content_n)
        name_4_2 = re.findall('名为\w[^。”；"’“‘]+[的、，（(]?\w{0,2}专利', fmt_content_n)
        name_4_3 = re.findall('名为\w[^。”；"’“‘]+[的、，（(]?\w{0,2}实用新型', fmt_content_n)
        name_4_4 = re.findall('名为\w[^。”；"’“‘]+[的、，（(]?\w{0,2}外观', fmt_content_n)
        name_4_5 = re.findall('名为\w[^。”；"’“‘]+[的、，（(]?\w{0,2}申请', fmt_content_n)

        data_name = name_1_1 + name_1_2 + name_1_3 + name_1_4 + name_1_5 + \
                    name_1_1_1 + name_1_1_2 + name_1_1_3 + name_1_1_4 + name_1_1_5 + \
                    name_2_1 + name_2_2 + name_2_3 + name_2_4 + name_2_5 + \
                    name_2_1_1 + name_2_2_2 + name_2_3_3 + name_2_4_4 + name_2_5_5 + \
                    name_3_1 + name_3_1_1 + name_3_2 + name_3_3 + name_3_4 + \
                    name_3_5 + name_3_6 + name_4_1 + name_4_2 + name_4_3 + \
                    name_4_4 + name_4_5
        if len(data_name) > 0:
            data_name_set = list(set(data_name))
            test_name = [i for i in data_name_set if i != '']
            test_str_name = ';'.join(test_name)
        else:
            test_str_name = ''
        return test_str_name

    def re_public_num(self):
        fmt_content_n = self.fmt_content_n
        public_num_patent = re.findall('[CcＣｃ][NnＮｎ][1-3]\d{5,9}[ABUSCDY]?[1-9]?', fmt_content_n)
        if len(public_num_patent) > 0:
            data_public_patent_set = list(set(public_num_patent))
            test_public_num_patent = [i for i in data_public_patent_set if i != '']
            test_str_public_num_patent = ';'.join(test_public_num_patent)
        else:
            test_str_public_num_patent = ''
        return test_str_public_num_patent

    def _sqlexe(self):
        self.db.execute_sql('select count(*) from jugement_table_0807')
        count_bar = self.db.get_one()[0]
        _bar = tqdm(total=count_bar)
        self.db.execute_sql('select * from jugement_table_0807')
        while True:
            data = self.db.get_one()
            _bar.update(1)
            if not data:
                break
            self.all_count+=1
            self.case_id = data[0]
            self.case_name = data[1]
            if self.case_name == None:
                self.case_name = ''
            self.case_reason = data[2]
            if self.case_reason == None:
                self.case_reason = ''
            fmt_content_clob = data[3]
            if fmt_content_clob == None:
                self.null_count+=1
                continue
            else:
                self.fmt_content_n = fmt_content_clob.read()
                data_patent = self.com_true()
                if data_patent == None:
                    self.panjue_count+=1
                    continue
                patent_num = data_patent["patent_num"]
                patent_name = data_patent["patent_name"]
                public_num = data_patent["public_num"]
            sql = "insert into jugement_table_0807_re1 values ('{}','{}','{}','{}','{}','{}')"\
                .format(self.case_id,self.case_reason,patent_num,patent_name,public_num,self.case_name)
            try:
                self.db1.execute_sql(sql)
            except:
                with open('0807.txt', 'a', encoding='utf-8') as a:
                    a.write(self.case_id)
                    a.write('\n')


    def run(self):
        self._sqlexe()
        print('共',self.all_count,'条','--','专利文书数量',self.patent_count,'--','裁定文书数量',self.caiding_count,'--','判决文书等数量',self.panjue_count,'--','文书为空数量',self.null_count)
















class Patent_num(object):
    def __init__(self):
        self.db = OracleOperation()
        self.db1 = OracleOperation()
        self.case_id = ''
        self.clear_one = ''
        self.clear_one_name = ''
        self.case_reason = ''
        self.case_name = ''
        self.num = 0

    def _sqlexe_num(self):
        self.db.execute_sql("select count(*)  from jugement_table_0807_re_qx where identify='专利号'")
        count_bar = self.db.get_one()[0]
        _bar = tqdm(total=count_bar)
        self.db.execute_sql("select * from jugement_table_0807_re_qx where identify='专利号'")
        while True:
            data = self.db.get_one()
            _bar.update(1)
            if not data:
                _bar.close()
                break
            self.case_id = data[0]
            self.case_reason = data[1]
            self.case_name = data[2]
            self.clear_one = data[3]
            re_patent_num = self.re_num()
            try:
                sql1 = "insert into  jugement_table_0807_re_qx_bei values ('{}','{}','{}','{}','专利号','{}')".format(self.case_id,self.case_reason,
                                                                                                                   self.case_name,self.clear_one,re_patent_num)
                self.db1.execute_sql(sql1)
                self.num+=1
            except:
                with open('0807.txt','a',encoding='utf-8') as e:
                    e.write(self.case_id)
                    e.write('\n')

    def _sqlexe_name(self):
        self.db.execute_sql("select count(*)  from jugement_table_0807_re_qx where identify='专利名称'")
        count_bar = self.db.get_one()[0]
        _bar = tqdm(total=count_bar)
        self.db.execute_sql("select * from jugement_table_0807_re_qx where identify='专利名称'")
        while True:
            data = self.db.get_one()
            _bar.update(1)
            if not data:
                _bar.close()
                break
            self.case_id = data[0]
            self.case_reason = data[1]
            self.case_name = data[2]
            self.clear_one_name = data[3]
            re_patent_num = self.re_name()
            try:
                sql1 = "insert into  jugement_table_0807_re_qx_name values ('{}','{}','{}','{}','专利名称','{}')".format(
                    self.case_id, self.case_reason,
                    self.case_name, self.clear_one_name, re_patent_num)
                self.db1.execute_sql(sql1)
                self.num += 1
            except:
                with open('0807.txt', 'a', encoding='utf-8') as e:
                    e.write(self.case_id)
                    e.write('\n')

    def re_num(self):
        fmt_content_n = self.clear_one
        #8开头
        num_1_1 = re.findall('(^[8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_1_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_1_3 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        num_1_4 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([8ＸｘXx×][5-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)

        # 9开头
        num_2_1 = re.findall('(^[9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_2_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_2_3 = re.findall('([^\dLＬlｌNＮｎnＸｘXx×][9ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)

        #0开头
        num_3_1 = re.findall('(^[0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_3_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)
        num_3_3 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([0ＸｘXx×][0-3ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{5})\.?[\dＸｘXx×]?',fmt_content_n)

        #200x
        num_4_1 = re.findall('(^[2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_4_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_4_3 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][0ＸｘXx×][3-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)

        #201x
        num_5_1 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_5_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_5_3 = re.findall('(^[2ＸｘXx×][0ＸｘXx×][1ＸｘXx×][0-9ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)

        #2020
        num_6_1 = re.findall('(^[2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_6_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]([2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)
        num_6_3 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([2ＸｘXx×][0ＸｘXx×][2ＸｘXx×][0ＸｘXx×][12389ＸｘXx×][\dＸｘXx×]{7})\.?[\dＸｘXx×]?',fmt_content_n)

        #全部匹配
        num_7_1 = re.findall('专利号?为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_2 = re.findall('申请号?为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_3 = re.findall('外观设计为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_4 = re.findall('发明为?是?\s?:?ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_5 = re.findall('实用新型为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_6 = re.findall('涉案为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_7 = re.findall('[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)
        num_7_8 = re.findall('[^\dLＬlｌNＮｎnＸｘXx×]([\dＸｘXx×]{8,12})\.?[\dＸｘXx×]?', fmt_content_n)


        # num_7_1 = re.findall('[^\dLＬlｌNＮｎn]([\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?)', fmt_content_n)
        # num_7_2 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]{8,12}\.?[\dＸｘXx×]?',fmt_content_n)
        # num_7_3 = re.findall('[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?号?、?名?称?为?[‘“"《][^”，；。《]+[’”"》]',fmt_content_n)
        # num_7_4 = re.findall('[‘“"《][^”，；。《]+[’”"》]的?第[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[\dＸｘXx×]{8,12}\.?[\dＸｘXx×]?号',fmt_content_n)

        #拼接并去重
        data_num = num_1_1 + num_1_2 + num_1_4 + \
                   num_2_1 + num_2_2 + num_2_3 + \
                   num_3_1 + num_3_2 + num_3_3 + \
                   num_4_1 + num_4_2 + num_4_3 + \
                   num_5_1 + num_5_2 + num_5_3 + \
                   num_6_1 + num_6_2 + num_6_3 + \
                   num_7_1 + num_7_2 + num_7_3 + num_7_4 + \
                   num_7_5 + num_7_6 + num_7_7 + num_7_8
        if len(data_num) > 0:
            data_num_set = list(set(data_num))
            test_num = []
            for i in data_num_set:
                if len(i) > 12:
                    i.replace(i[12:],'')
                    test_num.append(i)
                else:
                    test_num.append(i)
            test_num_add = test_num + num_1_3
            test_str_num = ';'.join(test_num_add)
        else:
            test_str_num = ''
        return test_str_num

    def re_name(self):
        fmt_content_n = self.clear_one_name
        name_1_1 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》][，、]?\w{0,2}专利',fmt_content_n)
        name_1_2 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》][，、]?\w{0,2}发明',fmt_content_n)
        name_1_3 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》][，、]?\w{0,2}实用新型',fmt_content_n)
        name_1_4 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》][，、]?\w{0,2}外观',fmt_content_n)
        name_1_5 = re.findall('[”‘“"《]([^”"’“‘，；。《]+)[“’”"》][，、]?\w{0,2}申请',fmt_content_n)

        name_1_1_1 = re.findall('[”‘“"《]([^”，；。《]+)[“’”"》][，、]?\w{0,2}专利',fmt_content_n)
        name_1_1_2 = re.findall('[”‘“"《]([^”，；。《]+)[“’”"》][，、]?\w{0,2}发明',fmt_content_n)
        name_1_1_3 = re.findall('[”‘“"《]([^”，；。《]+)[“’”"》][，、]?\w{0,2}实用新型',fmt_content_n)
        name_1_1_4 = re.findall('[”‘“"《]([^”，；。《]+)[“’”"》][，、]?\w{0,2}外观',fmt_content_n)
        name_1_1_5 = re.findall('[”‘“"《]([^”，；。《]+)[“’”"》][，、]?\w{0,2}申请',fmt_content_n)

        name_2_1 = re.findall('发明名?称?为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        name_2_2 = re.findall('专利名?称?为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        name_2_3 = re.findall('实用新型名?称?为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        name_2_4 = re.findall('外观设?计?名?称?为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        name_2_5 = re.findall('申请名?称?为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)

        name_2_1_1 = re.findall('发明名?称?为?[”‘“"《]([^”，；。《]+)[“’”"》]', fmt_content_n)
        name_2_2_2 = re.findall('专利名?称?为?[”‘“"《]([^”，；。《]+)[“’”"》]', fmt_content_n)
        name_2_3_3 = re.findall('实用新型名?称?为?[”‘“"《]([^”，；。《]+)[“’”"》]', fmt_content_n)
        name_2_4_4 = re.findall('外观设?计?名?称?为?[”‘“"《]([^”，；。《]+)[“’”"》]', fmt_content_n)
        name_2_5_5 = re.findall('申请名?称?为?[”‘“"《]([^”，；。《]+)[“’”"》]', fmt_content_n)

        name_3_1 = re.findall('名称为?[”‘“"《]([^”"’“‘，；。《]+)[“’”"》]',fmt_content_n)
        name_3_1_1 = re.findall('名称为?[”‘“"《]([^”，；。《]+)[“’”"》]',fmt_content_n)

        name_3_2 = re.findall('名称为?([^。”；"’“‘]+)[的、，（(]?\w{0,2}发明',fmt_content_n)
        name_3_3 = re.findall('名称为?([^。”；"’“‘]+)[的、，（(]?\w{0,2}专利',fmt_content_n)
        name_3_4 = re.findall('名称为?([^。”；"’“‘]+)[的、，（(]?\w{0,2}实用新型',fmt_content_n)
        name_3_5 = re.findall('名称为?([^。”；"’“‘]+)[的、，（(]?\w{0,2}外观',fmt_content_n)
        name_3_6 = re.findall('名称为?([^。”；"’“‘]+)[的、，（(]?\w{0,2}申请',fmt_content_n)

        name_4_1 = re.findall('名为([^。”；"’“‘]+)[的、，（(]?\w{0,2}发明', fmt_content_n)
        name_4_2 = re.findall('名为([^。”；"’“‘]+)[的、，（(]?\w{0,2}专利', fmt_content_n)
        name_4_3 = re.findall('名为([^。”；"’“‘]+)[的、，（(]?\w{0,2}实用新型', fmt_content_n)
        name_4_4 = re.findall('名为([^。”；"’“‘]+)[的、，（(]?\w{0,2}外观', fmt_content_n)
        name_4_5 = re.findall('名为([^。”；"’“‘]+)[的、，（(]?\w{0,2}申请', fmt_content_n)

        data_name = name_1_1 + name_1_2 + name_1_3 + name_1_4 + name_1_5 + \
                    name_1_1_1 + name_1_1_2 + name_1_1_3 + name_1_1_4 + name_1_1_5 + \
                    name_2_1 + name_2_2 + name_2_3 + name_2_4 + name_2_5 + \
                    name_2_1_1 + name_2_2_2 + name_2_3_3 + name_2_4_4 + name_2_5_5 + \
                    name_3_1 + name_3_1_1 + name_3_2 + name_3_3 + name_3_4 + \
                    name_3_5 + name_3_6 + name_4_1 + name_4_2 + name_4_3 + \
                    name_4_4 + name_4_5
        if len(data_name) > 0:
            data_name_set = list(set(data_name))
            test_name = [i for i in data_name_set if i != '']
            test_str_name = ';'.join(test_name)
        else:
            test_str_name = ''
        return test_str_name

    def run(self):
        # self._sqlexe_num()
        self._sqlexe_name()
        print('已完成共',self.num,'条')



if __name__ == '__main__':
    print('开始--------')
    # _re = just_about_patent()
    # _re. run()
    _re = Patent_num()
    _re.run()


