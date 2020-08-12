import threading
import queue
import random
import time
from tools.shujuku_conn.mysql_conn import MysqlConnect
from tools.address_api.gaodeaddress_api import Gaode_address
db = MysqlConnect('127.0.0.1', 'root', '', 'wenshu')
gd = Gaode_address()

class Producer(threading.Thread):

    def __init__(self, queue):
        super(Producer,self).__init__()
        self.queue = queue

    def run(self):
        sql = 'select * from address_0730'
        data_address = db.select(sql)
        for i in data_address:
            dict = gd.get_api(i[0])
            dict["address"] = i[0]
            self.queue.put(dict)
            print('%s 添加到队列 %s' % (i, self.name))



class Consumer(threading.Thread):

    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            integer = self.queue.get()
            address = integer["address"]
            province = integer["province_api"]
            city = integer["city_api"]
            district = integer["district_api"]
            sql = 'insert into address_pcd values ("{}","{}","{}","{}")'.format(address, province, city,district)
            db.exec(sql)
            print('%s 已插入数据库，执行者- %s' % (integer, self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()