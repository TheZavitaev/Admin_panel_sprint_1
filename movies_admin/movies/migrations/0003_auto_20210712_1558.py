# Generated by Django 3.1 on 2021-07-12 15:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='дата создания фильма')),
                ('certificate', models.TextField(blank=True, null=True, verbose_name='сертификат')),
                ('mpaa_rating', models.CharField(choices=[('general', 'без ограничений'), ('parental_guidance', 'рекомендовано смотреть с родителями'), ('parental_guidance_strong', 'просмотр не желателен детям до 13 лет'), ('restricted', 'до 17 в сопровождении родителей'), ('no_one_17_under', 'только с 18')], max_length=50, null=True, verbose_name='возрастной рейтинг')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='film_works/', verbose_name='файл')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='рейтинг')),
                ('type', models.TextField(blank=True, choices=[('film', 'фильм'), ('series', 'сериал'), ('tv_show', 'шоу')], verbose_name='тип')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='дата создания')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'кинопроизведение',
                'verbose_name_plural': 'кинопроизведения',
                'db_table': 'content.film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='дата создания')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'verbose_name': 'жанр кинопроизведение',
                'verbose_name_plural': 'жанры кинопроизведения',
                'db_table': 'content.genre_film_work',
                'unique_together': {('film_work', 'genre')},
            },
        ),
        migrations.CreateModel(
            name='FilmWorkPerson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('role', models.TextField(choices=[('actor', 'актер'), ('writer', 'сценарист'), ('director', 'режиссер')], verbose_name='роль')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='дата создания')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'verbose_name': 'участник кинопроизведение',
                'verbose_name_plural': 'участники кинопроизведения',
                'db_table': 'content.person_film_work',
                'unique_together': {('film_work', 'person', 'role')},
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.FilmWorkPerson', to='movies.Person'),
        ),
    ]
