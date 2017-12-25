# Tournament Planner

by Yasser Albarbary, in fulfillment of Udacity's [Full-Stack Web Developer Nanodegree 2015]

### About

This project provides a Python module that uses a PostgreSQL database to keep track of players and matches in a game tournament, using the Swiss pairing system.

### How to run

This directory can be initiated with [Vagrant](https://www.vagrantup.com/) by executing the command `vagrant up` within the `vagrant/` directory.  The test cases can be run by executing the following commands:

- `vagrant ssh`
- `cd /vagrant/tournament`
- `python tournament_test.py`



Note that
- `/vagrant/tournament/tournament.sql`  file needs to be executed to build the tournament database. 
- the last line of the output from tournament_test.py should be "Success! All tests pass"
- the test suite wipes and adds records to the database, so in the off chance that you are using this in a production environment, do not execute it!
