from mongoengine import *


class Account(Document):
    account_id = IntField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    banned = BooleanField(required=True)
    is_admin = BooleanField(required=True)
    characters = ListField()
