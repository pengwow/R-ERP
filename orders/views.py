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
    for i in range(1, nrows):
        row_dict = dict(zip(title,table.row_values(i)))
        print(str(row_dict))
        # model_data = row_dict
        # ZYImportData(**model_data)
        # print(table.row_values(i))
    # raise Exception("1111")
    return render_json({},"导入成功！")