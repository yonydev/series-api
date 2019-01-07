from django.db import models

# Create your models here.


class Serie(models.Model):
    """
    Class that holds Serie information
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    cover = models.CharField(max_length=50, blank=False, null=False)
    serie_type = models.CharField(max_length=50, blank=False, null=False)
    language = models.CharField(max_length=50, blank=False, null=False)
    music = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(max_length=4, blank=False, null=False)
    # genre = models.
    # cast = models.ForeignKey()
    # directors = models.ForeignKey()
    # characters = models.ForeignKey()
    # seasons = models.ForeignKey()


class Person(models.Model):
    """
    Class that holds Cast information
    """
    name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    # series = models.ForeignKey()


class Character(models.Model):
    """
    Class that holds Character information
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(max_length=4, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=False, null=False)
    # actor = models.ForeignKey()
    # seasons = models.ForeignKey()
    # chapters = models.ForeignKey()
