
from django.contrib import admin
from django.urls import path
from .import views
from .models import statuscategory
from .models import statusdescription



urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('setting/',views.setting,name="setting"),
    path('signup/',views.signup,name="signup"),
    path('comments/<int:pk>',views.comments.as_view(),name='comments'),
    path('edit/<int:pk>',views.edit.as_view(),name='edit'),
    path('post/<int:pk>/delete',views.delete.as_view(),name='delete'),
    path('search/',views.search,name='search'),
    
    
]