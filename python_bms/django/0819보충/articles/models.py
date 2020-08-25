from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255) #제목제목 => string
    content = models.TextField() # 내용내용 => string
    created_at = models.DateTimeField(auto_now_add=True) # datetime 객체
    updated_at = models.DateTimeField(auto_now=True) # datetime 객체