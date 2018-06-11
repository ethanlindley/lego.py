from mongoengine import *


class Account(Document):
    account_id = SequenceField(collection_name='lego-py.account')
    username = StringField(required=True)
    password = StringField(required=True)
    banned = BooleanField(required=True)
    is_admin = BooleanField(required=True)
