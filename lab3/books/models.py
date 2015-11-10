from django.db import models
from django.contrib import admin

class Author(models.Model):   
    name = models.CharField(u'姓名', max_length=100)
    age = models.IntegerField(u'年龄', max_length=100)
    AuthorID = models.CharField( max_length=100)
    country = models.CharField(u'国籍',max_length=100)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(u'书名',max_length=100)
    ISBN  = models.CharField( max_length=100)
    #authorsID = models.ManyToManyField(Author)
    authorsID = models.ForeignKey(Author)
    Publisher = models.CharField(u'出版商',max_length=100)
    PublishDate = models.DateField(u'出版日期')
    Price = models.FloatField(u'价格')
    #def __unicode__(self):
      #  return self.title
admin.site.register(Author)
admin.site.register(Book)