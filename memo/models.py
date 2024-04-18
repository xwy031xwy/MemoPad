from django.db import models
from django.utils import timezone
from datetime import datetime

# Memo Table
class Memo(models.Model):
    class Meta:
        verbose_name = 'Memo Table'
        verbose_name_plural = 'Memos Table'
        db_table = 'memo'

    content = models.CharField(verbose_name='メモ', max_length=100, default='', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.content + '(' + datetime(self.created_at).strftime('%Y/%m/%d %H:%M:%S') + ')'