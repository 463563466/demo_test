


class Address_filter(object):
    
    def filter(self,province,city,district):
        if province in ('北京市', '天津市', '上海市'):
                city = '市辖区'
        if province == '重庆市':
            if '县' in district:
                city = '县'
            elif '区' in district:
                city = '市辖区'
        if city in ('东莞市', '中山市', '儋州市', '三沙市', '嘉峪关市'):
            district = city
        if province == '台湾省':
            city = '台湾省'
            district = '台湾省'
        if province in ('香港特别行政区', '澳门特别行政区'):
            city = province
            district = province
        if district in ('石河子市', '阿拉尔市', '图木舒克市', '五家渠市', '北屯市', '铁门关市', '双河市', '可克达拉市', '昆玉市', '胡杨河市'):
            city = '自治区直辖县级行政区划'
        if district in (
        '济源市', '仙桃市', '潜江市', '天门市', '神农架林区', '五指山市', '琼海市', '文昌市', '万宁市', '东方市', '定安县', '屯昌县', '澄迈县', '临高县', '白沙黎族自治县',
        '昌江黎族自治县', '乐东黎族自治县', '陵水黎族自治县', '保亭黎族苗族自治县', '琼中黎族苗族自治县'):
            city = '省直辖县级行政区划'
        data = {}
        data["province"] = province
        data["city"] = city
        data["district"] = district
        return  data