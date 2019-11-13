'''
练习：线程通信二:
a、使用Condition实现线程通信
b、使用Queue控制线程通信(实例)
c、使用Event控制线程通信
******************************************
queue提供三种形式：标准队列(先进先出)、栈队列（先进后出）、优先级队列
queue.Queue(maxsize = 0)、queue.LifoQueue(maxsize=0)、PriorityQueue(maxsize=0)
这三种队列都提供了如下的方法：
Queue.qsize():返回队列的实际大小，就是该队列中包含几个元素
Queue.empty():
Queue.full():
Queue.put(item,block=True,timeout=None):如果队列已满，并且block=True；
    当前线程被阻塞；如果队列已满，并且block=False，则直接引发queue.Full异常
    timeout设置为None则代表一直阻塞
Queue.put(item)：向队列中放入一个元素，不阻塞；相当于上一个函数设置block=False
Queue.get(item,block=True,timeout=None):如果队列已空，并且block=True；
    当前线程被阻塞；如果队列已空，并且block=False，则直接引发queue.EMPTY异常
    timeout设置为None则代表一直阻塞
Queue.get()：向队列中放入一个元素，不阻塞；相当于上一个函数设置block=False
'''
import threading
import queue
import time

def product(bq):
    '''队列的put方法，放置元素到队列中'''
    str_tuple = ("Python","Java","Javascript","Avisynth","Bat")
    for i in range(10):
        time.sleep(0.2)
        #尝试放入队列，如果队列满则线程被阻塞
        bq.put(str_tuple[i%5])
        print(threading.current_thread().name + "生产者生产元素完成")
        print("**"*20)

def consum(bq):
    '''队列的get方法，队列中元素出来'''
    while True:
        #尝试取出元素，如果队列为空，则线程阻塞
        t = bq.get()
        print(threading.current_thread().name+"消费【%s】元素"%t)
        print("- "*20)

#创建一个容量为1的queue
bq = queue.Queue(1)
#启动三个生产者进程
threading.Thread(name="玫瑰产线", target=product, args=(bq,)).start()
threading.Thread(name="牡丹产线", target=product, args=(bq,)).start()
threading.Thread(name="荷花产线", target=product, args=(bq,)).start()
#启动一个消费者进程
threading.Thread(name="学习者", target=consum, args=(bq,)).start()
