# My tournament project

This is a module which allows to store and pairs players during a tournament (swiss system).

This folder contains 4 files:

- README.md : This file
- tournament.sql : Database definition, see bellow how to use this file
- tournament.py : module containing the definiton of the Python functions which interacts with the database
- tournament_test.py : test module for the tournament.py module

## Installation

Create the datase thru the following steps:
```
	ubuntu@ubuntu-xenial:/vagrant/tournament$ psql
	psql (9.5.6)
	Type "help" for help.
	ubuntu=> \i tournament.sql
	DROP DATABASE
	CREATE DATABASE
	You are now connected to database "tournament" as user "ubuntu".
	CREATE TABLE
	CREATE TABLE
	tournament=>
```
Everything is now ready, you can safely exit psql command line (\q)
To confirm all is working propermy, launch tournament.py module's functions:
```
	ubuntu@ubuntu-xenial:/vagrant/tournament$ python tournament_test.py 
	1. countPlayers() returns 0 after initial deletePlayers() execution.
	2. countPlayers() returns 1 after one player is registered.
	3. countPlayers() returns 2 after two players are registered.
	4. countPlayers() returns zero after registered players are deleted.
	5. Player records successfully deleted.
	6. Newly registered players appear in the standings with no matches.
	7. After a match, players have updated standings.
	8. After match deletion, player standings are properly reset.
	9. Matches are properly deleted.
	10. After one match, players with one win are properly paired.
	Success!  All tests pass!
```

## Usage

Here is a list of the functions available in the module along with a brief description:

- deleteMatches(): Remove all the match records from the database.

- deletePlayers(): Remove all the player records from the database.

- countPlayers(): Returns the number of players currently registered.

- registerPlayer(name): Adds a player to the tournament database.

- playerStandings(): Returns a list of the players and their win records, sorted by wins.

- reportMatch(winner, loser): Records the outcome of a single match between two players.

- swissPairings(): Returns a list of pairs of players for the next round of a match.
  


