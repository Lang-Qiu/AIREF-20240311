from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    username = models.CharField(max_length=20, verbose_name="昵称", unique=True)
    phone = models.CharField(max_length=20, verbose_name="联系方式", default="", blank=True)
    cate = models.CharField(max_length=10, verbose_name="用户类型", blank=True)
    detail = models.CharField(max_length=1000, verbose_name="简介", blank=True)
    address = models.CharField(max_length=500, verbose_name="地址", blank=True)
    # upload_to指定了图片上传的位置
    # %Y%m%d是日期格式化的写法，会最终格式化为系统时间
    # avater = models.ImageField(upload_to='avatar/%Y%m%d/', verbose_name='头像', blank=True)

    # pic = models.CharField(max_length=300,verbose_name='头像')


# 3 class Meta:
#      verbose_name = 'UserInfo'
