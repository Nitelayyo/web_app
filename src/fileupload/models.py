from django.db import models


class FileUpLoad(models.Model):
    file = models.FileField()
