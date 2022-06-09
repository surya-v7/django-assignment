from django.db import models


class Marks(models.Model):
    sem = models.CharField(max_length=255)
    marks = models.CharField(max_length=5)


class Skill(models.Model):
    type = models.CharField(max_length=255)
    list = models.CharField(max_length=255)
