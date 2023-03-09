CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    lng FLOAT NOT NULL,
    lat FLOAT NOT NULL,
    place_name TEXT UNIQUE,
    peacefulness INTEGER
);

CREATE TABLE locations (id SERIAL PRIMARY KEY, creator INTEGER REFERENCES users, lng FLOAT NOT NULL, lat FLOAT NOT NULL, place_name TEXT UNIQUE, peacefulness INTEGER);

CREATE TABLE form_data (
  id serial PRIMARY KEY,
  creator INTEGER REFERENCES users,
  lng FLOAT NOT NULL,
  lat FLOAT NOT NULL,
  place_name TEXT UNIQUE,
  space INT NOT NULL,
  ground_type VARCHAR(20) NOT NULL,
  surroundings INT NOT NULL,
  crowds INT NOT NULL,
  light INT NOT NULL,
  restrooms VARCHAR(20) NOT NULL,
  image bytea,
  CHECK (ground_type IN ('grass', 'asphaltetc', 'gravel', 'indoor', 'other')),
  CHECK (restrooms IN ('Yes', 'No', 'NoInfo'))
);

CREATE TABLE sections (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    access INTEGER DEFAULT 1
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP,
    message TEXT,
    user_id INTEGER REFERENCES users,
    section_id INTEGER REFERENCES sections,
    visible INTEGER DEFAULT 1
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES threads,
    sent_at TIMESTAMP,
    answer TEXT,
    user_id INTEGER REFERENCES users,
    visible INTEGER DEFAULT 1
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    answer_id INTEGER REFERENCES answers,
    user_id INTEGER REFERENCES users,
    vote INTEGER
);

ALTER TABLE users ADD COLUMN role INT NOT NULL DEFAULT 1;
UPDATE users SET role=1;
