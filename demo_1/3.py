from lxml import etree
from tools.shujuku_conn.mysql_conn import MysqlConnect
import os
import time
import zipfile


db = MysqlConnect('127.0.0.1', 'root', '123456', 'file_com')


num = 0
def get_conent(filename,file_path,file_name):
    tree = etree.parse(filename)  # 打开xml文档
    # root = ET.fromstring(country_string) #从字符串传递xml
    root = tree.getroot()# 获得root节点
    business = root.nsmap['business']
    base = root.nsmap['base']
    xsi = root.nsmap['xsi']
    PRSRecord = root.xpath(".//business:PRSRecord", namespaces={"business":business})
    for nodes in PRSRecord:
        global num
        num+=1
        standard_number = ''
        standard_date = ''
        original_date = ''
        original_number = ''
        prsid = nodes.attrib['PRSID']
        status = nodes.attrib['status']
        children = nodes.getchildren()
        standard_appltype = children[0].attrib['applType']
        dataformat = children[0].attrib['dataFormat']
        if dataformat == 'standard':
            standard_appltype = children[0].attrib['applType']
            dataformat_standard = children[0].attrib['dataFormat']
            standard_sequence = children[0].attrib['sequence']
            for children_C in children[0].getchildren():
                    for children_Cc in  children_C.getchildren():
                        if 'DocNumber' in children_Cc.tag:
                            standard_number = children_Cc.text
                        elif 'Date' in children_Cc.tag:
                            standard_date = children_Cc.text
                        else:
                            standard_number = ''
                            standard_date = ''
            original_appltype = children[1].attrib['applType']
            dataformat_original = children[1].attrib['dataFormat']
            original_sequence = children[1].attrib['sequence']
            original_sourceDB = children[1].attrib['sourceDB']
            for children_Cc in children[1].getchildren():
                for children_C_c in children_Cc.getchildren():
                    if 'DocNumber' in children_C_c.tag:
                        original_number = children_C_c.text
                    elif 'Date' in children_C_c.tag:
                        original_date = children_C_c.text
                    else:
                        original_number = ''
                        original_date = ''
        elif dataformat == 'original':
            original_appltype = children[0].attrib['applType']
            dataformat_original = children[0].attrib['dataFormat']
            original_sequence = children[0].attrib['sequence']
            original_sourceDB = children[0].attrib['sourceDB']
            for children_C in children[0].getchildren():
                for children_Cc in children_C.getchildren():
                    if 'DocNumber' in children_Cc.tag:
                        original_number = children_Cc.text
                    elif 'Date' in children_Cc.tag:
                        original_date = children_Cc.text
                    else:
                        original_number = ''
                        original_date = ''
            standard_appltype = children[1].attrib['applType']
            dataformat_standard = children[1].attrib['dataFormat']
            standard_sequence = children[1].attrib['sequence']
            for children_Cc in children[1].getchildren():
                for children_C_c in children_Cc.getchildren():
                    if 'DocNumber' in children_C_c.tag:
                        standard_number = children_C_c.text
                    elif 'Date' in children_C_c.tag:
                        standard_date = children_C_c.text
                    else:
                        standard_number = ''
                        standard_date = ''
        iprtype = children[2].text
        PRSPublicationDate_ = children[3].getchildren()
        prspublicationdate = PRSPublicationDate_[0].text
        prscode = children[4].text
        prsvalue = children[5].text
        prsinformation = children[6].text
        statusindicator = children[7].text


        #写入mysql
        sql = "insert into xml_analysis_legals" \
              " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%\
              (file_path,file_name,prsid,status,dataformat_standard,standard_appltype,standard_sequence,standard_number,
               standard_date,dataformat_original,original_appltype,original_sequence,original_number,original_date,original_sourceDB,
               iprtype,prspublicationdate,prscode,prsvalue,prsinformation,statusindicator)
        try:
            db.exec(sql)
            print('写入', num, '条....')
        except Exception as e:
            print('第',num,'条出错')
            data_all = []
            data_all.append(file_path)
            data_all.append(file_name)
            data_all.append(prsid)
            data_all.append(status)
            data_all.append(dataformat_standard)
            data_all.append(standard_appltype)
            data_all.append(standard_sequence)
            data_all.append(standard_number)
            data_all.append(standard_date)
            data_all.append(dataformat_original)
            data_all.append(original_appltype)
            data_all.append(original_sequence)
            data_all.append(original_number)
            data_all.append(original_date)
            data_all.append(original_sourceDB)
            data_all.append(iprtype)
            data_all.append(prspublicationdate)
            data_all.append(prscode)
            data_all.append(prsvalue)
            data_all.append(prsinformation)
            data_all.append(statusindicator)
            with open('xml_log.txt','a',encoding='utf-8') as f:
                for i in data_all:
                    f.write(i)
                    f.write('\t')
            with open('xml_log.txt', 'a', encoding='utf-8') as f:
                f.write('\n')


        #写入excel
        # print('写入',num,'条....')
        # wb = load_workbook('E:\\Analysis_legals_first_0630.xlsx')
        # ws = wb["Sheet1"]
        # for i in range(len(data_all)):
        #     ws.cell(row=num+1, column=i+1, value=data_all[i])
        # wb.save('E:\\Analysis_legals_first_0630.xlsx')


def get_File(folder_name):
    os.chdir(folder_name)
    # file_names = os.listdir("./")
    # path_zero = os.getcwd()
    # for name in file_names:
    #     openpath = path_zero + '\\' + name
    #     os.chdir(openpath)
    #     print('进入文件夹',name)
    file_names = os.listdir("./")
    path_one = os.getcwd()
    for name in file_names:
        if name == 'over':
            continue
        openpath = path_one + '\\' + name
        os.chdir(openpath)
        print('进入文件夹', name)
        file_names = os.listdir("./")
        for name in file_names:
            print('寻找zip文件...')
            if os.path.isfile(name) :
                houzhui = name[-4:]
                 # = os.path.dirname(os.getcwd()) + '\\Screenshots\\'
                if houzhui == '.ZIP':
                    print('找到zip文件开始解压...')
                    path = os.getcwd()
                    file_path = path + '\\' + name
                    zfile = zipfile.ZipFile(file_path, "r")
                    namelist = zfile.namelist()
                    zfile.extractall()
                    # 不设置延时会导致还没有解压完，就开始去找文件，导致找到文件错误
                    time.sleep(1)
                    for name in namelist:
                        if len(name) < 70:
                            continue
                        path_all = path + '\\' + name.replace('/','\\')
                        openfile_path = path_all
                        file_path = path_all[11:].replace('\\','/')
                        file_name = name.split('/')[2]
                        print('开始打开文件',file_name,'并解析...')
                        get_conent(openfile_path,file_path,file_name)

if __name__ == '__main__':
    path = 'E:/CN-PRSS/CN-PRSS-10_中国发明专利法律状态标准化数据'
    get_File(path)











