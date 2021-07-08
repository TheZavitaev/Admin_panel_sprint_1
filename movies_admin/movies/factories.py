import random

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from .models import Person, Genre, FilmWork, FilmWorkPerson, GenreFilmWork, MPAARatingType, FilmWorkType, RoleType

# See the list of factory providers at
# https://faker.readthedocs.io/en/stable/providers.html


description = factory.Faker(
        'sentence',
        nb_words=128,
        variable_nb_words=True
    )
customer_name = factory.Faker("name")
customer_address = factory.Faker("address")
creation_date = factory.Faker("date")
factory.Faker('catch_phrase')
name = factory.Faker('company')


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    full_name = factory.Faker('name')
    birth_date = factory.Faker('date')
    created_at = factory.Faker('date')


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker('company')
    description = factory.Faker('sentence', nb_words=128, variable_nb_words=True)
    created_at = factory.Faker('date')


class FilmWorkFactory(DjangoModelFactory):
    class Meta:
        model = FilmWork

    title = factory.Faker('company')
    description = factory.Faker('sentence', nb_words=128, variable_nb_words=True)
    creation_date = factory.Faker('date')
    certificate = factory.Faker('company')
    mpaa_rating = FuzzyChoice(MPAARatingType)
    file_path = factory.Faker('name')
    rating = factory.LazyAttribute(random.randrange(0, 11))
    type = FuzzyChoice(FilmWorkType)
    genres = factory.Faker('company')
    persons = factory.Faker('name')
    created_at = factory.Faker('date')
    updated_at = factory.Faker('date')


class FilmWorkPersonFactory(DjangoModelFactory):
    class Meta:
        model = FilmWorkPerson

    film_work = factory.SubFactory(FilmWorkFactory)
    person = factory.Faker('name')
    role = FuzzyChoice(RoleType)
    created_at = factory.Faker('date')


class GenreFilmWorkFactory(DjangoModelFactory):
    class Meta:
        model = GenreFilmWork

    film_work = factory.SubFactory(FilmWorkFactory)
    genre = factory.SubFactory(GenreFactory)
    created_at = factory.Faker('date')
