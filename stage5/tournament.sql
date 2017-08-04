-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament; 

\c tournament;

CREATE TABLE players (name TEXT,
                     id SERIAL PRIMARY KEY);

-- table contains the matches played between players.
-- winner and loser are foreign keys as they need to have been defined in the "players" table

CREATE TABLE matches (winner int REFERENCES players(id),
                     loser int REFERENCES players(id),
                     id SERIAL PRIMARY KEY);



