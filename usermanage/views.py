import json
import random
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from common.utils import render_json,get_ip
from common.token import get_token, out_token
from .services import verify_account,update_failnumber, reset_user


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    ip = get_ip(request)
    # 验证账号
    status, message = verify_account(username,ip)
    if not status:
        return render_json({}, message ,code=100001)
    user_obj = auth.authenticate(username=username, password=password)
    if user_obj:
        auth.login(request,user_obj)
        result = dict(id=user_obj.id,
        username=user_obj.username,
        token=get_token(user_obj.username,60))
        return render_json(result,"登录成功！")
    else:
        update_failnumber(username,ip)
        return render_json({},"登录失败！",code=100002)

@csrf_exempt
def reset_account(request):
    data = json.loads(request.body)
    username = data.get('username')
    reset_user(username)
    return render_json({},"重置账号完成！")


@csrf_exempt
def logout(request):
    if request.method == "GET":
        raise Exception("1111")
    redirect('user/login')
    return render_json("注销成功")

@csrf_exempt
def twofactor(request):
    result = dict(stepCode=random.randint(0,1))
    return render_json(result)


def user_info(request):
    from .temp import get_role, user_info
    userinfo = user_info()
    return render_json(userinfo,"用户信息")
