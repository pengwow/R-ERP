import json
import random
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from common.utils import render_json
from common.token import get_token, out_token
from .services import verify_account


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    # 验证账号
    username, password = verify_account(request)

    user_obj = auth.authenticate(username=username, password=password)
    if user_obj:
        auth.login(request,user_obj)
        result = dict(id=user_obj.id,
        username=user_obj.username,
        token=get_token(user_obj.username,60))
        return render_json(result,"登录成功！")
    return render_json({},"登录失败！")

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
