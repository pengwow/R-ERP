#coding=utf-8
import json

from .models import LoginInfo

def verify_account(username,ip):
    login_info = LoginInfo.objects.filter(username=username,lastLoginIp=ip)
    if len(login_info) > 0:
        if login_info[0].failNumber > 5:
            raise Exception("超过最大失败次数，禁止登录")
    return

def update_failnumber(username,ip):
    login_info = LoginInfo.objects.filter(username=username,lastLoginIp=ip)
    if len(login_info):
        login_info[0].failNumber = login_info[0].failNumber + 1
        login_info[0].save()
    else:
        login_info_dict = dict(username=username,lastLoginIp=ip,failNumber=1)
        logininfo = LoginInfo(**login_info_dict)
        logininfo.save()
    return

def reset_user(username):
    login_info = LoginInfo.objects.filter(username=username)
    for item in login_info:
        item.delete()
    return