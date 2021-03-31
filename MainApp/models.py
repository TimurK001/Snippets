from django.db import models
from datetime import datetime

LANG_CHOICES = [
    ('py','python'),
    ('cpp','C++'),
    ('js', 'java script'),
]

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.now())
