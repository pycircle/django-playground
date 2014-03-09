from django.contrib import admin

from playground.blog import models


admin.site.register(models.Category)
admin.site.register(models.Post)
