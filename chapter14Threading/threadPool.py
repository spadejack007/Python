'''
进程池操作
**************************
线程池的基类是concurrent.futures 模块中的Executor,Executor提供了两个子类
ThreadPoolExecutor 和 ProcessPoolExecutor，其中ThreadPoolExecutor用于创建线程池
ProcessPoolExecutor用于进程池
-----------------------
Executor提供常用方法：
1、submit(fn,*args,**kwargs):将fn函数提交给线程池。*args代表传给fn函数的参数，*kwargs
代表以关键字参数的形式为fn函数传入参数
2、map(func,*iterables,timeout=None,chunksize=1):该函数类似于全局函数map(func,*iterables),
只是该函数将会启动多个线程，以异步方式立即对iterables执行map处理
3、shutdown(wait=True):关闭线程池
-----------------------
提交submit给线程池后，submit方法会返回一个Future对象，Future类主要用于获取线程任务函数的返回值。
Future提供了如下方法：
cancel():取消该Future代表的线程任务。如果该任务正在执行，不可取消，则返回False；否则会取消该任务，返回True。
cancelled():返回Future线程是否被取消
running():如果该Future代表的线程任务正在执行、不可被取消，该方法返回True
done():如果该Future代表的线程任务被成功取消或执行完成，则该方法返回True
result(timeout=None):获取该Future代表的线程任务最后返回的结果。
exception(timeout=None):
add_done_callback(fn):

'''
from concurrent.futures import ThreadPoolExecutor
import threading
import time

'''
定义一个准备作为线程任务的函数
'''
def action(max):
	my_sum = 0
	for i in range(max):
		print(threading.current_thread().name + " " +str(i))
		my_sum +=i
	return my_sum

'''
创建一个包含两个线程的线程池
'''
with ThreadPoolExecutor(max_workers=2) as pool:
	#向线程池中提交一个任务，50会作为action()函数的参数
	future1 = pool.submit(action,50)
	#向线程池中再提交一个任务，100会作为action()函数的参数
	future2 = pool.submit(action,100)
	#回调函数
	def get_result(future):
		print(future.result())
	#添加回调函数
	future1.add_done_callback(get_result)
	future2.add_done_callback(get_result)
	
	print("-"*20)

