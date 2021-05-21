-- Создаем схему
CREATE SCHEMA IF NOT EXISTS content;

-- Добавляем нумерованные типы для ролей
CREATE TYPE film_team_role AS ENUM ('director', 'writer', 'actor');

-- Создаем таблицы

CREATE TABLE IF NOT EXISTS content.film_work (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT
    creation_date DATE,
    imdb_rating FLOAT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id UUID PRIMARY KEY,
    name varchar NOT NULL UNIQUE,
);

CREATE TABLE IF NOT EXISTS content.film_work_genre (
    id UUID PRIMARY KEY,
    movie_id UUID REFERENCES content.film_work (id),
    genre_id UUID REFERENCES content.genre (id),
    UNIQUE (film_work_id, genre_id)
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    birthdate DATE
);

CREATE TABLE IF NOT EXISTS content.film_work_person (
    id UUID PRIMARY KEY,
    movie_id UUID REFERENCES content.film_work (id),
    person_id UUID REFERENCES content.person (id),
    role film_team_role,
    UNIQUE (film_work_id, person_id, role)
);
