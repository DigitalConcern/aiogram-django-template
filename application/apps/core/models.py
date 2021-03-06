# from tortoise import Tortoise, fields
# from tortoise.models import Model
from django.db import models
# from orm_converter.tortoise_to_django import ConvertedModel


class User(models.Model):
    tg_id = models.CharField("Telegram User ID", max_length=255)
    username = models.CharField("Telegram Username", max_length=255)

    def __str__(self) -> str:
        return f"{self.username} - {self.tg_id}"


class Comment(models.Model):
    text = models.CharField("Message text", max_length=1000)
