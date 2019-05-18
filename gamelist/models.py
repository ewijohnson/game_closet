from django.db import models
from django.urls import reverse


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.person_name

    def get_absolute_url(self):
        return reverse('gamelist_person_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('gamelist_person_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('gamelist_person_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['person_name']


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=45, unique=True)
    person = models.ManyToManyField(Person, related_name='games', blank=True, default='')

    def __str__(self):
        return '%s' % self.game_name

    def get_absolute_url(self):
        return reverse('gamelist_game_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('gamelist_game_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('gamelist_game_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['game_name']
