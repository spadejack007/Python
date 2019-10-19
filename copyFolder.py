#拷贝当前目录下的文件夹所有内容
#1、lexists和exists的区别还需要继续学习
#2、Readline后面会带着换行符，直接赋值给exist()函数总会返回false，需要strip掉'\n'换行符
import os.path
from shutil import copytree,ignore_patterns

'''
功能：通过task.txt文档中的文件夹名字，拷贝对应目录文件--》指定盘符下面
1、copyTree
2、os.path.exist()
3、strip去掉readlines的换行符
--------v1.0.0----------
'''

try:
	
	#print(os.environ)
	winDriver = "G:"
	newDictory = "西瓜视频"
	currentDir = os.path.abspath(os.curdir)
	count = 0
	
	with open(file = "task.txt",mode = 'r',encoding = "utf-8") as fp:
		ls = fp.readlines()
	for item in ls:
		count = count + 1
		fsrc = os.path.join(currentDir,item.strip('\n'))
		fdst = os.path.join(winDriver,os.sep,newDictory,item.strip('\n'))
		print("%s	" % str(count),end = '')
		print(fsrc,end = '')
		print(os.path.exists(fsrc))

		if os.path.exists(fsrc):
			if not os.path.exists(fdst):
				copytree(fsrc ,fdst,ignore=ignore_patterns('*.wav', '*.jpg'))
				print("拷贝完成",fdst)
			else:
				print("已存在",fdst)
		else:
			print("不存在",fsrc)		
		fsrc = ""
		fdst = ""

except IOError as e:
	pass
	
finally:
	pass
 
