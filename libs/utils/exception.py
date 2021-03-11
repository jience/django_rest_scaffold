#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/3/11 0009 17:37
@Author    :Alex Zhang
@File      :exception.py
@Desc      :自定义异常处理
"""
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.views import Response


def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准的错误响应对象
    response = exception_handler(exc, context)

    if response is None:
        return Response({
            'message': '服务器错误:{exc}'.format(exc=exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    else:
        return Response({
             'message': '服务器错误:{exc}'.format(exc=exc)
        }, status=response.status_code, exception=True)


# def custom_exception_handler(exc, context):
#     # 先调用REST framework默认的异常处理方法获得标准的错误响应对象
#     response = exception_handler(exc, context)
#
#     # 在此处补充自定义的异常处理
#     if response is not None:
#         response.data.clear()
#         response.data['code'] = response.status_code
#         response.data['data'] = []
#
#         if response.status_code == status.HTTP_400_BAD_REQUEST:
#             response.data['message'] = 'Parse error'
#         elif response.status_code == status.HTTP_401_UNAUTHORIZED:
#             response.data['message'] = 'Not authentication'
#         elif response.status_code == status.HTTP_403_FORBIDDEN:
#             response.data['message'] = 'Permission denied'
#         elif response.status_code == status.HTTP_404_NOT_FOUND:
#             response.data['message'] = 'Not found'
#         elif response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
#             response.data['message'] = 'Method not allowed'
#         elif response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
#             response.data['message'] = 'Not acceptable'
#         elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
#             response.data['message'] = 'Interval error'
#
#     return response
