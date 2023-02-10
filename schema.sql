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
