from django.db import models

# Create your models here.

class MemoTemplateModel(models.Model):
    """备忘录"""
    memo_id = models.AutoField(primary_key=True)
    memo_name = models.CharField(max_length=10,help_text='名称')
    memo_time = models.DateTimeField(auto_now=True,null=True, help_text='最后修改日期')
    memo_tent = models.CharField(max_length=100,help_text='内容')

    class Meta:
        db_table = 'memoa'