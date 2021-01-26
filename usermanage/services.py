#coding=utf-8
import json

from .models import LoginInfo

def verify_account(username,ip):
    login_info_ip = LoginInfo.objects.filter(lastLoginIp=ip,islocking=1)
    if len(login_info_ip) >0:
        return False, "IP已被锁定，禁止访问"
    login_info_ip = LoginInfo.objects.filter(lastLoginIp=ip,failNumber__gte=10)
    if len(login_info_ip) > 0:
        if not login_info_ip[0].islocking:
            login_info_ip[0].islocking = 1
            login_info_ip[0].save()
        return False, "IP地址总认证失败次数超过限制，禁止访问"
    login_info = LoginInfo.objects.filter(username=username,lastLoginIp=ip)
    if len(login_info) > 0:
        if login_info[0].failNumber > 5:
            login_info[0].islocking = 1
            login_info[0].save()
            return False, "用户认证错误次数超过限制，禁止访问"
    else:
        create_login_fail(username,ip)
    return True, "验证成功"

def update_failnumber(username,ip):
    login_info = LoginInfo.objects.filter(username=username,lastLoginIp=ip)
    if len(login_info):
        login_info[0].failNumber = login_info[0].failNumber + 1
        login_info[0].save()
    else:
        create_login_fail(username,ip)
    return

def create_login_fail(username,ip):
    login_info_dict = dict(username=username,lastLoginIp=ip,failNumber=1)
    logininfo = LoginInfo(**login_info_dict)
    logininfo.save()

def reset_user(username):
    login_info = LoginInfo.objects.filter(username=username)
    for item in login_info:
        item.delete()
    return