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

    def __init__(self,fmt_content_n,case_name,case_reason,patent_count,caiding_count):
        self.fmt_content_n = fmt_content_n
        self.case_name = case_name
        self.case_reason = case_reason
        self.patent_count = patent_count
        self.caiding_count = caiding_count


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



    def sql_name(self):
        data_count = {}
        data_count["patent_count"] = self.patent_count
        data_count["caiding_count"] = self.caiding_count
        return data_count

    def run(self):
        data = self.com_true()
        return data

if __name__ == '__main__':
    db = OracleOperation()
    db1 = OracleOperation()
    db.execute_sql('select count(*) from jugement_table_0807')
    count_bar = db.get_one()[0]
    # _bar = tqdm(total=count_bar)
    db.execute_sql('select * from jugement_table_0807')
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
        # _bar.update(1)
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
                print('共',all_count,'条','--','专利文书数量',patent_count,'--','裁定文书数量',caiding_count,'--','判决文书等数量',panjue_count,'--','文书为空数量',null_count)
            # _bar.close()
        except Exception as e :
            with open('0807.txt','a',encoding='utf-8') as a:
                a.write(case_id)
                a.write('\n')


# if __name__ == '__main__':
#     db = OracleOperation()
#     null_count = 0
#     panjue_count = 0
#     all_count = 0
#     caiding_count = 0
#     patent_count = 0
#     case_id = '006be9987056092a92e5e49df4ef889f0'
#     fmt_content = '乐腾达（深圳）日用品有限公司与永康市锋达五金工具厂、浙江天猫网络有限公司确认不侵害商标权纠纷一审民事裁定书广东省深圳市福田区人民法院民 事 裁 定 书（2016）粤0304民初23278号原告乐腾达（深圳）日用品有限公司，住所地广东省深圳市福田区。法定代表人郭振威，执行董事。被告永康市锋达五金工具厂，住所地浙江省永康市。法定代表人杜岩宣，厂长。委托代理人熊仙凤，浙江杭知桥律师事务所律师。被告浙江天猫网络有限公司，住所地浙江省杭州市余杭区。法定代表人陆兆禧。原告乐腾达（深圳）日用品有限公司诉被告永康市锋达五金工具厂、浙江天猫网络有限公司确认不侵害商标权纠纷一案，本院于2016年9月30日立案。原告乐腾达（深圳）日用品有限公司诉称，原告是国内专业生产防噪音耳塞、眼罩、颈枕、慢回弹枕头、腰垫等睡眠护理产品的大型生产商，目前拥有自有品牌&ldquo;零听&rdquo;、&ldquo;圆目&rdquo;等。原告产品在全国各大药房以及沃尔玛、家乐福、华润万家等多家商场超市以及天猫、京东、亚马逊、当当网、一号店等电商平台占有很高的市场份额，已经成为睡眠护理产品的领头企业。原告于2010年10月19日就已在《类似商品和服务区分表》第九类上申请注册&ldquo;圆目&rdquo;商标，核定使用范围包括&ldquo;遮光眼罩&rdquo;等，专用权期间自2011年10月28日至2021年10月27日。被告永康市锋达五金工具厂于2012年11月5日在第二十五类上申请注册&ldquo;圆目&rdquo;商标，核定使用范围包括&ldquo;睡眠用眼罩&rdquo;等，专用权期间自2014年4月7日至2024年4月6日。目前原告已经针对被告永康市锋达五金工具厂&ldquo;圆目&rdquo;商标向国家工商行政管理总局商标评审委员会提出无效宣告申请。被告永康市锋达五金工具厂商标指定使用的商品&ldquo;遮光眼罩&rdquo;与原告商标指定使用商品&ldquo;遮光眼罩&rdquo;在功能和用途、销售渠道、销售对象、消费群体等方面均相同。2016年7月5日被告永康市锋达五金工具厂向被告浙江天猫网络有限公司投诉称：原告及经销商在被告浙江天猫网络有限公司处销售的&ldquo;遮光眼罩&rdquo;商品侵犯其第11698248号&ldquo;圆目sleepeasy&rdquo;注册商标专用权，投诉编号：3205789。原告收到被告浙江天猫网络有限公司的通知后分别于2016年8月30日、9月6日两次予以申诉，但被告浙江天猫网络有限公司仍强行将原告商品予以下架处理。经原告检索，国内多家知名眼罩产品生产商都将商标在第9类&ldquo;遮光眼罩&rdquo;商品上申请注册；与此相对，被告永康市锋达五金工具厂在第25类上抢注上述企业的知名商标，主观恶意极其明显。原告认为被告永康市锋达五金工具厂的投诉、被告浙江天猫网络有限公司未经核实强行将原告商品链接下架，严重干扰了原告的正常经营状态，故原告请求法院判令：1、确认原告不侵犯被告永康市锋达五金工具厂注册的第11698248号&ldquo;圆目sleepeasy&rdquo;注册商标权；2、在确认原告不侵犯被告永康市锋达五金工具厂商标权的基础上，被告浙江天猫网络有限公司立即恢复原告产品链接；3、被告承担诉讼合理开支4万元。被告永康市锋达五金工具厂在提交答辩状期间，对管辖权提出异议认为，本案为确认不侵害商标权纠纷，在诉讼管辖法院的确定上与侵害商标专用权纠纷无异。本案中，我方投诉系针对原告未经许可，在其经营的天猫（即被告浙江天猫网络有限公司平台）店铺链接所展示的内容中使用我方第11698248号&ldquo;圆目sleepeasy&rdquo;商标，侵害我方注册商标专用权的行为。本案侵权行为地为实施前述侵权行为的网络服务器、计算机终端等设备所在地，即被告浙江天猫网络有限公司住所地浙江省杭州市余杭区文一西路969号。因我方所指称的侵权行为提起相关的确认不侵权之诉，根据《最高人民法院关于审理商标民事纠纷案件适用法律若干问题的解释》第六条的规定，&ldquo;因侵犯注册商标专用权行为提起的民事诉讼，由商标法第十三条、第五十二条所规定侵权行为的实施地、侵权商品的储藏地或者查封扣押地、被告住所地人民法院管辖。前款规定的侵权商品的储藏地，是指大量或者经常性储存、隐匿侵权商品所在地；查封扣押地，是指海关、工商等行政机关依法查封、扣押侵权商品所在地&rdquo;，原告未举证侵权商品的储藏地，且本案不存在查封扣押地，应当适用侵权行为实施地或被告住所地确定管辖权。其次，遵循方便诉讼当事人、节约司法成本和提高审判效率等审理原则，本案移送浙江省杭州市余杭区人民法院管辖更为经济便利。综上，本案不应由深圳市福田区人民法院管辖，请求将本案移送至有管辖权的浙江省杭州市余杭区人民法院审理。本院经审查认为，本案为确认不侵害商标权纠纷，属于侵权类纠纷。根据《中华人民共和国民事诉讼法》第二十八条的规定，&ldquo;因侵权行为提起的诉讼，由侵权行为地或者被告住所地人民法院管辖&rdquo;，《民诉解释》第二十四条规定，&ldquo;民事诉讼法第二十八条规定的侵权行为地，包括侵权行为实施地、侵权结果发生地&rdquo;,第二十五条规定，&ldquo;信息网络侵权行为实施地包括实施被诉侵权行为的计算机设备所在地，侵权结果发生地包括被侵权人住所地&rdquo;。本案中，被告永康市锋达五金工具厂主张原告在其经营的天猫店铺中销售的&ldquo;遮光眼罩&rdquo;商品侵犯其注册商标专用权，原告要求法院确认原告涉案行为不侵权，原告住所地即侵权结果发生地。原告住所地位于深圳市福田区，故原告向本院提起诉讼符合法律规定，本院依法对本案享有管辖权。依照《中华人民共和国民事诉讼法》第二十八条、第一百二十七条第一款、《最高人民法院关于适用&lt;中华人民共和国民事诉讼法&gt;的解释》第二十四条、第二十五条的规定，裁定如下：驳回被告永康市锋达五金工具厂对本案管辖权提出的异议。如不服本裁定，可以在裁定书送达之日起十日内（涉外、涉港澳台当事人可在裁定书送达之日起三十日内），向本院递交上诉状，并按对方当事人或者代表人的人数提出副本，上诉于广东省深圳市中级人民法院。审　判　长　　魏　巍人民陪审员　　李宏新人民陪审员　　张艳荣二〇一六年十一月二十一日本件与原本核对无异书　记　员　　朱淑乔'
#     case_name = '乐腾达（深圳）日用品有限公司与永康市锋达五金工具厂、浙江天猫网络有限公司确认不侵害商标权纠纷一审民事裁定书'
#     case_reason = ''
#     run = just_about_patent(fmt_content, case_name, case_reason,patent_count,caiding_count)
#     data = run.run()
#     if data == None:
#         print(data)
#     patent_num = data["patent_num"]
#     patent_name = data["patent_name"]
#     public_num = data["public_num"]
#     sql = "insert into jugement_table_0807_re values ('{}','{}','{}','{}','{}','{}')".format(case_id,case_reason,patent_num,patent_name,public_num,case_name)
#     db.execute_sql(sql)
#     data_count = run.sql_name()
#     patent_count = data_count["patent_count"]
#     caiding_count = data_count["caiding_count"]
#     print('已插入',all_count,'条','--','专利文书数量',patent_count,'--','裁定文书数量',caiding_count,'--','判决文书等数量',panjue_count,'--','文书为空数量',null_count)