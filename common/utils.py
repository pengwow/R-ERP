# coding=utf-8
import time
from django.http import JsonResponse

def render_json(result,message='',code=0,timestamp=None):
    if not message and result:
        message = str(result)
    if not timestamp:
        timestamp = time.clock()
    re = dict(result=result,message=message,code=code,timestamp=timestamp)
    return JsonResponse(re)