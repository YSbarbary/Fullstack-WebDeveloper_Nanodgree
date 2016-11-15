# Udacity nano dgree project 2
# tournament.py -- implementation for Swiss-system tournament
#

import psycopg2
DBNAME = "tournament"
def connect (dbname=DBNAME):
	""" Connect to the PostgreSQL database.  Returns a database connection."""
	return psycopg2.connect('dbname='+ dbname)
def connect(database_name=DBNAME):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Cannot connect to database")
	
def registerPlayer(playerName):
	"""register new player in the tournament, add to players table."""
	db, cursor = connect()
	query = """
	INSERT INTO players (name) VALUES (%s)
	"""
	parameter = (playerName,)
	cursor.execute(query, parameter)
	db.commit()
	db.close()

def countPlayers():
	"""Returns the number of players currently registered."""
	db, cursor = connect()
	query = """
	SELECT COUNT(id) from players;
	"""
	cursor.execute(query)
	result = cursor.fetchall()
	db.close()
	assert len(result) == 1
	return int(result[0][0])

def matchResult(winner, loser):
	"""Records the result of a single match between two players."""
	db, cursor = connect()
	query = """
    INSERT INTO matches (winner_id, loser_id)
    VALUES (%s, %s)
    """.format(winner_id=winner, loser_id=loser)
	parameters = (winner,loser)
	cursor.execute(query, parameters )
	db.commit()
	db.close()
def playerStanding():
	"""Return player WIns sorted by number of wins """
	""" Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
     """
	db, cursor = connect()
	query = """SELECT players.id, name , count(matches.id) as {win_or_lose}
				FROM players LEFT JOIN matches
				ON players.id = {field}_id
				GROUP BY players.id
				ORDER BY {win_or_lose} DESC
				"""
	query_wins = query.format(field='winner', win_or_lose='wins')
	query_losses = query.format(field='loser', win_or_lose='losses')
	
	query_all = """SELECT winners.id, winners.name, wins, wins+losses AS matches
				    FROM ({query_wins}) AS winners LEFT JOIN ({query_losses}) as losers
				    ON winners.id = losers.id
				    """.format(query_wins=query_wins, query_losses=query_losses)
	cursor.execute(query_all + ';')
	results = cursor.fetchall()
	db.close()
	return results
	
def swissPairing():
	"""Returns a list of pairs of players for the next round of a match."""
	standings = [(record[0], record[1]) for record in playerStanding()]
	if len(standings) < 2:
		raise KeyError("Not enough players.")
	left = standings[0::2]
	right = standings[1::2]
	pairings = zip(left, right)

	# flatten the pairings and convert back to a tuple
	results = [tuple(list(sum(pairing, ()))) for pairing in pairings]

	return results
	
def deleteMatches():
	"""Remove all the match records from the database."""
	db, cursor = connect()
	query = """
	DELETE FROM matches;
	"""
	cursor.execute(query)
	db.commit()
	db.close()

def deletePlayers():
	"""Remove all the player records from the database."""
	db, cursor = connect()
	query = """
	DELETE FROM players;
	"""
	cursor.execute(query)
	db.commit()
	db.close()
	
