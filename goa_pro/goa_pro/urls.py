"""goa_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from goa_app import views

admin.site.site_header = "Sewak Meghwal Admin Portal"
admin.site.site_title = "Tourist Place Admin Portal"
admin.site.index_title = "Welcome to Tourist Place Admin"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('show',views.show,name='show'),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('res_read<int:id>',views.res_read,name='res_read'),
    path('form',views.form,name='form'),
    path('search',views.search,name='search'),
    path('state/<str:state1>',views.state_fil,name='state'),
    path('diff',views.diff_plsce,name='diff_place'),
    path('hotels',views.hotels,name='hotels'),
    path('season/<str:season1>',views.season_fil,name='honeymoon'),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('changep',views.changep,name='changep'),
    path('profileimage',views.profile_image,name='profileimage'),
    path('update<int:id>',views.update,name='update'),









    




]
