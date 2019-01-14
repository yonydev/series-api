from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    year = models.IntegerField(blank=False, null=False)
    genre = ArrayField(
        models.CharField(max_length=80, blank=False)
    )

    cast = ArrayField(
        models.ForeignKey('Person', on_delete=models.CASCADE,
                          blank=False, null=False,
                          limit_choices_to={'person_type': 'actor'}),
        blank=False,
        null=False
    )
    voices = ArrayField(
        models.ForeignKey('Person', on_delete=models.CASCADE,
                          blank=False, null=False,
                          limit_choices_to={'person_type': 'voice'}),
        blank=False,
        null=False
    )
    directors = ArrayField(
        models.ForeignKey(
            'Person', on_delete=models.CASCADE,
            blank=False, null=False,
            limit_choices_to={'person_type': 'director'}
        )
    )
    characters = ArrayField(
        models.ForeignKey(
            'Character', on_delete=models.CASCADE,
            blank=False, null=False
        )
    )
    seasons = ArrayField(
        models.ForeignKey('Season', blank=True, null=True,
                          on_delete=models.CASCADE)
    )


PERSON_CHOICES = (
    (u'actor', u'Actor'),
    (u'voice', u'Voice'),
    (u'director', u'Director'),
)


class Person(models.Model):
    """
    Class that holds Cast information
    """
    name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    biography = models.CharField(max_length=255, blank=True, null=True)
    portfolio = ArrayField(
        models.CharField(max_length=100, blank=False)
    )
    person_type = models.CharField(
        max_length=15, choices=PERSON_CHOICES, blank=False, null=False)


class Character(models.Model):
    """
    Class that holds Character information
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=False, null=False)
    actor = models.ForeignKey('Person', on_delete=models.CASCADE,
                              blank=False, null=False,
                              limit_choices_to={'person_type': 'actor'},
                              related_name="+")
    voice = models.ForeignKey('Person', on_delete=models.CASCADE,
                              blank=False, null=False,
                              limit_choices_to={'person_type': 'voice'},
                              related_name="+")
    chapters = ArrayField(
        models.ForeignKey('Chapter', blank=True, null=True,
                          on_delete=models.CASCADE)
    )
    seasons = ArrayField(
        models.ForeignKey('Season', blank=True, null=True,
                          on_delete=models.CASCADE)
    )


class Season(models.Model):
    """
    Class that holds Season information
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    chapters = ArrayField(
        models.ForeignKey('Chapter', blank=True, null=True,
                          on_delete=models.CASCADE)
    )
    release_year = models.CharField(
        max_length=4, default="1900", blank=False, null=False)


class Chapter(models.Model):
    """
    Class that holds Chapter information
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
