#!/usr/bin/python
# encoding: utf-8

import sys
import os.path
from shutil import copytree,ignore_patterns
import logging
import time
import traceback

'''
功能：通过task.txt文档中的文件夹名字，拷贝对应目录文件--》指定盘符下面
1、copyTree
2、os.path.exist()
3、strip去掉readlines的换行符
--------v0.1.0----------
1、完成了拷贝程序的主体函数
--------v0.2.0----------
1、增加函数入口__main__
2、增加log日志输出
3、增加task.txt不存在时检查
------------------------
学习体会：拷贝当前目录下的文件夹所有内容
#1、lexists和exists的区别还需要继续学习
#2、Readline后面会带着换行符，直接赋值给exist()函数总会返回false，需要strip掉'\n'换行符
'''
def path_parse(filePath):	
	return str(filePath.rstrip(os.sep))

def copy_folder (newDictory):
	try:
		
		currentDir = os.path.abspath(os.curdir)
		count = 0
		
		#此处还需要加一个任务文件task.txt是否存在的判断，不存在则提示
		#
		with open(file = "task.txt",mode = 'r',encoding = "utf-8") as fp:
			ls = fp.readlines()
		for item in ls:
			count = count + 1
			fsrc = os.path.join(currentDir,item.strip('\n'))
			fdst = os.path.join(newDictory,item.strip('\n'))#此处不用单独添加os.step,函数自动添加了os.step
			#打印拷贝的信息，后续会打印到logging中
			logging.info("%s【%d】==>%s" % (time.strftime("%Y%m%d-%H:%M:%S"),count,fdst))
			#目录路径判断及目录(copyTree)拷贝
			if os.path.exists(fsrc):
				if not os.path.exists(fdst):
					copytree(fsrc ,fdst,ignore=ignore_patterns('*.wav', '*.jpg'))
					print("%s【SUCCESS】拷贝完成==>%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fdst))
					logging.info("%s【SUCCESS】拷贝完成==>%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fdst))
				else:
					print("%s【ERROR】目标目录已存在==>%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fdst))
					logging.info("%s【ERROR】目标目录已存在==>%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fdst))
			else:
				print("%s【ERROR】源目录不存在--%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fsrc))
				logging.info("%s【ERROR】源目录不存在--%s" % (time.strftime("%Y%m%d-%H:%M:%S"),fsrc))
			#对源目录和目的目录字符串清空，用于下次迭代	
			fsrc = ""
			fdst = ""

	except FileNotFoundError as err:
		err_message = 'task.txt不存在，请检查文件'
		print(err_message)
		logging.info("%s【ERROR】%s" % (time.strftime("%Y%m%d-%H:%M:%S"),err_message))
	else:
		print('traceback.format_exc():\n%s' % traceback.format_exc())
		logging.info("%s【ERROR】%s" % (time.strftime("%Y%m%d-%H:%M:%S"),traceback.format_exc()))
##############################################################################
if __name__ == "__main__":	
	#logging输出设置
	time_stamp = time.strftime("%Y%m%d_%H%M%S")
	logging.basicConfig(filename=time_stamp+'.log', level=logging.INFO)
	print("拷贝任务完成后，请查看程序exe所在目录下的xxx.log文件")
	#判断参数是否为2个eg：python XXX.py e:\temp;若不存在提示，请输入目的地址
	if len(sys.argv) == 2:
		newDictory = path_parse(sys.argv[1])
		copy_folder(newDictory)	
	else:
		print("请输入目的目录")
		logging.info("%s【ERROR】请您输入目的目录eg: e:\temp" % (time.strftime("%Y%m%d-%H:%M:%S")))
	
		
		