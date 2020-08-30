from django.urls import path
from . import views
from django.views.generic import TemplateView

from django.conf.urls import url


urlpatterns = [
    path('', views.logine,name="login"),
    path('admin/',views.admin,name="admin"),
    path('black', views.black,name="black"),
    path('index',views.index,name='index'),
    #path('signup',views.signup,name='signup'),
    path('admin_add',views.admin_add,name="admin_add"),
    path('admin_update',views.admin_update,name="admin_update"),
    path('update_id_catch',views.update_id_catch,name="update_id_catch"),
    path('admin_delete',views.admin_delete,name="admin_delete"),
    path('registration',views.registration,name="registration"),
    path('admin_search',views.admin_search,name="admin_search"),
    path('user_search',views.user_search,name="user_search"),
    path('logout',views.logout,name="logout"),
    path('user_list',views.user_list, name="user_list")
    #url(r'^registration/$', views.registration, name='registration')
]