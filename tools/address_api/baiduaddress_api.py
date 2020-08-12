import requests

class Baidu_address(object):

    def __init__(self):
        self.url_latlng = 'http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak=p7Qt9MzgWrsjlziNhtnKeSd4ThUn9w1p'
        self.url_address = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=p7Qt9MzgWrsjlziNhtnKeSd4ThUn9w1p&output=json&coordtype=bd09ll&location={},{}'

    def get_api(self,address):
        get_api = requests.get(self.url_latlng.format(address))
        concent_api = get_api.json()
        if concent_api["status"] == 0:
            print('服务请求正常召回')
            lng = concent_api["result"]["location"]["lng"]
            lat = concent_api["result"]["location"]["lat"]
            result = self.get_api_address(lng,lat)
            return  result

    def get_api_address(self,lat,lng):
        get_api = requests.get(self.url_address.format(lng,lat))
        concent_api = get_api.json()
        data_api = {}
        if concent_api["status"] == 0 and concent_api["result"]["addressComponent"]["country_code"] == 0 and concent_api["result"]["addressComponent"]["country"] == '中国':
            print('服务请求正常召回')
            province_api = concent_api["result"]["addressComponent"]["province"]
            city_api = concent_api["result"]["addressComponent"]["city"]
            district_api = concent_api["result"]["addressComponent"]["district"]
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
            data_api["province_api"] = province_api
            data_api["city_api"] = city_api
            data_api["district_api"] = district_api
            return data_api
        else:
            data_api["province_api"] = ''
            data_api["city_api"] = ''
            data_api["district_api"] = ''
            return data_api

