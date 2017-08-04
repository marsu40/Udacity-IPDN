#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random

#########################
### Helper functions ####
#########################

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def update_database(query, vars = None):
    """ Update and commit the database thru the query

    Args:
        query : SQL statement to be executed
        vars : Possible variables to be inserted in the query in the form of a tuple
    """
    conn = connect()
    c = conn.cursor()
    if vars == None:
        c.execute(query)
    else:
        c.execute(query, vars)
    conn.commit() 
    conn.close()

def list_by_wins():
    '''
    Returns a list of list of tuples containing players (id, name)
    with each player having the same number of wins regrouped in the same list
    '''
    standings = playerStandings() 
    # we now have a list of tuples of the following format : (id, name, wins, matches)
    result = []
    current_wins = -1 # initialized to a non-existing value
    for p in standings:
        if current_wins == -1:
            current_wins = p[2] # number of wins of this player
            current = [(p[0], p[1])] # (id, name)
        elif current_wins == p[2]:
            # Same number of wins so append it in the same list
            current.append((p[0], p[1])) 
        else:
            # the current list is now complete, we can add it to the result 
            # and reinitialize current with the new player
            result.append(current)
            current_wins = p[2]
            current = [(p[0], p[1])]
    # add last current list to the result
    result.append(current)
    return result


########################
### Module functions ###
#######################

def deleteMatches():
    """Remove all the match records from the database."""
    update_database("DELETE FROM matches;")

def deletePlayers():
    """Remove all the player records from the database."""
    update_database("DELETE FROM players;") 


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT Count(id) AS num FROM Players;")
    # the search returns a single column single row containing the number of players in the database
    # so we extract it with the next command
    res = c.fetchall()[0][0]
    conn.close()  
    return res

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    update_database("INSERT INTO players VALUES (%s)", (name,))
     

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    result = [] # will contain the list of tuples
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id from players;")
    # get a list of all the players ids
    ids = c.fetchall() 
    for idx in ids:
        c.execute("SELECT name from players WHERE id = %s;", (idx[0],))
        # retrieve the name of the player with the id: "idx"
        name = c.fetchall()[0][0] 
        c.execute("SELECT count(*) from matches WHERE winner = %s;", (idx[0],))
        # get the number of wins of this specific player
        wins = int(c.fetchall()[0][0])
        c.execute("SELECT count(*) from matches WHERE winner = %s OR loser = %s;", (idx[0],idx[0],))
        # return the number of matches played
        matches = int(c.fetchall()[0][0])
        result.append((int(idx[0]), name, wins, matches))
    conn.close()
    if len(result):     
        return sorted(result, key=lambda tup: tup[2]) # Sorting adapted from the following link: http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    update_database("INSERT INTO matches VALUES (%s, %s)", (winner, loser))    

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairing = []
    lbw = list_by_wins()
    p1 =  ()
    for players in lbw:
        while len(players):
            # if p1 is not empty this means it could not be paired before sonothing to do
            # otherwise, let's take the first player in the list 

            if len(p1) == 0:
                p1 = players.pop(0)
            # if players list is not empty then we can proceed
            # and pair p1 randomly with one of the remaining players in the list
            if len(players):
                p2 = random.choice(players)
                players.remove(p2)
                pairing.append(p1 + p2)
                p1 = () # clearing p1 content to avoid repairing it wiht another player
    return pairing
