-- Table definitions for the tournament project.
--
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players (id serial primary key,
					  name varchar(1000) not null,
					  created_at timestamp default current_timestamp);

CREATE TABLE matches (id serial primary key,
					  winner_id int,
					  loser_id int,
					  foreign key (winner_id) references players(id),
					  foreign key (loser_id) references players(id),
					  created_at timestamp default current_timestamp);
--
-- You can write comments in this file by starting them with two dashes, like
