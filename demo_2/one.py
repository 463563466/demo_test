import re
import pandas as pd
import requests
from tools.shujuku_conn.mysql_conn import MysqlConnect

db = MysqlConnect('127.0.0.1', 'root', '123456', 'address_shangbiao')


def api_select(address):
    try:
        get_api = requests.get('https://restapi.amap.com/v3/geocode/geo?address={}&output=JSON&key=8398d5d32f176383c70b20ea2d3152dc'.format(address))
        concent_api = get_api.json()
        if concent_api["status"] == '1':
            province_api = concent_api["geocodes"][0]["province"]
            city_api = concent_api["geocodes"][0]["city"]
            district_api = concent_api["geocodes"][0]["district"]
            if province_api in ('北京市','天津市','上海市'):
                city_api = '市辖区'
            if province_api == '重庆市':
                if '县' in district_api:
                    city_api ='县'
                elif '区' in district_api:
                    city_api = '市辖区'
            if city_api in ('东莞市','中山市','儋州市','三沙市','嘉峪关市'):
                district_api = city_api
            if province_api == '台湾省':
                city_api = '台湾省'
                district_api = '台湾省'
            if province_api in ('香港特别行政区','澳门特别行政区'):
                city_api = province_api
                district_api = province_api
            if district_api in ('石河子市', '阿拉尔市', '图木舒克市', '五家渠市', '北屯市', '铁门关市', '双河市', '可克达拉市', '昆玉市','胡杨河市'):
                city_api = '自治区直辖县级行政区划'
            if district_api in ('济源市', '仙桃市', '潜江市', '天门市', '神农架林区', '五指山市', '琼海市', '文昌市', '万宁市', '东方市', '定安县', '屯昌县', '澄迈县', '临高县', '白沙黎族自治县', '昌江黎族自治县', '乐东黎族自治县', '陵水黎族自治县', '保亭黎族苗族自治县', '琼中黎族苗族自治县'):
                city_api = '省直辖县级行政区划'
            data_api = {}
            data_api["province_api"] = province_api
            data_api["city_api"] = city_api
            data_api["district_api"] = district_api
            return data_api
        else:
            print('搜不到。。。')
    except Exception as e:
        print('搜不到。。。')


def get_df(file):
    mylist = []
    for chunk in pd.read_csv(file, chunksize=50000, iterator=True):
        mylist.append(chunk)
    temp_df = pd.concat(mylist, axis=0)
    del mylist
    return temp_df
file = 'temp_shangbiao_address_two_1.csv'
content =get_df(file)
num = 0
for indexs in content.columns:
    con = content[indexs]
    con_ = con.values
    for address_source in con_:
        address = address_source.replace('\t', '')
        try:
            address_re = re.findall('(.*?)省(.*?)市(.*?)县|(.*?)省(.*?)市(.*?)区',address)
            if len(address_re) > 0:
                if len(address_re[0]) > 0:
                    if len(address_re[0][0]) > 0:
                        province_re = address_re[0][0]
                        city_re = address_re[0][1]
                        district_re = address_re[0][2]
                        province = province_re + '省'
                        city = city_re + '市'
                        district = district_re + '县'
                    elif len(address_re[0][3]) > 0:
                        province_re = address_re[0][3]
                        city_re = address_re[0][4]
                        district_re = address_re[0][5].replace('"','')
                        province = province_re + '省'
                        city = city_re + '市'
                        district = district_re + '区'
                    sql = 'select count(*) from p_c_d where province="{}" and city="{}" and district="{}";'.format(province,city,district)
                    back_data = db.select(sql)[0][0]
                    if back_data == 0:
                        #通过api查询
                        data_api = api_select(address)
                        province_api = data_api["province_api"]
                        city_api = data_api["city_api"]
                        district_api = data_api["district_api"]
                        sql = 'select count(*) from p_c_d where province="{}" and city="{}" and district="{}";'.format(province_api,city_api,district_api)
                        back_api_data = db.select(sql)[0][0]
                        if back_api_data == 0:
                            with open('E:/address/no_find_all.txt','a',encoding='utf-8') as e:
                                e.write(address)
                                e.write('\n')
                                print('查不到，已跳过...')
                        else:
                            data = []
                            data.append(address)
                            data.append(province_api)
                            data.append(city_api)
                            data.append(district_api)
                            with open('E:/address/shangbiao_one.txt','a',encoding='utf-8') as e:
                                for i in data:
                                    e.write(i)
                                    e.write('\t')
                            with open('E:/address/shangbiao_one.txt','a',encoding='utf-8') as e:
                                e.write('\n')
                                num+=1
                                print('插入第',num,'条...')
                    else:
                        data = []
                        data.append(address)
                        data.append(province)
                        data.append(city)
                        data.append(district)
                        with open('E:/address/shangbiao_one.txt', 'a', encoding='utf-8') as e:
                            for i in data:
                                e.write(i)
                                e.write('\t')
                        with open('E:/address/shangbiao_one.txt', 'a', encoding='utf-8') as e:
                            e.write('\n')
                            num += 1
                            print('插入第', num, '条...')
            else:
                data_api = api_select(address)
                province_api = data_api["province_api"]
                city_api = data_api["city_api"]
                district_api = data_api["district_api"]
                sql = 'select count(*) from p_c_d where province="{}" and city="{}" and district="{}";'.format(province_api,city_api,district_api)
                back_api_data = db.select(sql)[0][0]
                if back_api_data == 0:
                    with open('E:/address/no_find_all.txt', 'a', encoding='utf-8') as e:
                        e.write(address)
                        e.write('\n')
                else:
                    data = []
                    data.append(address)
                    data.append(province_api)
                    data.append(city_api)
                    data.append(district_api)
                    with open('E:/address/shangbiao_one.txt', 'a', encoding='utf-8') as e:
                        for i in data:
                            e.write(i)
                            e.write('\t')
                    with open('E:/address/shangbiao_one.txt', 'a', encoding='utf-8') as e:
                        e.write('\n')
                        num += 1
                        print('插入第', num, '条...')
        except Exception as e:
            with open('E:/address/no_find_all.txt', 'a', encoding='utf-8') as e:
                e.write(address)
                e.write('\n')
                print('查不到，已跳过...')