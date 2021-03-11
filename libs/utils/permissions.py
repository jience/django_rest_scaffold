#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/3/11 0008 16:22
@Author    :Alex Zhang
@File      :permissions.py
@Desc      :自定义权限管理类
"""

from rest_framework import permissions


class CustomModelPermissions(permissions.DjangoModelPermissions):
    """
    重写 DjangoModelPermissions，添加view权限。
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
