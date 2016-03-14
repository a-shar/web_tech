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
from django.conf.urls import include, url, handler404
from django.contrib import admin
from qa.views import test

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', handler404),
    url(r'^login/', handler404),
    url(r'^signup/', handler404),
    url(r'^question/(?P<qid>\d+)/', test),
    url(r'^ask/', handler404),
    url(r'^popular/', handler404),
    url(r'^new/', handler404),
]
