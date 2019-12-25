
import xlrd
# data = xlrd.open_workbook('case.xlsx')
# tables = data.sheet_by_index(0)

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
            self.data = self.get_data()
        else:
            self.file_name='case.xlsx'
            self.sheet_id=0
        self.data=self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_index(self.sheet_id)
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取某一个单元格的内容
    def get_cell_value(self,row,rol):
        return self.data.cell_value(row,rol)






if __name__ =='__main__':
    opers=OperationExcel()
    print(opers.get_data().nrows)
    print(opers.get_cell_value(0,1))