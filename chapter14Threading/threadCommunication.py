'''
练习：线程通信:
a、使用Condition实现线程通信
b、使用Queue控制线程通信
c、使用Event控制线程通信
******************************************
Condition类提供几个方法
acquire([timeout])/release()，调用Lock的acquire()和release()方法
wait([timeout]):导致当前线程进入Condition的等待池等待通知并释放锁，直到其他线程调用该Condition的notify()和notify_all()
	方法唤醒。在调用该方法的时候可以传入timeout参数，设置等待时间。
notify():唤醒Condition池内的单个线程，该线程自动调用acquire()方法尝试加锁；如果所有线程都在等待池中，则选择任意一个线程
	进行唤醒。
notify_all():唤醒在该Condition等待池中的所有线程并通知它们。
'''
import threading


class Account:

	def __init__(self, account_no, balance):
		'''构造器函数,初始化账户编号、余额；调用Condition类，并设定flag初始值'''
		#封装账户编号和账户余额两个成员变量
		self.account_no = account_no
		self._balance = balance
		#调用Condition类和定义是否已经存钱的标志flag
		self.cond = threading.Condition()
		self._flag = True
	
	def getBalance(self):
		'''账户余额获取函数。因为账户余额不能随便修改，所以职位self._balance设置getter方法'''
		return self._balance
	
	def draw(self, draw_amount):
		'''取钱操作函数，取钱之前设置加锁'''
		self.cond.acquire()
		try:
			if not self._flag:#如果self.flag为False，标明账户中还没有存钱进去，取钱方法被阻塞
				print("取款操作被阻塞")
				self.cond.wait()
			else:
				print(threading.current_thread().name+"取钱："+str(draw_amount))
				self._balance -=draw_amount
				print("账户余额为："+str(self._balance))
				#设置取款的标志位False
				self._flag = False
				#唤醒其他进程
				self.cond.notify_all()
		finally:
			self.cond.release()
	
	def deposit(self, deposit_amount):
		'''存钱函数，存钱之前设置加锁'''
		#加锁
		self.cond.acquire()
		try:
			if self._flag:
				print("存款操作被阻塞")
				self.cond.acquire()
			else:
				print(threading.current_thread().name+"存钱："+str(deposit_amount))
				self._balance+=deposit_amount
				print("账户余额为："+str(self._balance))
				#设置存款的标志位True
				self._flag = True
				#唤醒其他进程
				self.cond.notify_all()
		finally:
			self.cond.release()

def draw_many(account,draw_amount,max):
	#模拟用户多次花钱；account为Account的实例对象
	for i in range(max):
		account.draw(draw_amount)

def deposit_many(account,deposite_amount,max):
	#模拟多次存钱；account为Account的实例对象
	for i in range(max):
		account.deposit(deposite_amount)

#创建一个账户
acc = Account("我的账户",800)
#创建一个取钱线程
threading.Thread(name="取钱者", target=draw_many, args=(acc,800,3)).start()
#创建一个存钱线程
threading.Thread(name="存钱甲", target=deposit_many, args=(acc,800,3)).start()
