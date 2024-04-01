
from django.urls import path,include
from . import views
urlpatterns = [
   path('home/', views.home,name="home"),
   path('home/show/<int:id>', views.show,name="show"),
   path('home/login', views.log,name="log"),
   path('home/register', views.reg,name="reg"),
   path('home/register/login', views.registers,name="registers"),
   path('home/login/register', views.login,name="login"),
   path('home/filter/<int:fid>', views.filter,name="filter"),
]