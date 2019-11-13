'''
练习：线程通信三:
a、使用Condition实现线程通信
b、使用Queue控制线程通信
c、使用Event控制线程通信(实例)
************Event方法******************************
is_set():该方法返回Event内部旗标是否为True
set():该方法设置Event内部旗标为True
clear():该方法设置Event内部旗标为False,通常接下来会调用wait()方法来阻塞当前线程
wait():阻塞该进程
'''
import threading
import time

#此处event变量是个全局变量
event = threading.Event()
#定义方法
def cal():
    '''enent调用方法'''
    #启动线程
    print("%s 启动,进入计算状态"%threading.current_thread().getName())
    #阻塞进程
    event.wait()
    #收到事件后，正式计算
    print("%s收到通知了，正式计算"%threading.current_thread().getName())

#创建并启动两个线程
threading.Thread(name="甲",target=cal,args=()).start()
threading.Thread(name="乙",target=cal,args=()).start()
time.sleep(2)
print("*"*20)
#发出事件
print("主线程发出事件")
event.set()
