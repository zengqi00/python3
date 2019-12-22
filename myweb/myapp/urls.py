from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from myapp import views



urlpatterns = [
    path('', views.login),

    url(r'^login/$',views.login,name='login'),
    url(r'^user_list/$', views.user_list,name='user_list'),
    url(r'^register/$', views.register ,name='register'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete,name='delete'),
    url(r'^edit_user/', views.edit_user,name='edit'),
    url(r'^blog_list/$', views.blog_list,name='blog_list'),
    url(r'^login_in/$',views.login_in),



    path('admin/', admin.site.urls),
]
