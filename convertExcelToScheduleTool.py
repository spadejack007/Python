import xlrd

'''
根据自己定义的个人进度规划表格，转化为可以导入管理系统的表格
'''

def read_excel():
    #打开文件
    workbook = xlrd.open_workbook(r"a.xls")
    print(workbook.sheet_names())
    sheet = workbook.sheet_by_index(0)#第一个表格作为
    
    print(sheet.nrows)
    print(sheet.ncols)
    
    print(sheet.cell(0,3).value)

if __name__ == '__main__':
    read_excel()