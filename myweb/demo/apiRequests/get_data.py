from operation_excel import OperationExcel
import data_config
from operation_json import OperetionJson
class GetData:
    def __init__(self):
        self.opera_excel=OperationExcel()
    #获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    def get_is_run(self,row):  #获取是否执行
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(col)
        if run_model =='yes':
            Flag = True
        else:
            flag = False
        return False
    def is_header(self,row):  #是否携带header
        col = data_config.get_headr()
        header = self.opera_excel.get_cell_value(col)
        if header =='yes':
            return data_config.get_header_value()
        else:
            return None
    def get_request_method(self,row): #获取请求方式
        col = data_config.get_request_way()
        request_method = self.opera_excel.get_cell_value(col)
        return request_method
    def get_request_url(self,row): #获取url
        col = data_config.get_url()
        request_url = self.opera_excel.get_cell_value(col)
        return request_url
    def get_request_data(self,rpw): #获取请求数据
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(col)
        if data == '':
            return None
        return data
    def get_data_for_json(self,row): #通过关键字拿到数据
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return  request_data
    def get_expect_data(self,row): #获取预期结果
        col=data_config.get_expext()
        expect =   self.opera_excel.get_cell_value(row,col)
        if expect=='':
            return None
        return expect

        