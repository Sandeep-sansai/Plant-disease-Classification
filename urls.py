

from django.urls import path
from django.urls import re_path as url  # Import the url function
from .views import predictImage,HomePage,SignupPage,LoginPage,LogoutPage,index1


urlpatterns = [
    path('',HomePage,name='home'),
    path('index1', index1, name='index1'),
    path('signup/',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    url('^$',index1,name='homepage'),
    # url('^$',index,name='homepage'),
    url('predictImage',predictImage,name='predictImage'),
]