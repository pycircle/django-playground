# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="autor", null=True)
    posted = models.DateTimeField(
        verbose_name="opublikowano", auto_now_add=True)
    title = models.CharField(verbose_name="tytuł", max_length=50)
    text = models.TextField(verbose_name="treść")
    url = models.URLField(
        verbose_name="strona internetowa", null=True, blank=True)
    category = models.ForeignKey("Category", verbose_name="Kategoria")

    def __unicode__(self):
        if self.author:
            return self.author.username + ":" + self.title
        else:
            return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})


class Category(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=200)
    subcategory = models.ForeignKey(
        "self", verbose_name="Podkategoria", null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
