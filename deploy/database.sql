CREATE TABLE urls (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name varchar(255),
    created_at DATE
);

CREATE TABLE url_checks (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    url_id BIGINT REFERENCES urls (id),
    status_code BIGINT,
    h1 varchar(255),
    title varchar(255),
    description varchar(255),
    created_at DATE
);