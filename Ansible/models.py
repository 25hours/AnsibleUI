from django.db import models
from UserAuthentication.models import UserProfile
# Create your models here.

class Task(models.Model):
    TaskId = models.AutoField(u'任务ID',primary_key=True,max_length=16)
    Name = models.CharField(u'任务名称',max_length=255)
    Description = models.TextField(u'任务描述',blank=True,null=True,default='')
    Hosts = models.CharField(u'主机',max_length=1024)
    Command = models.CharField(u'执行命令',max_length=1024)
    PlayBook = models.TextField(u'任务脚本')
    Script = models.TextField(u'Shell脚本')

class TaskInfo(models.Model):
    class Meta:
        ordering = ['-TaskId']
    Status_Choices = (
        ('Success', u'成功'),
        ('Running', u'执行中'),
        ('Failed', u'失败'),
        ('Pending', u'进入队列')
    )
    TaskId = models.OneToOneField(Task,primary_key=True)
    name = models.OneToOneField(UserProfile,verbose_name='任务发起人')
    ExecuteTime = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(u'执行状态',choices=Status_Choices,max_length=32)
    Result_stdout = models.TextField(u'执行成功信息',blank=True,editable=False,default='',null=True)
    Result_stderr = models.TextField(u'执行失败信息',blank=True,editable=False,default='',null=True)
