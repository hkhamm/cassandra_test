import logging
import uuid
import arrow
from random import randint
import dateutil.parser

# Local libs
from models_cassandra import Event

# cqlengine libs
from cqlengine import connection

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

URLS = ['127.0.0.1'] #  ['10.0.1.61', '10.0.1.199', '10.0.1.198'] #
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME,
                                      password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

time = arrow.utcnow()

print('Posting...')
year = 2014
for i in range(100000):
    month = randint(7,8)
    monthString = '0' + str(month)

    day = randint(1,31)
    if(day < 10):
        dayString = '0' + str(day)
    else:
        dayString = str(day)

    hour = randint(0,23)
    if(hour < 10):
        hourString = '0' + str(hour)
    else:
        hourString = str(hour)

    minute = randint(0,59)
    if(minute < 10):
        minuteString = '0' + str(minute)
    else:
        minuteString = str(minute)

    timestampString = str(year) + "-" + monthString + "-" + dayString + " " + hourString + ":" + minuteString + ":" + "00+00:00"
    timestamp = arrow.get(timestampString, 'YYYY-MM-DD HH:mm:ss')
    Event.create(event_id=str(uuid.uuid4()),
                             api_key='secret-ans-8g9xb-key',
                             app_id='app_id1',
                             device_code=str(uuid.uuid4()),
                             session_id=str(uuid.uuid4()),
                             event_timestamp=dateutil.parser.parse(timestampString),
                             event_type='null',
                             ip_address='127.0.0.1',
                             collection='test',
                             lat_long='27.175015, 78.042155',
                             at_school='1',
                             location='location 1')

print('Posting began ' + time.humanize())
