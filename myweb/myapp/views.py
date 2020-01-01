from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from myapp.models import User,BlogsPost
from django.shortcuts import render_to_response
import json
from django.http.response import JsonResponse
#from config.run_method import RunMethod
import requests
class RunMethod:

    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res= requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data=None,header=None):
        res = None
        if header !=None:
            res = requests.get(url=url,data=data,headers=header).json()
        else:
            res= requests.get(url=url,data=data).json()
        return res



    def run_main(self,method,url,data,header=None):
        res = None
        if method =='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
from django import forms
# Create your views here.
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名：',max_length=100)
#     password = forms.CharField(label="密码：",widget=forms.PasswordInput())

#登陆
def login(request):
    #如果是post请求，就取出提交的数据，做登陆判断
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    return redirect(reverse('user_list'))
                else:
                    message = "密码或账号不正确"
                    return render(request,'login.html',{'error_msg':message})
            except:
                message = "用户名不存在"

    return render(request, 'login.html', {'error_msg': message})

#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')  # 显示注册页面
    message = ''
    if request.method == 'POST':
        #用户填写了新的username
        new_name = request.POST.get('username',None)
        new_password = request.POST.get('password',None)
        if new_name and new_password:
            if len(new_name)<6 or len(new_name) >10:
                message = '账号长度应为6-10位'
                return render(request, 'register.html', {'error_msg': message})
            User.objects.create(username=new_name,password=new_password)
            return render(request, 'login.html', {'error_msg': message})
        else:message = '账号或密码不能空'
    return render(request,'register.html',{'error_msg':message})


#展示所有用户
def user_list(request):
    #去数据库中查看所有用户
    ret = User.objects.all()
    return render(request,'user_list.html',{"user_list":ret})
#删除
def delete(request,pk):
    #删除指定的数据
    #1.从get请求的参数里面拿到将要删除的id
    # del_id = request.GET.get('user_id')
    # if del_id:
    #     del_obj=User.objects.get(user_id=del_id)
    #     del_obj.delete()
    #     #返回到展示所有用户页面
    #     return redirect(reverse('user_list'))
    # else:
    #     return HttpResponse("要删除的数据不存在")
    #
    User.objects.filter(pk=pk).delete()
    return redirect(reverse('user_list'))

#编辑用户
def edit_user(request):
    #获取提交的数据
    edit_id = request.GET.get('user_id')
    #查找到要编辑的对象
    user_obj = User.objects.get(user_id=edit_id)
    if request.method == 'POST':
        #获取新提交的数据
        edit_id = request.POST.get('user_id')
        new_user = request.POST.get('username')
        user_obj.username = new_user
        user_obj.save()
        return redirect('/user_list/')
    return render(request, 'edit_user.html', {'user': user_obj})

def blog_list(request):
    blog_list = BlogsPost.objects.all()
    return render(request,'blog_list.html',{'blog_list' :blog_list})

def login_in(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        result['user'] = username
        result['passwd'] = passwd
        #result = json.dumps(result)
        #return HttpResponse(result,content_type='')
        return JsonResponse(result)

    else:
        return render_to_response('login_in.html')

def index(request):
    pt=RunMethod()
    exr=request.POST.get('exr',None)
    data=""
    data1=""
    url = request.POST.get('url',None)
    header = request.POST.get('testdate',None)
    re_data =request.POST.get('header',None)
    mothod = request.POST.get('fun',None)
    if request.method=='POST':
        data=pt.run_main(mothod,url,data,header)
        result=data.json()
        data1=result['message']
        if int(result['message']==int(exr)):
            data=u'测试通过'
        else:
            data=u'测试失败'
    return render(request,"index.html",{"data":data,"data1":data1})


def add_args(a,b):
    x=int(a)
    y=int(b)
    return x+y

def post(request):
    if request.method=='POST':
        d={}
        if request.POST:
            a=request.POST.get('a',None)
            b=request.POST.get('b',None)
            if a and b:
                res=add_args(a, b)
                d['message']=res
                d=json.dumps(d)
                return HttpResponse(d)
            else:
                return HttpResponse(u'输入错误')
        else:
            return HttpResponse(u'输入为空')
    else:
        return HttpResponse(u'方法错误')



