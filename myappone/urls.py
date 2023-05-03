from django.urls import path
from . import views

urlpatterns = [

    path("login",views.login,name='login1'),
    path("login1",views.login,name='login1'),
    path("register",views.register,name='register'),
    path("logout",views.logout, name = "logout"),
    path("",views.home,name='home1'),
    path('base1.html',views.base1,name='base1'),
    path('home1.html',views.home,name='home1'),
    path('register1.html',views.register,name='register1'),
    path('login1.html',views.login,name='login1'),
    path('empadd.html',views.empadd,name='empadd.html'),
    path('empretrive.html',views.employee_list,name='empretrive'),
    path('delete_data/<int:empid>',views.delete_data,name='delete_data'),
    path('edit_data/<int:empid>',views.update_data,name='update_data'),
    path('update_data/<int:empid>',views.edit_data,name='edit_data'),
    path('default.html',views.defaultpage,name='default'),
    path('update_data/empadd.html',views.update_empadd,name='upadd'),
    path('update_data/empretrive.html',views.update_empret,name='upempret'),
    path('update_data/default.html',views.update_default,name='updefault')
]