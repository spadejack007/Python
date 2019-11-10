'''
1、调用connect()方法打开数据库连接，该方法返回数据库连接对象
2、通过数据库连接对象打开游标
3、使用游标执行SQL语句(包含DDL、DML、select查询语句等)
4、关闭游标
5、关闭数据库连接
6、本例子练习了a、数据库连接、b、执行语句、d、执行多条插入、d、执行多次获取、e、sqlite自定义函数 f、自定义聚集函数
***************
1、python如果只带一个元素的元组，元素后面要加一个","  逗号。 
2、DML语句(Data Manipulation Language)：用于增删改表中数据，DML是伴随TCL事务控制的。
3、DDL语句(Data Definition Language)：数据定义语言，用来维护数据库对象 
4、rowcount属性在update语句后面才会返回行数，默认是-1
**************MySQL与SQLite不同之处
1、#mysql的语句：a、整型为int b、字符型的为varchar c、浮点型为double d、自增长auto_increment
2、占位符为%s
3、存储过程定义前要使用DELIMITER
'''
import mysql.connector

#1、打开或创建数据库
conn = mysql.connector.connect(user = 'root', password = 'xueshan007',host = 'localhost',port = '3306',database = 'python',use_unicode = True)
#mysql的连接语句比SQLite的多了很多参数
#2、获取游标
c = conn.cursor()
#3、执行语句
#***3.1、3.2、3.3多个章节的语句可以逐次打开执行***#
#3.1数据库DDL语句，创建user_tb、order_tb两个表
create_user_tb_SQL = '''create table user_tb(user_id int primary key auto_increment,
name varchar(255),
pass varchar(255),
gender varchar(255))'''
create_order_tb_SQL = '''create table order_tb(order_id int primary key auto_increment,
item_name varchar(255),
item_price double,
item_number double,
user_id int,
foreign key(user_id) references user_tb(user_id) )'''
c.execute(create_user_tb_SQL)
c.execute(create_order_tb_SQL)

#3.2执行插入语句
#c.execute('insert into user_tb (name,pass,gender) values (%s,%s,%s)',("孙悟空","123456","male"))
#conn.commit()

#3.3执行多行插入
#insertManyList = (("sun","123456","male"),("bai","123456","female"),("zhu","123456","male"))
#c.executemany('insert into user_tb (name,pass,gender) values (%s,%s,%s)',insertManyList)#此处用了占位符"%s"
#conn.commit()

#3.3.1执行多行插入-通过设置autocommit属性
#conn.autocommit = True
#insertManyList = (("zhang","123456","male"),("liu","123456","female"),("li","123456","male"))
#c.executemany('insert into user_tb (name,pass,gender) values (%s,%s,%s)',insertManyList)#此处用了占位符"%s"

#3.4执行获取数据并逐行呈现
'''c.execute('select * from user_tb where user_id > %s',(1,))
#print('查询返回的记录数：',c.rowcount)
#通过游标的descritpion属性获取列信息
for col in (c.description):
    print(col[0],end = '\t')
print('\n','- '*30)
while True:
    row = c.fetchone()
    if not row:
        break
    print(row)
    print(row[1]+'---->'+row[2])'''

#3.5调用存储函数callproc(self,procname,args=())
'''#使用自定义函数。场景：可以用于密码加密
****************（*号内的为存储过程在mysql8.0中定义）
DELIMITER //
create procedure add_proc(in a int,in b int,out sum_result int) 
BEGIN
set sum_result = a + b;
END;//
****************
restult_args = c.callproc('add_proc',(5,6,0))
print(restult_args)
print(restult_args[2])'''

#4、关闭游标
c.close()
#5、关闭连接
conn.close()