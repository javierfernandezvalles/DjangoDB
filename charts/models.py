# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'charts'


class Genres(models.Model):
    genreid = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'genres'
        app_label = 'charts'



class Hasagenre(models.Model):
    movieid = models.ForeignKey('Movies', models.DO_NOTHING, db_column='movieid', primary_key=True)
    genreid = models.ForeignKey(Genres, models.DO_NOTHING, db_column='genreid')

    class Meta:
        managed = False
        db_table = 'hasagenre'
        app_label = 'charts'
        unique_together = (('movieid', 'genreid'),)


class Movieavg(models.Model):
    movieid = models.IntegerField(blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movieavg'
        app_label = 'charts'


class Movies(models.Model):
    movieid = models.IntegerField(primary_key=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'movies'
        app_label = 'charts'


class Query1(models.Model):
    name = models.TextField(blank=True, null=True)
    moviecount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query1'
        app_label = 'charts'


class Query2(models.Model):
    name = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query2'
        app_label = 'charts'


class Query3(models.Model):
    title = models.TextField(blank=True, null=True)
    countofratings = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query3'
        app_label = 'charts'


class Query4(models.Model):
    movieid = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query4'
        app_label = 'charts'


class Query5(models.Model):
    title = models.TextField(blank=True, null=True)
    average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query5'
        app_label = 'charts'


class Query6(models.Model):
    average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query6'
        app_label = 'charts'


class Ratings(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    movieid = models.ForeignKey(Movies, models.DO_NOTHING, db_column='movieid')
    rating = models.DecimalField(max_digits=65535, decimal_places=65535)
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ratings'
        app_label = 'charts'
        unique_together = (('userid', 'movieid'),)


class Sim(models.Model):
    movieid1 = models.IntegerField(blank=True, null=True)
    movieid2 = models.IntegerField(blank=True, null=True)
    sim = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'
        app_label = 'charts'


class Simquery(models.Model):
    movieid1 = models.IntegerField(blank=True, null=True)
    movieid2 = models.IntegerField(blank=True, null=True)
    sim = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simquery'
        app_label = 'charts'


class Taginfo(models.Model):
    tagid = models.IntegerField(primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'taginfo'
        app_label = 'charts'


class Tags(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    movieid = models.ForeignKey(Movies, models.DO_NOTHING, db_column='movieid')
    tagid = models.ForeignKey(Taginfo, models.DO_NOTHING, db_column='tagid')
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tags'
        unique_together = (('userid', 'movieid', 'tagid'),)


