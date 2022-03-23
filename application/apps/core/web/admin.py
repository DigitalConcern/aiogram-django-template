from django.contrib import admin

from .. import models

# Register your models here.
# To get django model: models.<ModelName>.DjangoModel

admin.site.register(models.User)


# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):
#     pass
