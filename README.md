Cassandra Test
==============

These python scripts provide a few different ways to interact with the Cassandra database. This only works from the same subnet as the database servers.

post.py
-------

Posts a new event to the database. If modifying the sent make sure you keep all the column datatypes and names the same.

```
python post.py
```

query.py
--------

Queries the database and returns all events. Currently gets all events, stores them in an Event object, and prints them out a line at a time as dictionaries.

```
python query.py
```

models_cassandra.py
-------------------

The Event model. Don't modify this.


sync_cassandra.py
-----------------

Creates the initial keyspace and event table in the database. Run only on an empty database, otherwise it does nothing.
