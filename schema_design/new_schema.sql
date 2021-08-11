-- Я не совсем понял требования к этому заданию, в ТЗ от джанги увидел,
-- что они должны быть идентичны, поэтому догнал схему тем, что мы добавили в джангу

-- Создаем схему
CREATE SCHEMA IF NOT EXISTS content;

-- Добавляем нумерованные типы для ролей
CREATE TYPE content.film_team_role AS ENUM ('director', 'writer', 'actor');

-- Делаем тоже самое для типов кинопроизведений
CREATE TYPE content.film_work_types AS ENUM ('movie', 'series', 'tv_show');

-- И для MPAA рейтинга
CREATE TYPE content.film_mpaa_rating_type AS ENUM ('g', 'pg', 'pg_13', 'r', 'nc_17');


-- Создаем таблицы

CREATE TABLE IF NOT EXISTS content.film_work (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    mpaa_rating content.film_mpaa_rating_type,
    file_path TEXT,
    imdb_rating NUMERIC(2,1) CHECK (imdb_rating >= 0,0),
    type content.film_work_types,
    created_at TIMESTAMP with time zone,
    updated_at TIMESTAMP with time zone
);

-- В реальном проекте я бы тоже использовал ENUM и здесь, но упрощу для учебных целей
CREATE TABLE IF NOT EXISTS content.genre (
    id UUID PRIMARY KEY,
    name varchar NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP with time zone
);

CREATE TABLE IF NOT EXISTS content.film_work_genre (
    id UUID PRIMARY KEY,
    film_work_id UUID REFERENCES content.film_work (id),
    genre_id UUID REFERENCES content.genre (id),
    created_at TIMESTAMP with time zone,
    UNIQUE (film_work_id, genre_id)
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    birthdate DATE
);

CREATE TABLE IF NOT EXISTS content.film_work_person (
    id UUID PRIMARY KEY,
    film_work_id UUID REFERENCES content.film_work (id),
    person_id UUID REFERENCES content.person (id),
    role content.film_team_role,
    UNIQUE (film_work_id, person_id, role)
);

-- Создаем индекс
CREATE INDEX film_work_creation_date_idx ON content.film_work(creation_date);
