import threading
import random
import time

class Producer(threading.Thread):
    """
    向列表中生产随机整数
    """

    def __init__(self, integers, condition):
        """
        构造器

        @param integers 整数列表
        @param condition 条件同步对象
        """
        super(Producer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run方法。在随机时间向列表中添加一个随机整数
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()  # 获取条件锁
            self.integers.append(integer)
            print ('%d appended to list by %s' % (integer, self.name))
            self.condition.notify()  # 唤醒消费者线程
            self.condition.release()  # 释放条件锁
            time.sleep(1)  # 暂停1秒钟


class Consumer(threading.Thread):
    """
    从列表中消费整数
    """

    def __init__(self, integers, condition):
        """
        构造器

        @param integers 整数列表
        @param condition 条件同步对象
        """
        super(Consumer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run()方法，从列表中消费整数
        """
        while True:
            self.condition.acquire()  # 获取条件锁
            while True:
                if self.integers:  # 判断是否有整数
                    integer = self.integers.pop()
                    print ('%d popped from list by %s' % (integer, self.name))
                    break
                self.condition.wait()  # 等待商品，并且释放资源
            self.condition.release()  # 最后释放条件锁


if __name__ == '__main__':
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()