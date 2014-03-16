# -*- coding: utf-8 -*-

from django.contrib import admin
from playground.blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'posted')
    list_filter = ('posted',)
    search_fields = ('author__username', 'title')


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)


"""
Zadanie na teraz:
Napisz CategoryAdmin, spraw, by wyglądaj jakoś inaczej.
Np. Możliwość wyszukiwania kategorii,
tak aby uwzględniał podkategorie (np. Szukając Jedzenie wyświetli mi Pizza)
"""