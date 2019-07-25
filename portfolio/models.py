from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

#upload_to = 'images/' 란? #media 경로 아래에 위치한 디렉토리
