"""Database Model"""

__author__ = "Keith Hamm"
__copyright__ = "Copyright 2014, Analytic Spot"

# Std libs
import uuid

# cqlengine libs
from cqlengine import columns
from cqlengine.models import Model


class Event(Model):
    """
    Analytic Event
    """
    __keyspace__ = 'ans'
    __table_name__ = 'events'

    event_id = columns.UUID(primary_key=True, default=uuid.uuid4)

    # Required General Event Columns

    api_key = columns.Text(primary_key=True, required=True)
    device_code = columns.UUID(required=True)
    app_id = columns.Text(required=True)
    session_id = columns.UUID(required=True)
    event_type = columns.Text(required=True)
    # event_timestamp is when the item was completed
    event_timestamp = columns.Text(required=True)

    # Required Item Event Columns

    correctness = columns.Boolean()
    item_on_item = columns.Float()

    # Other General Events Columns

    ip_address = columns.Text()
    client_timestamp = columns.Text()
    # collection is the name of the collection
    collection = columns.Text()
    lat_long = columns.Text()

    # Server Generated General Event Columns

    location = columns.Text()
    # at_school choices: -1 unknown, 0 no, 1 yes
    at_school = columns.Text(default=-1)

    # Other Item Event Columns

    # Set or list?
    problem_types = columns.Set(value_type=columns.Text)
    item_code = columns.Text()
    item_response = columns.Text()
    difficulty = columns.Integer()
    attempts = columns.Integer()


# todo2: will these ITEM properties below become _ans_ prefixed and the library handling it on ios?


# Education specifc event details (store all in flexible json)
# L1 - most important
#   time_on_item - (L1) how long was spent on the item (float in secs, eg: 3.23) [api: float/int/str]
#   first_try_correct (L1) (int 0=no, 1=yes)  [api: int or str]

# L2 less important but helpful
#   item_id (L2 but opt) - anything unique that identifies each question (1+1, 1>2, etc) [api: str]
#   item_difficulty (L2 but opt) - this could be mangled later based on item_id.
#   item_type (opt) - type of item, any unique name to distinguish. only necessary if app has multiple problem types
#   errors_before_correct (opt) - if they get multiple chances to get it correct, how many did it take (0 means they got it right on first try)
#   response_options_count (opt) - if multiple options


# future: Lower Priority
# todo2: country = models.CharField(max_length=2, null=True, blank=True) # two-letter country code
#   item_description - fuller description of the item (e.g. )
#   response_options - actual options for
#   response_value - could be the correct value only or array of each one tried

# FUTURE: Auth only fields
# user_id = models.CharField(max_length=50, null=True, blank=True) # if learner logged in, pushes this as well (in case different learners per device)
# latitude = models.CharField(max_length=50, null=True, blank=True) # future:collapse lat/long into single field?
# longitude = models.CharField(max_length=50, null=True, blank=True)
# ip_address = models.CharField("IP Address", max_length=50, null=True, blank=True) # future: ip-address specific field

# future: handle implications of malfeasance if pushes multiple events with same event_id. what havoc would that cause.
