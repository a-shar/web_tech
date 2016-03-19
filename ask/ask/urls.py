"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from qa.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'^login/', auth_views.login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/', auth_views.logout),
    url(r'^signup/', signup),
    url(r'^question/(?P<qid>\d+)/', question_detail),
    url(r'^ask/', ask),
    url(r'^popular/', popular_page),
    url(r'^new/', test),
    url(r'^answer/', answer),
]
