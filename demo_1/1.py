#获取.docx文件
import os,re
import sys
import os.path
import docx

#文件路径
def list_file(path_file):
    count = 0
    path_data = []
    for filename in os.listdir(path_file):
        if os.path.splitext(filename)[1] == '.docx':
            count = count+1
            f_name = filename
            f_path = path_file + '\\' + filename
            path_data.append(f_path)
    print('total docx file: ',count)
    return path_data

#输出数据
def input_excel(path_all):
    file = docx.Document(path_all)
    text_1 = ''
    for para in file.paragraphs:
        text = para.text
        text.replace('\n', '').replace('\r', '').replace('\t', '')
        text_1 = text_1 + text
    text_date = re.findall('附件(.*?)（.*发证日期：(.*?)）',text_1)
    if text_date:
        print(text_date[0][0])
        print(text_date[0][1])
        data = {}
        data['名称'] = text_date[0][0]
        data['日期'] = text_date[0][1]
        return data
    else:
        data = {}
        data['名称'] = '不存在'
        data['日期'] = '不存在'
        return data


list = os.listdir(r'C:\Users\Administrator\Desktop\chage')
for i in list:
    path = r'C:\Users\Administrator\Desktop\chage' + '\\' + i
    path_alls =list_file(path)
    context = []
    for path_all in path_alls:
        data = input_excel(path_all)
        name_company = data['名称']
        date_out = data['日期']
        context.append(name_company)
        context.append(date_out)
    with open('统计_总.txt','a+',encoding='utf8') as e:
        text =  "   ".join(str(i) for i in context)
        e.write(text+'\n')




def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)


def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])







