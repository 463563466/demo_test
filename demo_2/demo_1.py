import requests
from tools.shujuku_conn.mysql_conn import MysqlConnect

db = MysqlConnect('127.0.0.1', 'root', '', 'wenshu')

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


def sele():
    sql = 'select * from address_0730;'
    data_address = db.select(sql)
    num = 0

    for i in data_address:
        try:
            address = i[0]
            gaode = api_select(address)
            province_api = gaode["province_api"]
            city_api = gaode["city_api"]
            district_api = gaode["district_api"]
            sql = 'insert into address_pcd values ("{}","{}","{}","{}")'.format(address,province_api,city_api,district_api)
            db.exec(sql)
            num+=1
            print('添加',num)
        except Exception as e:
            print('搜不到。。。')

sele()