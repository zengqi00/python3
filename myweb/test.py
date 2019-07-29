import re
def emails(e):
    if len(e) >=5:
        if re.match('[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]',e)!= None:
            return '邮箱格式正确'
    return '邮箱格式错误'





e = input('请输入邮箱：')
print (emails(e))







