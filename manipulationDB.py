#数据库连接变量的事务提交和executemany()方法
#1、python如果只带一个元素的元组，元素后面要加一个","  逗号。 
#2、DML语句(Data Manipulation Language)：用于增删改表中数据，DML是伴随TCL事务控制的。
#3、DDL语句(Data Definition Language)：数据定义语言，用来维护数据库对象 

import sqlite3

#1、打开数据库
conn = sqlite3.connect("test_Raspberry.db")

#2、打开游标
c = conn.cursor()

#3、执行SQL语句
c.execute('''insert into user (user,pass,age) values ("jack","1899",15);''')
print("影响的行数:",c.rowcount)

c.executemany('insert into user values (null,?,?,?)',(
("孙悟空",'12345',25),
("猪八戒",'123457',26),
("沙和尚",'1234567',27)
))
print("影响的行数:",c.rowcount)
#4、提交事务
conn.commit()#注意，是conn的事务处理提交，不是cursor的
#4、关闭游标
c.close()
#5、关闭连接
conn.close()