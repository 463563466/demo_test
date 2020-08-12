from tools.shujuku_conn.oracle_conn import OracleOperation
import requests,json

def baidu_api(address):
    try:
        get_data = requests.get('http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak=p7Qt9MzgWrsjlziNhtnKeSd4ThUn9w1p'.format(address))
        con = get_data.content
        json_con = json.loads(con)
        area_xy_dict = json_con['result']
        if len(area_xy_dict) > 0:
            lng = str(area_xy_dict['location']['lng'])
            lat = str(area_xy_dict['location']['lat'])
            area_xy = lng + ',' + lat
            return area_xy
    except Exception as e:
        with open('area1_xy_log.txt', 'a', encoding='utf-8') as aa:
            aa.write(comp_id)
            aa.write('\n')
            global num
            num += 1

if __name__ == '__main__':
    db = OracleOperation()
    DATA = db.execute_sql('SELECT comp_id,address FROM wuhan_rest')
    data = db.get_data()
    num = 0
    for concent in data:
        comp_id = concent[0]
        if concent[1][:3] == '武汉市':
            address = concent[1][:28].replace('#','')
        else:
            address = '武汉市'+concent[1][:28].replace('#', '')
        try:
            area_xy = baidu_api(address)
            sql = "update WUHANMINGLU_NEW set area_xy_baidu='{}' where comp_id='{}'".format(area_xy,comp_id)
            # sql = "insert into wuhan_addr_new values ('{}','{}')".format(comp_id,area_xy)
            # sql = "update wuhan_rest set area_xy_baidu='{}' where comp_id='{}'".format(area_xy,comp_id)
            DATA = db.execute_sql(sql)
            num+=1
            print('已完成定位',num,'条')
        except Exception as e:
            with open('area1_xy_log.txt','a',encoding='utf-8') as aa:
                aa.write(comp_id)
                aa.write('\n')
                num += 1