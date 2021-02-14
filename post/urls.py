from django.contrib import admin
from django.urls import path
from .import views
from  .views import edit_profile
from  .views import profile_pic_change


urlpatterns = [
   
    path('',views.profile.as_view(),name='profile'),
    path('status_form/',views.status_form,name='status_form'),
    path('comment_form/',views.comment_form,name='comment_form'),
    path('profile_pic/',views.profile_pic,name='profile_pic'),
    path('edit_profile/',edit_profile.as_view(),name='edit_profile'),
    path('profile_pic_change/',views.profile_pic_change,name='profile_pic_change'),
    
    
    

 
    
]