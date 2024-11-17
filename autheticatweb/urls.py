# self 
from django.urls import path,include
from autheticatweb import views
from django.conf import settings


urlpatterns = [
   
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('addproduct/',views.addproduct),
    path('yourworld/',views.order),
    path('login/',views.loginu),
    path('signup/',views.signup),
    path('logout/',views.logouthandle,name="logouthandle"),
    path('send/', views.send_message, name='send_message'),
    path('display/', views.display_messages, name='display_messages'),
   
    
]