#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/3/11 0010 9:27
@Author    :Alex Zhang
@File      :renderer.py
@Desc      :自定义渲染器
"""
from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('message', '请求成功')
                code = data.pop('code', renderer_context['response'].status_code)
            else:
                msg = '请求成功'
                code = renderer_context['response'].status_code

            ret = dict(
                code=code,
                message=msg,
                data=data
            )
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
