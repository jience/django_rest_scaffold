"""django_scaffold URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify

from apis.user.views import UserViewSet
from apis.user.views import GroupViewSet

import xadmin
xadmin.autodiscover()

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include(router.urls)),
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),
    path('api/token/refresh/', token_refresh, name='token_refresh'),
    path('api/token/verify/', token_verify, name='token_verify'),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
