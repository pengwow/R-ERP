import os
import json
import random
import uuid
import xlrd
from datetime import datetime
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from common.utils import render_json, get_storage_path
from common.token import get_token, out_token
from .models import ZYImportData

# Create your views here.

@csrf_exempt
def upload_report(request):
    if request.method == "GET":
        return render(request, "login.html")
    fd = request.FILES.get('file')
    report_data = fd.read()
    storage_path = get_storage_path()
    file_name = str(uuid.uuid1())
    file_path = os.path.join(storage_path,file_name)
    with open(file_path,'wb') as uuid_fd:
        uuid_fd.write(report_data)
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0] #通过索引顺序获取
    nrows = table.nrows
    # ncols = table.ncols
    title = table.row_values(0)
    # print(title)
    zy_obj = ZYImportData()
    models_dict = zy_obj.get_models_dict()
    for i in range(1, nrows):
        row_dict = dict(zip(title,table.row_values(i)))
        new_dict = dict()
        for k, v in row_dict.items():
            new_key = models_dict.get(k)
            if new_key:
                new_dict[new_key] = v
        if new_dict.get('datetime',''):
            new_dict['datetime'] = datetime.strptime(new_dict.get('datetime',''),'%Y/%m/%d')
        if new_dict.get('id'):
            try:
                zy_obj = ZYImportData(**new_dict)
                zy_obj.save()
            except Exception as e:
                print(e)
                print(new_dict)
    # print(ZYImportData._meta.get_field('refund').help_text)
    # print(ZYImportData().get_models_dict())
    return render_json({},"导入成功！")

@csrf_exempt
def get_list(request):
    params = request.GET
    print(params)
    result = list()
    zy_objs = ZYImportData.objects.all()
    for item in zy_objs:
        zy_dict = model_to_dict(item)
        result.append(zy_dict)
    # TODO: 分页
    return render_json(result,"获取数据完成")