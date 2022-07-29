"""hobbyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
from accounts import views as a_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', a_views.login, name='login'),
    path('logout/', a_views.logout, name='logout'),
    path('register', a_views.register, name='register'),
    
    path('todo/', views.todo, name='todo'),
    path('modify/<int:id>', views.modify, name='modify'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('done/<int:id>', views.done, name='done'),
    path('others/', views.others, name='others'),
    path('detail/<int:id>', views.detail, name='detail'),
]
