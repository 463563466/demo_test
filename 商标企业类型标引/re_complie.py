import re

class Reg_complie(object):

    def __init__(self):
        self.enterprise_one = ['厂','苑','店','坊','园','场','屋','行','庄','阁','业','号','室','馆','社']
        self.enterprise_two_after = ['公司','集团','企业','会社','公社','商行','银行']
        self.enterprise_two_front = ['公司','集团','企业','会社','公社','商行','银行']
        self.enterprise_three_ = ['合作社','艺术团','企业','会社','公社']
        self.enterprise_four = ['株式会社',]

    def no_personal(self,reg_namecn):
        #按照优先级进行匹配
        #特殊
        if reg_namecn == '中国人民银行':
            reg_namecn_type = '事业单位'
            return reg_namecn_type
        #一
        if reg_namecn[-2:] in ['公司','集团','企业','会社','公社','商行','银行'] or reg_namecn[-3:] in ['合作社','艺术团','企业','会社','公社']:
            reg_namecn_type = '企业'
            return reg_namecn_type
        # 二
        if reg_namecn[:4] == '株式会社' or reg_namecn.find('有限') != -1 or reg_namecn.find('（株）') != -1 or reg_namecn.find('(株)') != -1 or reg_namecn.find('(普通合伙)') != -1 or reg_namecn.find('（普通合伙）') != -1:
            reg_namecn_type = '企业'
            return reg_namecn_type



        #获取产业名称后一位
        last_one = reg_namecn[:-1]
        if last_one in self.enterprise_one:
            reg_namecn_type = '企业'
            if last_one == '行' and reg_namecn == '中国人民银行':
                reg_namecn_type = '事业单位'
            return reg_namecn_type

        last_two = reg_namecn[:-2]
        if last_two in self.enterprise_two:
            reg_namecn_type = '企业'
            if last_two == '银行' and reg_namecn == '中国人民银行':
                reg_namecn_type = '事业单位'

            return reg_namecn_type

        last_three = reg_namecn[:-3]
        if last_three in self.enterprise_three:
            reg_namecn_type = '企业'
            return reg_namecn_type





    def personal(self,reg_namecn):
        pass




    #先判断产业的长度
    def leng_name(self,reg_namecn):
        if len(reg_namecn) >= 4:
            #先判定为企业
            self.no_personal(reg_namecn)
        else:
            self.personal(reg_namecn)