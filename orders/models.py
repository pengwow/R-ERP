from django.db import models

# Create your models here.
# class Orders(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         db_table = "orders"
#         verbose_name = "订单表"


class ZYImportData(models.Model):
    id = models.IntegerField(primary_key=True,blank=True,help_text="id") # ID number of Zhiying order
    no = models.CharField(max_length=32,blank=True,help_text="no") # verbose_name="Sales Order No"
    datetime = models.DateTimeField(blank=True,help_text="时间") # verbose_name="Order time",
    business_manager = models.CharField(max_length=32,blank=True,help_text="业务员") # verbose_name="business manager",
    source = models.CharField(max_length=32,blank=True,help_text="来源") # verbose_name="Account source",
    currency = models.CharField(max_length=16,blank=True,help_text="币种") # verbose_name="Currency",
    price = models.FloatField(blank=True,help_text="金额") # verbose_name="amount of money"
    cost = models.FloatField(blank=True,help_text="费用") # verbose_name="production cost",
    refund = models.FloatField(blank=True,help_text="费用") # verbose_name="drawback refund reimburse",
    income = models.FloatField(blank=True,help_text="人民币收入")
    purchasing_cost = models.FloatField(blank=True,help_text="采购成本")
    profit = models.FloatField(blank=True,help_text="利润")
    product_id = models.CharField(max_length=32,blank=True,help_text="产品ID")
    asin = models.CharField(max_length=32,blank=True,help_text="ASIN")
    sku = models.CharField(max_length=64,blank=True,help_text="SKU")
    zh_name = models.CharField(max_length=64,blank=True,help_text="中文简称")
    gross_weight = models.IntegerField(blank=True,help_text="毛重")
    size = models.CharField(max_length=16,blank=True,help_text="尺寸")
    quantity = models.IntegerField(blank=True,help_text="数量")
    logistics = models.CharField(max_length=16,blank=True,help_text="物流")
    channel = models.CharField(max_length=64,blank=True,help_text="渠道")
    waybill_no = models.CharField(max_length=64,blank=True,help_text="运单号")
    track_no = models.CharField(max_length=64,blank=True,help_text="追踪号")
    freight = models.FloatField(blank=True,help_text="运费")
    order_remarks = models.CharField(max_length=200,blank=True,help_text="订单备注")
    region = models.CharField(max_length=10,blank=True,help_text="地区")
    buyer = models.CharField(max_length=32,blank=True,help_text="买家名称")
    mailbox = models.CharField(max_length=128,blank=True,help_text="邮箱")
    telephone = models.CharField(max_length=64,blank=True,help_text="电话")
    city = models.CharField(max_length=32,blank=True,help_text="城市")
    state = models.CharField(max_length=16,blank=True,help_text="州省")
    postcode = models.CharField(max_length=16,blank=True,help_text="邮编")
    address = models.CharField(max_length=128,blank=True,help_text="地址")

    class Meta:
        db_table = "zy_import_data"
        verbose_name = "智盈导入数据"