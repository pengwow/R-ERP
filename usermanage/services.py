#coding=utf-8
import json
from common.utils import get_ip
from .models import LoginInfo

def verify_account(request):

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    ip = get_ip(request)

    login_info = LoginInfo.objects.filter(username=username,lastLoginIp=ip)
    if len(login_info) > 0:
        if login_info[0].failNumber > 5:


    return username, password
