'''
练习：用于观察线程运行的效果
python主要通过两种方式创建线程
1、使用threading模块的Thread类构造器创建线程
2、集成threading模块的Thread类创建线程类
----------Thread类的构造器------------------------------
__init__(self,group=None, target=None, name=None, args=(), kwargs=None,*,daemon=None)
group:指定该线程所属的线程组，目前还未实现，只能设置值为None
target:指定线程要调度的目标方法
args:指定一个元组。元组的第一个元素传递给target函数的第一个参数，元组的第二个元素传递个target函数的第二个参数...,以此类推
kwargs:指定一个字典，以关键字擦书的形式为target指定的函数传入参数
daemon:指定所构建的线程是否为后台进程
----------Thread类的注意事项----------------------------
1、启动线程使用start()方法，而不是run()方法。
2、设置线程为后台线程后，前台进程结束后，后台线程也会被强制退出。
'''
import threading

def action(max):
	'''方法一：定义一个普通的action方法，该方法准备作为线程主体执行'''
	for i in range(max):
		#调用threading模块的current_thread()方法获取当前线程
		#调用线程的getName()方法，获取当前线程名称
		print(threading.current_thread().getName() + " " + str(i))

class FKThread(threading.Thread):
	'''方法二：继承Thead类的方法'''
	def __init__(self):
		'''继承Thead类的方法'''
		threading.Thread.__init__(self)
		self.i = 0
	def run(self):
		'''重写run方法'''
		while self.i<100:
			print(threading.current_thread().getName() + " " + str(i))
			self.i+=1
#下面是主线程
for i in range(100):
	print(threading.current_thread().getName() + " " + str(i))
	if i == 20:
		'''方法一调用
		#创建并启动第一个线程
		t1 = threading.Thread(target=action,args=(100,))
		t1.start()
		#创建并启动第二个线程
		t2 = threading.Thread(target=action,args=(100,))
		t2.start()'''
		'''方法二调用'''
		#创建并启动第一个线程
		ft1 = FKThread()
		ft1.start()
		#创建并启动第二个线程
		ft2 = FKThread()
		ft2.start()
		
print("主线程执行完毕")