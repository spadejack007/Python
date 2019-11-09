'''
1、调用connect()方法打开数据库连接，该方法返回数据库连接对象
2、通过数据库连接对象打开游标
3、使用游标执行SQL语句(包含DDL、DML、select查询语句等)
4、关闭游标
5、关闭数据库连接
'''
import sqlite3

#1、打开或创建数据库
conn = sqlite3.connect('first.db')
#2、获取游标
c = conn.cursor()
#3、执行语句
#3.1数据库DDL语句，创建user_tb、order_tb两个表
create_user_tb_SQL = '''create table user_tb(_id integer primary key autoincrement,
name text,
pass text,
gender text)'''
create_order_tb_SQL = '''create table order_tb(_id integer primary key autoincrement,
item_name text,
item_price real,
item_number real,
user_id integer,
foreign key(user_id) references user_tb(_id))'''
#c.execute(create_user_tb_SQL)
#c.execute(create_order_tb_SQL)

#3.2执行插入语句
#c.execute('insert into user_tb (name,pass,gender) values ("孙悟空","123456","male")')
#c.execute('insert into order_tb (item_name,item_price,item_number,user_id) values ("鼠标",34.2,3,1)')
#conn.commit()

#3.3执行多行插入
#4、关闭游标
c.close()
#5、关闭连接
conn.close()