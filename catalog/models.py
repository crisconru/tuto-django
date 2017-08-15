from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=150, blank=False, help_text='Nombre del grupo musical')
    web = models.URLField(blank=True, default='')
    bio = models.TextField(blank=False, help_text='Biografia del grupo')