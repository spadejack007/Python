'''解析字符串'''
from urllib.parse import * 

result = urlparse("https://www.baidu.com/s?wd=CSDN&rsv_spt=1&")
print('scheme-属性获取',result.scheme,'\nscheme-数组下标获取',result[0])
print('主机和端口-属性获取',result.netloc,'\nscheme-数组下标获取',result[1])
print('主机',result.hostname)
print('端口',result.port)
