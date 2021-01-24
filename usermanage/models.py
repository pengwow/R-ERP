from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

class LoginInfo(models.Model):
    id = models.IntegerField(verbose_name='主键',primary_key=True)
    username = models.CharField(verbose_name='用户名',max_length=150,null=True,blank=True)
    lastLoginIp = models.CharField(verbose_name='上次登录IP',name='last_login_ip',max_length=32,blank=True,null=True)
    lastLoginTime = models.DateTimeField(verbose_name='上次登录时间',name='last_login_time',auto_now=True,blank=True,null=True)
    failNumber= models.IntegerField(verbose_name='失败次数',default=0)

    class Meta:
        db_table = "login_info"
        verbose_name = "登录信息表"