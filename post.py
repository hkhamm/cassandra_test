import logging
import uuid
import arrow
import dateutil.parser

# Local libs
from models_cassandra import Event

# cqlengine libs
from cqlengine import connection

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

URLS = ['54.68.10.142'] #  ['10.0.1.61', '10.0.1.199', '10.0.1.198'] #
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME,
                                      password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

time = arrow.utcnow()

print('Posting...')

for i in range(10000):
    timestamp = arrow.utcnow().to('local').format('YYYY-MM-DDTHH:mm:ssZZ')
    Event.create(event_id=str(uuid.uuid4()),
	         api_key='secret-ans-8g9xb-key',
	         app_id='app_id1',
		 device_code=str(uuid.uuid4()),
                 session_id=str(uuid.uuid4()),
	         event_timestamp=dateutil.parser.parse(timestamp),
	         event_type='null',
		 ip_address='127.0.0.1',
		 collection='test',
		 lat_long='27.175015, 78.042155',
		 at_school='1',
		 location='location 1')

print('Posting began ' + time.humanize())
