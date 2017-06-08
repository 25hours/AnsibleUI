from django.db import models
from UserAuthentication.models import UserProfile
# Create your models here.

class Task(models.Model):
    Name = models.CharField(u'任务名称',max_length=255)
    Description = models.CharField(u'任务描述',max_length=255)
    Hosts = models.CharField(u'主机',max_length=1024)
    Command = models.CharField(u'执行命令',max_length=1024)
    PlayBook = models.TextField(u'任务脚本')
    Script = models.TextField(u'Shell脚本')

Status_Choices = (
    ('Success',u'成功'),
    ('Running',u'执行中'),
    ('Failed',u'失败'),
    ('Pending',u'进入队列')
)

class TaskInfo(models.Model):
    TaskId = models.CharField(u'任务ID',max_length=16,unique=True)
    Sponsor = models.ForeignKey('UserProfile',verbose_name='任务发起人')
    Status = models.CharField(u'执行状态',choices=Status_Choices,max_length=32)