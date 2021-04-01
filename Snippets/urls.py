"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from MainApp import views

from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets_add'),
    # path('snippets/create', views.snippet_create),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippet/<int:id>', views.snippet_page, name='snippet_page'),
    path('auth/login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mysnippets/', views.my_snippets, name='my_snippets'),
    path('auth/register/', views.registration, name='registration'),
    path('comment/add', views.comment_add, name="comment_add"),
    path('admin/', admin.site.urls),
]

