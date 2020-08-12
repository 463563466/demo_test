import threading,time
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('生产者',self.name,' Append'+str(val),L)
            if lock_con.acquire():#条件锁
                L.append(val)
                lock_con.notify()#唤醒消费者线程
                lock_con.release()#释放条件锁
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()#获取条件锁
            if len(L)==0:
                lock_con.wait()#等待商品，并且释放资源
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('消费者',self.name,'Delete'+str(L[0]),L)
            del L[0]
            lock_con.release()#最后释放条件锁
            time.sleep(0.5)
if __name__=='__main__':
    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    print(threads)
    for t in threads:
        t.start()
    for t in threads:
        t.join()