from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 업로드 경로를 년월일로 각 폴더에다가 저장하는 방법으로 권장
    img = models.ImageField(blank=True,upload_to='%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
