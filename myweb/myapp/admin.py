from django.contrib import admin

# Register your models here.
from myapp.models import BlogsPost,User

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','body','create_time']
admin.site.register(BlogsPost,BlogsPostAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','create_time']
admin.site.register(User,UserAdmin)
