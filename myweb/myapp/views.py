from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import User,BlogsPost

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
                    return redirect('/user_list/')
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
            return render(request,'success.html')
        else:message = '账号或密码不能空'
    return render(request,'register.html',{'error_msg':message})


#展示所有用户
def user_list(request):
    #去数据库中查看所有用户
    ret = User.objects.all()
    return render(request,'user_list.html',{"user_list":ret})
#删除
def delete(request):
    #删除指定的数据
    #1.从get请求的参数里面拿到将要删除的id
    del_id = request.GET.get('user_id')
    if del_id:
        del_obj=User.objects.get(user_id=del_id)
        del_obj.delete()
        #返回到展示所有用户页面
        return redirect("/user_list/")
    else:
        return HttpResponse("要删除的数据不存在")
#编辑用户
def edit_user(request):
    if request.method == 'POST':
        #获取用户信息
        edit_id = request.POST.get('user_id')
        new_user = request.POST.get('username')
        edit_username = User.objects.get(user_id = edit_id)
        edit_username.username = new_user
        edit_username.save()
        return redirect('/user_list/')

    ed_id=request.GET.get('user_id')
    if ed_id:
        #获取当前编辑的用户
        user_obj = User.objects.get(user_id = ed_id)
        return render(request,'edit_user.html',{'user':user_obj})

def blog_list(request):
    blog_list = BlogsPost.objects.all()
    return render(request,'index.html',{'blog_list' :blog_list})








