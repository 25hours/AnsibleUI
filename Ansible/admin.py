from django.contrib import admin

# Register your models here.
from Ansible import models
admin.site.register(models.Task)
admin.site.register(models.TaskInfo)