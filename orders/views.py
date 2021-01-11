import os
import json
import random
import uuid
import xlrd
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
    print(title)
    zy_obj = ZYImportData()
    models_dict = zy_obj.get_models_dict()
    for i in range(1, nrows):
        row_dict = dict(zip(title,table.row_values(i)))
        new_dict = dict()
        for k, v in row_dict.items():
            new_key = models_dict.get(k)
            new_dict[new_key] = v
        print(new_dict)
        ZYImportData.objects.update_or_create(id=new_dict.get('id'),defaults=new_dict)
        # print(str(row_dict))
        # model_data = row_dict
        # ZYImportData(**model_data)
        # print(table.row_values(i))

    print(ZYImportData._meta.get_field('refund').help_text)
    print(ZYImportData().get_models_dict())
    return render_json({},"导入成功！")

@csrf_exempt
def get_list(request):
    params = request.GET
    if params:
        zy_obj = ZYImportData.objects.filter(**params)
        for item in zy_obj:
            paas
        return


    return