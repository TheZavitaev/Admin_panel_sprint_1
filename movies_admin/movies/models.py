import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from model_utils.models import TimeStampedModel


class Person(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField(_('полное имя'))
    birth_date = models.DateField(_('дата рождения'), null=True)
    created_at = AutoCreatedField(_('дата создания'))

    class Meta:
        verbose_name = _('персона')
        verbose_name_plural = _('персоны')
        db_table = 'content.person'

    def __str__(self):
        return self.full_name


class Genre(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(_('название'))
    description = models.TextField(_('описание'), blank=True)
    created_at = AutoCreatedField(_('дата создания'))

    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')
        db_table = 'content.genre'

    def __str__(self):
        return self.name


class RoleType(models.TextChoices):
    ACTOR = 'actor', _('актер')
    WRITER = 'writer', _('сценарист')
    DIRECTOR = 'director', _('режиссер')


class FilmWorkType(models.TextChoices):
    MOVIE = 'film', _('фильм')
    SERIES = 'series', _('сериал')
    TV_SHOW = 'tv_show', _('шоу')


class MPAARatingType(models.TextChoices):
    G = 'general', _('без ограничений')
    PG = 'parental_guidance', _('рекомендовано смотреть с родителями')
    PG_13 = 'parental_guidance_strong', _('просмотр не желателен детям до 13 лет')
    R = 'restricted', _('до 17 в сопровождении родителей')
    NC_17 = 'no_one_17_under', _('только с 18')


class FilmWork(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)
    creation_date = models.DateField(_('дата создания фильма'), null=True, blank=True)
    certificate = models.TextField(_('сертификат'), blank=True, null=True)
    mpaa_rating = models.CharField(_('возрастной рейтинг'), choices=MPAARatingType.choices, null=True, max_length=50)
    file_path = models.FileField(_('файл'), upload_to='film_works/', null=True, blank=True)
    rating = models.FloatField(_('рейтинг'), validators=[MinValueValidator(0)], null=True, blank=True)
    type = models.TextField(_('тип'), choices=FilmWorkType.choices, blank=True)
    genres = models.ManyToManyField('Genre', through='GenreFilmWork')
    persons = models.ManyToManyField('Person', through='FilmWorkPerson')
    created_at = AutoCreatedField(_('дата создания'))
    updated_at = AutoLastModifiedField(_('дата последнего изменения'))

    class Meta:
        verbose_name = _('кинопроизведение')
        verbose_name_plural = _('кинопроизведения')
        db_table = 'content.film_work'

    def __str__(self):
        return self.title


class FilmWorkPerson(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(_('роль'), choices=RoleType.choices)
    created_at = AutoCreatedField(_('дата создания'))

    class Meta:
        verbose_name = _('участник кинопроизведение')
        verbose_name_plural = _('участники кинопроизведения')
        db_table = 'content.person_film_work'
        unique_together = ('film_work', 'person', 'role')


class GenreFilmWork(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created_at = AutoCreatedField(_('дата создания'))

    class Meta:
        verbose_name = _('жанр кинопроизведение')
        verbose_name_plural = _('жанры кинопроизведения')
        db_table = 'content.genre_film_work'
        unique_together = ('film_work', 'genre')
