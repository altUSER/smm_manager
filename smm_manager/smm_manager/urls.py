"""smm_manager URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path

from ui import views, setting_view, new_publication_view, json_posts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect_to_del_post),
    path('delayed_posts/', views.delayed_posts, name='delayed_posts'),
    path('published_posts/', views.published_posts, name='published_posts'),
    path('new_publication/', new_publication_view.new_publication, name='new_publication'),
    path('settings/', setting_view.settings, name='settings'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('get_json_published_posts/', json_posts_view.get_json_published_posts, name='get_json_published_posts'),\
    path('get_json_delayed_posts/', json_posts_view.get_json_delayed_posts, name='get_json_delayed_posts'),
]
