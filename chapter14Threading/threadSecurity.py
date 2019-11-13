'''
练习：线程锁
threading 模块提供了Lock和RLock两个类
1、threading.Lock:它是基本的锁对象，每次只能锁定一次，其余的锁请求，需要等待锁释放后才能获取。
2、threading.RLock:它代表可重入锁，同一个线程中可以多次锁定，也可以多次释放。该锁的acquire()和Release()方法必须成对出现
3、Lock和RLock都提供了两个方法实现加锁和释放锁
   a、acquire(blocking=True，timeout=-1)，请求加锁，其中timeout制定加锁多少秒
   b、release()：释放锁
'''
import threading
import time

class Account:
	def __init__(self,account_no,balance):
		#定义account构造函数
		#封装账户编号和账户余额两个成员变量
		self.account_no = account_no
		self._balance = balance
		self.lock = threading.RLock()
	
	def getBalance(self):
		#由于账户余额不允许随便修改，所以只为self._balance提供getter方法
		return self.balance
	
	def draw(self,draw_amount):
		#提供一个线程安全的draw()方法来完成取钱操作
		#加锁
		self.lock.acquire()
		try:
			if self._balance >= draw_amount:
				print(threading.current_thread().name+"取钱成功！吐出钞票："+str(draw_amount))
				time.sleep(0.001)
				#修改余额
				self._balance -=draw_amount
				print("\t余额为："+str(self._balance))
			else:
				print(threading.current_thread().name+"取钱失败，余额不足！")
		finally:
			self.lock.release()
		
def draw_money(account,draw_amount):
	#传递进来的account对象和需要取的钱数-draw_amount
	account.draw(draw_amount)

acct = Account("134567",1000)
#使用两个线程模拟取钱
threading.Thread(name='甲', target=draw_money, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw_money, args=(acct, 800)).start()

'''执行结果如下
甲取钱成功！吐出钞票：800
        余额为：200
乙余额不足，取钱失败！
'''

