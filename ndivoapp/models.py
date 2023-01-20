from django.db import models
from django.db import models

class PdfFile(models.Model):
    file = models.FileField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)
